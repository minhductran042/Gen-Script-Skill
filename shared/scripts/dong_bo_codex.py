"""Generate Codex wrappers: .agents/skills/<name>/SKILL.md points at the real skill in .claude/skills/.

Usage:
    py -I shared/scripts/dong_bo_codex.py          # write wrappers, remove wrappers of deleted skills
    py -I shared/scripts/dong_bo_codex.py --kiem   # exit 1 when wrappers are out of date

Wrappers instead of symlinks: git symlinks break on Windows without Developer Mode, and the team works on Windows.
"""
import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SRC, DST = ROOT / ".claude" / "skills", ROOT / ".agents" / "skills"

BODY = """
# {name}

File này do `shared/scripts/dong_bo_codex.py` sinh ra, không sửa tay.

Nội dung skill nằm ở `.claude/skills/{name}/SKILL.md`, dùng chung với Claude Code. Đọc toàn bộ file đó rồi làm đúng theo.
Đường dẫn trong đó tính từ thư mục gốc repo. Đầu vào là lời người dùng sau `${name}`.
"""


def wrappers():
    result = {}
    for path in sorted(SRC.glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        m = re.match(r"---\n(.*?)\n---\n", text, re.S)
        name = re.search(r"^name: (.+)$", m.group(1), re.M).group(1).strip()
        description = re.search(r"^description: (.+)$", m.group(1), re.M).group(1).strip()
        result[name] = f"---\nname: {name}\ndescription: {description}\n---\n" + BODY.format(name=name)
    return result


def main():
    want = wrappers()
    have = {p.parent.name: p.read_text(encoding="utf-8") for p in DST.glob("*/SKILL.md")}
    if "--kiem" in sys.argv:
        stale = sorted(n for n in want.keys() | have.keys() if want.get(n) != have.get(n))
        print("Lệch: " + ", ".join(stale) if stale else "Khớp.")
        return 1 if stale else 0
    for name, text in want.items():
        out = DST / name / "SKILL.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        with open(out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
    for name in have.keys() - want.keys():
        shutil.rmtree(DST / name)
    print(f"Đã ghi {len(want)} skill vào .agents/skills/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
