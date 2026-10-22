"""Short-video script tool: read the team's Excel format, check structure, export back to Excel.

Usage:
    py -I kich_ban.py doc  <in.xlsx> <out.json>   # Excel (team format) -> JSON
    py -I kich_ban.py kiem <in.json>              # structural checks, exit 1 on any "Nặng" error
    py -I kich_ban.py xuat <in.json> <out.xlsx>   # JSON -> Excel (team format)

Format spec: shared/luat/format-kich-ban.md. Error codes: shared/luat/loi-kich-ban.md.

Needs openpyxl. When the system Python lacks it, the script installs it into <repo>/.cong-cu/venv (the same
git-ignored venv phan_tich_mau.py uses) and re-runs itself there, so a fresh clone needs nothing but Python.
"""
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

VENV = Path(__file__).resolve().parents[2] / ".cong-cu" / "venv"
VENV_PY = VENV / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


def _ensure_openpyxl():
    try:
        import openpyxl  # noqa: F401
        return
    except ImportError:
        pass
    pip = ["-m", "pip", "install", "--disable-pip-version-check", "-q", "openpyxl"]
    if Path(sys.prefix).resolve() == VENV.resolve():
        subprocess.run([sys.executable, *pip], check=True)
        return
    if not VENV_PY.exists():
        print("Lần đầu: tạo môi trường riêng ở .cong-cu/venv ...")
        subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
    if subprocess.run([str(VENV_PY), "-I", "-c", "import openpyxl"], capture_output=True).returncode:
        print("Lần đầu: cài openpyxl (đọc / ghi Excel) ...")
        subprocess.run([str(VENV_PY), *pip], check=True)
    sys.exit(subprocess.run([str(VENV_PY), "-I", str(Path(__file__).resolve()), *sys.argv[1:]]).returncode)


_ensure_openpyxl()

import openpyxl  # noqa: E402
from openpyxl.styles import Alignment, Font, PatternFill  # noqa: E402

HEADERS = ["STT", "Tóm tắt - Title", "Địa điểm", "Mục đích", "Nhân vật",
           "Nội dung", "Biểu cảm", "Góc quay", "Text nổi bật", "Ghi chú"]
SCENE_KEYS = ["muc_dich", "nhan_vat", "noi_dung", "bieu_cam", "goc_quay", "text_noi_bat", "ghi_chu"]
REQUIRED_SCENE_KEYS = ["muc_dich", "nhan_vat", "noi_dung", "goc_quay"]
MAX_ACTORS = 6  # see shared/luat/dieu-kien-san-xuat.md
# Common Vietnamese words in their diacritic-stripped form (là, thôi, không, được...).
STRIPPED_WORDS = {"la", "thoi", "khong", "duoc", "nguoi", "nhung", "cua", "voi", "roi", "gi", "nay", "dang",
                  "nhieu", "minh", "toi", "phai", "biet", "muon", "lam", "trong", "quan", "y", "a", "di", "day"}

# Overview block printed above each script's table: (label, key, stored under kb["overview"]?)
OVERVIEW_FIELDS = [
    ("Tóm tắt", "tom_tat", False),
    ("Title", "title", False),
    ("Nhóm chủ đề", "chu_de", True),
    ("Thông điệp", "thong_diep", True),
    ("Khán giả chính", "khan_gia", True),
    ("Tông", "tong", True),
    ("Hook", "hook", True),
    ("Diễn biến chính", "dien_bien", True),
    ("Kết", "ket", True),
    ("Nhân vật", "nhan_vat", True),
    ("Địa điểm", "dia_diem", False),
    ("Thời điểm", "boi_canh", False),
    ("Đạo cụ", "dao_cu", False),
    ("Lưu ý sản xuất", "luu_y_san_xuat", True),
]
OVERVIEW_BY_LABEL = {label: (key, nested) for label, key, nested in OVERVIEW_FIELDS}
OVERVIEW_REQUIRED = ["chu_de", "thong_diep", "hook", "nhan_vat"]
SEC_OVERVIEW, SEC_SCRIPT = "TỔNG QUAN", "KỊCH BẢN CHI TIẾT"

TITLE_RE = re.compile(r"^Kịch bản\s*(\d+)\s*:\s*(.*?)\s*\((?:Thời lượng dự kiến:\s*)?([^()]*)\)\s*$")
GIAY_RE = re.compile(r"^(.*?)\s*\((\d+\s*[–-]\s*\d+\s*s)\)\s*$")


def _s(v):
    return "" if v is None else str(v).strip()


# ---------------------------------------------------------------- doc (xlsx -> json)

def doc(path_in, path_out):
    """Read both layouts: one sheet per script (current) and several scripts stacked in one sheet (old)."""
    wb = openpyxl.load_workbook(path_in)
    scripts, cur, in_table = [], None, False
    rows = [row for ws in wb.worksheets for row in ws.iter_rows(min_row=1, max_col=10, values_only=True)]
    for row in rows:
        cells = [_s(v) for v in row]
        a = cells[0]
        if not any(cells):
            continue
        m = TITLE_RE.match(a)
        if m:
            cur = {"so": int(m.group(1)), "ten": m.group(2), "thoi_luong": m.group(3).strip(),
                   "boi_canh": "", "dao_cu": "", "tom_tat": "", "title": "", "dia_diem": "", "canh": []}
            scripts.append(cur)
            in_table = False
            continue
        if cur is None or a in (SEC_OVERVIEW, SEC_SCRIPT):
            continue
        if a == "STT":
            in_table = True
            continue
        if not in_table:
            if a in OVERVIEW_BY_LABEL:
                key, nested = OVERVIEW_BY_LABEL[a]
                if nested:
                    cur.setdefault("overview", {})[key] = cells[2]
                else:
                    cur[key] = cells[2]
            elif a.startswith("Đạo cụ:"):
                cur["dao_cu"] = a[len("Đạo cụ:"):].strip()
            else:
                cur["boi_canh"] = re.sub(r"\s+", " ", a)
            continue
        # Scene row
        if cells[1]:
            parts = re.split(r"\n\s*Title\s*:\s*", cells[1], maxsplit=1)
            cur["tom_tat"] = parts[0].strip()
            cur["title"] = parts[1].strip() if len(parts) > 1 else ""
        if cells[2] and not cur["dia_diem"]:
            cur["dia_diem"] = cells[2]
        scene = dict(zip(SCENE_KEYS, [cells[3], cells[4], cells[5], cells[6], cells[7], cells[8], cells[9]]))
        gm = GIAY_RE.match(scene["muc_dich"])
        scene["giay"] = ""
        if gm:
            scene["muc_dich"], scene["giay"] = gm.group(1), gm.group(2).replace(" ", "")
        if cells[2] and cells[2] != cur["dia_diem"]:
            scene["dia_diem"] = cells[2]
        cur["canh"].append(scene)
    data = {"du_an": wb.properties.title or wb.worksheets[0].title, "kich_ban": scripts}
    with open(path_out, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Đã đọc {len(scripts)} kịch bản, {sum(len(k['canh']) for k in scripts)} beat → {path_out}")


# ---------------------------------------------------------------- kiem (checks)

def _no_diacritics_line(line):
    """True when a 4+ word clause is typed without diacritics (likely a draft note in dialogue).

    Plain-ASCII clauses are legit for English terms ("Zoom out ra xa"), so it also needs 2+ words
    that are normally written with diacritics (la -> là, thoi -> thôi...).
    """
    for clause in re.split(r"[,.:;!?\"“”()]", line):
        words = re.findall(r"[A-Za-zÀ-ỹ]+", clause)
        if len(words) < 4 or not all(ord(ch) < 128 for w in words for ch in w):
            continue
        if sum(1 for w in words if w.lower() in STRIPPED_WORDS) >= 2:
            return True
    return False


def _actors(nhan_vat):
    text = re.sub(r"\(.*?\)", "", nhan_vat)
    if re.search(r"cả\s*\d+\s*người", text, re.I):
        return None  # group label, counted by other beats
    names = [n.strip() for n in re.split(r"[+,&]| và ", text) if n.strip()]
    return [re.sub(r"^voice\s+", "", n, flags=re.I) for n in names]


def kiem(path_in):
    with open(path_in, encoding="utf-8") as f:
        data = json.load(f)
    issues = []  # (level, code, where, message)

    def add(level, code, where, msg):
        issues.append((level, code, where, msg))

    long_lines = {}  # normalized line -> script number, to catch copy-paste across scripts
    for kb in data.get("kich_ban", []):
        so = kb.get("so", "?")
        tag = f"KB{so}"
        for key in ["ten", "thoi_luong", "dao_cu", "tom_tat", "title", "dia_diem"]:
            if not _s(kb.get(key)):
                add("Vừa", "NH-03", tag, f"thiếu trường '{key}'")
        for key in OVERVIEW_REQUIRED:
            if not _s((kb.get("overview") or {}).get(key)):
                add("Nhẹ", "NH-03", tag, f"phần tổng quan thiếu 'overview.{key}'")
        canh = kb.get("canh", [])
        if not canh:
            add("Nặng", "NH-03", tag, "không có beat nào")
            continue
        first = canh[0]
        if "hook" not in _s(first.get("muc_dich")).lower() or not _s(first.get("giay")):
            add("Vừa", "HK-03", f"{tag} beat 1", "beat đầu phải ghi Mục đích có 'Hook' và mốc giây (giay)")
        if not _s(canh[-1].get("text_noi_bat")):
            add("Nhẹ", "KT-02", f"{tag} beat {len(canh)}", "beat cuối chưa có Text nổi bật")

        actors = set()
        for i, c in enumerate(canh, 1):
            where = f"{tag} beat {i}"
            for key in REQUIRED_SCENE_KEYS:
                if not _s(c.get(key)):
                    add("Vừa", "NH-03", where, f"trống cột '{key}'")
            names = _actors(_s(c.get("nhan_vat")))
            if names:
                actors.update(n.lower() for n in names)
            for line in _s(c.get("noi_dung")).splitlines():
                line = line.strip()
                if _no_diacritics_line(line):
                    add("Vừa", "NH-02", where, f"dòng không dấu, có thể là ghi chú nháp: {line[:60]}")
                norm = unicodedata.normalize("NFC", re.sub(r"\s+", " ", line)).lower()
                if len(norm) >= 40:
                    other = long_lines.setdefault(norm, so)
                    if other != so:
                        add("Nặng", "NH-01", where, f"đoạn trùng nguyên văn với kịch bản {other}: {line[:60]}…")
        if len(actors) > MAX_ACTORS:
            add("Nặng", "SX-01", tag, f"{len(actors)} nhân vật ({', '.join(sorted(actors))}) > {MAX_ACTORS} diễn viên")

    order = {"Nặng": 0, "Vừa": 1, "Nhẹ": 2}
    issues.sort(key=lambda x: order[x[0]])
    if not issues:
        print("kiem: không có lỗi cấu trúc.")
        return 0
    print("| Mức | Mã | Vị trí | Vấn đề |\n|---|---|---|---|")
    for lv, code, where, msg in issues:
        print(f"| {lv} | {code} | {where} | {msg} |")
    n_heavy = sum(1 for x in issues if x[0] == "Nặng")
    print(f"\nTổng: {len(issues)} lỗi, {n_heavy} Nặng.")
    return 1 if n_heavy else 0


# ---------------------------------------------------------------- xuat (json -> xlsx)

COL_WIDTHS = [6, 26, 16, 20, 16, 50, 20, 20, 22, 18]  # A..J, sized for 12pt text; F (Nội dung) is the long column
OVERVIEW_CHARS_PER_LINE = 140                          # rough fit of 12pt text across merged C:J


def _sheet_name(kb, used):
    name = re.sub(r"[\[\]:*?/\\]", "", f"KB{kb['so']} - {_s(kb.get('ten'))}").strip()[:31] or f"KB{kb['so']}"
    base, n = name, 2
    while name in used:
        name = f"{base[:28]}({n})"
        n += 1
    used.add(name)
    return name


def xuat(path_in, path_out):
    with open(path_in, encoding="utf-8") as f:
        data = json.load(f)
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    wb.properties.title = _s(data.get("du_an")) or "Kịch bản"
    color = "FF1F1F1F"
    f_title = Font(name="Times New Roman", size=13, bold=True, color=color)
    f_section = Font(name="Times New Roman", size=12, bold=True, color=color)
    f_label = Font(name="Times New Roman", size=12, bold=True, color=color)
    f_body = Font(name="Times New Roman", size=12, color=color)
    yellow = PatternFill("solid", fgColor="FFFFFF00")
    grey = PatternFill("solid", fgColor="FFD9D9D9")
    wrap = Alignment(wrap_text=True, vertical="top")

    used = set()
    for kb in data.get("kich_ban", []):
        ws = wb.create_sheet(_sheet_name(kb, used))
        for col, width in zip("ABCDEFGHIJ", COL_WIDTHS):
            ws.column_dimensions[col].width = width

        def section(row, text):
            c = ws.cell(row, 1, text)
            c.font, c.fill = f_section, grey
            ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=10)

        r = 1
        ws.cell(r, 1, f"Kịch bản {kb['so']}: {kb['ten']} (Thời lượng dự kiến: {kb['thoi_luong']})").font = f_title
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=10)
        r += 1
        section(r, SEC_OVERVIEW)
        r += 1
        overview = kb.get("overview") or {}
        for label, key, nested in OVERVIEW_FIELDS:
            value = _s(overview.get(key) if nested else kb.get(key))
            if not value:
                continue
            lc = ws.cell(r, 1, label)
            lc.font, lc.alignment = f_label, wrap
            vc = ws.cell(r, 3, value)
            vc.font, vc.alignment = f_body, wrap
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
            ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=10)
            # Excel never auto-fits merged cells, so size the row from the text length
            lines = sum(max(1, -(-len(p) // OVERVIEW_CHARS_PER_LINE)) for p in value.split("\n"))
            ws.row_dimensions[r].height = 17 * lines
            r += 1
        r += 1
        section(r, SEC_SCRIPT)
        r += 1
        for col, h in enumerate(HEADERS, 1):
            c = ws.cell(r, col, h)
            c.font, c.fill, c.alignment = f_body, yellow, wrap
        r += 1
        for i, sc in enumerate(kb.get("canh", [])):
            muc_dich = _s(sc.get("muc_dich"))
            if _s(sc.get("giay")):
                muc_dich = f"{muc_dich} ({sc['giay']})"
            values = [""] * 10
            if i == 0:
                values[0] = kb["so"]
                values[1] = f"{_s(kb.get('tom_tat'))}\n\n\n\nTitle: {_s(kb.get('title'))}"
                values[2] = _s(kb.get("dia_diem"))
            if _s(sc.get("dia_diem")):
                values[2] = sc["dia_diem"]
            values[3:] = [muc_dich, _s(sc.get("nhan_vat")), _s(sc.get("noi_dung")), _s(sc.get("bieu_cam")),
                          _s(sc.get("goc_quay")), _s(sc.get("text_noi_bat")), _s(sc.get("ghi_chu"))]
            for col, v in enumerate(values, 1):
                c = ws.cell(r, col, v if v != "" else None)
                c.font, c.alignment = f_body, wrap
            r += 1
    if not wb.worksheets:
        wb.create_sheet("Kịch bản")
    wb.save(path_out)
    print(f"Đã xuất {len(data.get('kich_ban', []))} kịch bản → {path_out}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in {"doc", "kiem", "xuat"}:
        print(__doc__)
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "doc":
        doc(sys.argv[2], sys.argv[3])
    elif cmd == "kiem":
        sys.exit(kiem(sys.argv[2]))
    else:
        xuat(sys.argv[2], sys.argv[3])
