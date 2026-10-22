"""Reference-video tool: download, cut into labelled frame grids, measure editing rhythm, transcribe speech.

Usage:
    py -I phan_tich_mau.py cai                          # first-time setup (also runs automatically)
    py -I phan_tich_mau.py kiem-cai                     # report what is installed, exit 1 if not ready
    py -I phan_tich_mau.py chay <link|file.mp4> <dir>   # tai (link only) + tach + chep
    py -I phan_tich_mau.py tai  <link> <dir>            # video.mp4, meta.json, binh-luan.json, subtitles
    py -I phan_tich_mau.py tach <file.mp4> <dir>        # khung/, luoi-NN.jpg, canh.json, am-thanh.wav
    py -I phan_tich_mau.py chep <dir>                   # loi.json, loi.txt (speech-to-text with timestamps)

Options: --nguong <0..1> scene-cut threshold for tach/chay (default 0.3)
         --model <tiny|base|small|medium> whisper model for chep/chay (default small)
         --khong-chep skip transcription in chay

Tools live in <repo>/.cong-cu/ (git-ignored): a venv with yt-dlp, imageio-ffmpeg (bundled ffmpeg binary),
faster-whisper and Pillow, plus downloaded whisper models. Any command other than cai/kiem-cai installs them
on first use, then re-runs itself inside that venv, so the caller never has to set anything up.
Skill: .claude/skills/vid-phan-tich-mau/SKILL.md.
"""
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / ".cong-cu"
VENV = TOOLS / "venv"
VENV_PY = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
MODELS = TOOLS / "whisper-models"
MARKER = TOOLS / "da-cai.json"
PACKAGES = ["yt-dlp", "imageio-ffmpeg", "faster-whisper", "Pillow"]
MODULES = {"yt-dlp": "yt_dlp", "imageio-ffmpeg": "imageio_ffmpeg", "faster-whisper": "faster_whisper",
           "Pillow": "PIL"}

HOOK_END = 3.0        # seconds sampled densely: the hook decides whether people stop scrolling
HOOK_STEP = 0.5
MAX_GAP = 2.0         # a long shot still gets a frame at least every MAX_GAP seconds
LINE_GAP = 0.6        # a pause this long between words starts a new transcript line
NO_SPEECH_MIN = 0.8   # pauses this long between lines are reported as khong_thoai
MAX_FRAMES = 60
GRID_COLS, GRID_ROWS, THUMB_W = 4, 3, 360


def _die(msg, code=1):
    print(f"LỖI: {msg}", file=sys.stderr)
    sys.exit(code)


def _in_venv():
    return Path(sys.prefix).resolve() == VENV.resolve()


# ---------------------------------------------------------------- cai (setup)

def _venv_status():
    """Return {package: version or None} as seen by the venv interpreter."""
    if not VENV_PY.exists():
        return {p: None for p in PACKAGES}
    code = ("import importlib.metadata as m, json\n"
            f"out = {{}}\nfor p in {PACKAGES!r}:\n"
            "    try: out[p] = m.version(p)\n    except Exception: out[p] = None\n"
            "print(json.dumps(out))")
    r = subprocess.run([str(VENV_PY), "-I", "-c", code], capture_output=True, text=True)
    try:
        return json.loads(r.stdout)
    except ValueError:
        return {p: None for p in PACKAGES}


def cai():
    TOOLS.mkdir(exist_ok=True)
    if not VENV_PY.exists():
        print(f"Tạo môi trường riêng ở {VENV} ...")
        subprocess.run([sys.executable, "-m", "venv", str(VENV)], check=True)
    missing = [p for p, v in _venv_status().items() if v is None]
    if missing:
        print(f"Cài {', '.join(missing)} (lần đầu mất vài phút) ...")
        r = subprocess.run([str(VENV_PY), "-m", "pip", "install", "--disable-pip-version-check", "-q", *PACKAGES])
        if r.returncode:
            _die("pip install thất bại. Xem lỗi ở trên; nếu báo thiếu bản dựng cho phiên bản Python này thì cài "
                 "Python 3.12 rồi xoá thư mục .cong-cu và chạy lại.")
    status = _venv_status()
    not_ok = [p for p, v in status.items() if v is None]
    if not_ok:
        _die(f"vẫn thiếu: {', '.join(not_ok)}")
    MARKER.write_text(json.dumps({"python": sys.version.split()[0], "goi": status}, ensure_ascii=False, indent=2),
                      encoding="utf-8")
    print("Sẵn sàng: " + ", ".join(f"{p} {v}" for p, v in status.items()))
    print("Mô hình chép lời tải về lần đầu khi chạy 'chep' (small khoảng 480 MB).")


def kiem_cai():
    status = _venv_status()
    for p, v in status.items():
        print(f"{p:16} {v or 'CHƯA CÓ'}")
    for name in ("small", "base"):
        snap = list(MODELS.glob(f"models--Systran--faster-whisper-{name}/snapshots/*/model.bin"))
        state = "đã tải" if snap else "CHƯA TẢI (tự tải khi chép lời; small ~480 MB, có thể 10–15 phút)"
        print(f"{'whisper ' + name:16} {state}")
    sys.exit(0 if all(status.values()) else 1)


def _ensure_venv_and_reexec(argv):
    if _in_venv():
        return
    if not all(_venv_status().values()):
        print("Lần đầu dùng: tự cài công cụ phân tích video.")
        cai()
    r = subprocess.run([str(VENV_PY), "-I", str(Path(__file__).resolve()), *argv])
    sys.exit(r.returncode)


# ---------------------------------------------------------------- helpers (run inside venv)

def _ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def _ff(args):
    """Run ffmpeg, return stderr text (ffmpeg logs everything there)."""
    r = subprocess.run([_ffmpeg(), "-hide_banner", *args], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return r.returncode, r.stderr


def _probe(video):
    _, err = _ff(["-i", str(video)])
    m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", err)
    if not m:
        _die(f"không đọc được thời lượng của {video}")
    dur = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))
    size = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", err)
    w, h = (int(size.group(1)), int(size.group(2))) if size else (0, 0)
    rot = re.search(r"rotate\s*:\s*(-?\d+)|rotation of (-?[\d.]+)", err)
    if rot and abs(int(float(rot.group(1) or rot.group(2)))) in (90, 270):
        w, h = h, w
    return dur, w, h, "Audio:" in err


# ---------------------------------------------------------------- tai (download)

def tai(url, out):
    import yt_dlp
    out.mkdir(parents=True, exist_ok=True)
    base = {"outtmpl": str(out / "video.%(ext)s"), "quiet": True, "no_warnings": True, "noplaylist": True,
            "noprogress": True,
            "ffmpeg_location": _ffmpeg(), "merge_output_format": "mp4",
            "format": "b[height<=720][ext=mp4]/bv*[height<=720]+ba/b",
            "writesubtitles": True, "writeautomaticsub": True, "subtitleslangs": ["vi", "en"],
            "subtitlesformat": "vtt"}
    with_comments = dict(base, getcomments=True,
                         # max_comments = total, parents, replies, replies per thread: top-level threads only
                         extractor_args={"youtube": {"max_comments": ["60", "60", "0", "0"],
                                                     "comment_sort": ["top"]}})
    info = None
    for opts in (with_comments, base):
        try:
            with yt_dlp.YoutubeDL(opts) as ydl:
                info = ydl.extract_info(url, download=True)
            break
        except Exception as e:  # comments often fail (rate limit, login wall); retry without them
            last = e
    if info is None:
        _die(f"tải không được: {last}. Thử tải tay file .mp4 rồi chạy 'chay <file.mp4> <thư mục>'.")
    videos = sorted(out.glob("video.*"), key=lambda p: p.stat().st_size, reverse=True)
    videos = [p for p in videos if p.suffix.lower() in (".mp4", ".webm", ".mkv", ".mov")]
    if not videos:
        _die("tải xong nhưng không thấy file video")
    meta = {k: info.get(k) for k in ("title", "uploader", "channel", "webpage_url", "duration", "view_count",
                                      "like_count", "comment_count", "repost_count", "upload_date",
                                      "description", "tags", "track", "artist")}
    meta["nguon"] = url
    meta["file"] = videos[0].name
    fetched = info.get("comments") or []
    if fetched and meta.get("comment_count") == len(fetched):
        # yt-dlp overwrites comment_count with the number it downloaded, not the real total
        meta["comment_count"] = None
        meta["ghi_chu_comment_count"] = "không rõ tổng số bình luận; chỉ biết đã tải được " + str(len(fetched))
    (out / "meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    # Top-level comments only (replies have parent != "root"), most liked first
    top = [c for c in fetched if c.get("parent", "root") == "root"]
    comments = sorted(top, key=lambda c: c.get("like_count") or 0, reverse=True)[:40]
    (out / "binh-luan.json").write_text(json.dumps(
        [{"like": c.get("like_count"), "text": c.get("text")} for c in comments], ensure_ascii=False, indent=2),
        encoding="utf-8")
    subs = sorted(p.name for p in out.glob("video*.vtt"))
    print(f"Tải xong: {videos[0].name} · {meta.get('duration')}s · view {meta.get('view_count')} · "
          f"like {meta.get('like_count')} · bình luận lấy được {len(comments)} · phụ đề {subs or 'không có'}")
    return videos[0]


# ---------------------------------------------------------------- tach (frames, cuts, silence, audio)

def _cuts(video, threshold):
    _, err = _ff(["-i", str(video), "-an", "-vf", f"select='gt(scene,{threshold})',showinfo", "-f", "null", "-"])
    return [round(float(t), 2) for t in re.findall(r"pts_time:([\d.]+)", err)]


def _silences(video):
    _, err = _ff(["-i", str(video), "-vn", "-af", "silencedetect=n=-35dB:d=0.4", "-f", "null", "-"])
    starts = [float(x) for x in re.findall(r"silence_start:\s*([\d.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end:\s*([\d.]+)", err)]
    return [[round(s, 2), round(e, 2)] for s, e in zip(starts, ends)]


def _frame_times(dur, cuts):
    times = {round(t, 2): "hook" for t in [i * HOOK_STEP for i in range(int(HOOK_END / HOOK_STEP) + 1)] if t < dur}
    for c in cuts:
        t = round(min(c + 0.3, dur - 0.05), 2)   # just after the cut, past any transition blur
        times[t] = "cut"
    marks = sorted(set([0.0, *cuts, dur]))
    for a, b in zip(marks, marks[1:]):          # fill long shots
        t = a + MAX_GAP
        while t < b - 0.5:
            times.setdefault(round(t, 2), "giua")
            t += MAX_GAP
    times.setdefault(round(max(dur - 0.2, 0), 2), "cuoi")
    picked = []
    for t in sorted(times):                      # drop near-duplicates, cut frames win
        if picked and t - picked[-1][0] < 0.25:
            if times[t] == "cut":
                picked[-1] = (t, "cut")
            continue
        picked.append((t, times[t]))
    if len(picked) > MAX_FRAMES:                 # keep hook + cuts, thin the fillers
        keep = [p for p in picked if p[1] != "giua"]
        fill = [p for p in picked if p[1] == "giua"]
        room = max(MAX_FRAMES - len(keep), 0)
        step = max(len(fill) // room, 1) if room else len(fill) + 1
        picked = sorted(keep + fill[::step][:room])[:MAX_FRAMES]
    return picked


def _grids(frames, out):
    from PIL import Image, ImageDraw, ImageFont
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    per = GRID_COLS * GRID_ROWS
    paths = []
    for g in range(0, len(frames), per):
        chunk = frames[g:g + per]
        thumbs = [Image.open(f["file_abs"]).convert("RGB") for f in chunk]
        th = max(t.height for t in thumbs)
        rows = (len(chunk) + GRID_COLS - 1) // GRID_COLS
        sheet = Image.new("RGB", (GRID_COLS * THUMB_W, rows * th), "black")
        draw = ImageDraw.Draw(sheet)
        for i, (f, im) in enumerate(zip(chunk, thumbs)):
            x, y = (i % GRID_COLS) * THUMB_W, (i // GRID_COLS) * th
            sheet.paste(im, (x, y))
            label = f"{f['t']:.1f}s" + (" CUT" if f["loai"] == "cut" else "")
            box = draw.textbbox((x + 6, y + 6), label, font=font)
            draw.rectangle((box[0] - 4, box[1] - 3, box[2] + 4, box[3] + 3),
                           fill="#d00000" if f["loai"] == "cut" else "black")
            draw.text((x + 6, y + 6), label, fill="white", font=font)
        p = out / f"luoi-{g // per + 1:02d}.jpg"
        sheet.save(p, quality=85)
        paths.append(p.name)
    return paths


def tach(video, out, threshold=0.3):
    video = Path(video)
    if not video.exists():
        _die(f"không thấy file {video}")
    out.mkdir(parents=True, exist_ok=True)
    frame_dir = out / "khung"
    if frame_dir.exists():
        shutil.rmtree(frame_dir)
    frame_dir.mkdir()
    dur, w, h, has_audio = _probe(video)
    cuts = [c for c in _cuts(video, threshold) if 0.1 < c < dur - 0.1]
    frames = []
    for t, kind in _frame_times(dur, cuts):
        f = frame_dir / f"{t:07.2f}s.jpg"
        _ff(["-ss", f"{t:.2f}", "-i", str(video), "-frames:v", "1", "-vf", f"scale={THUMB_W}:-2", "-q:v", "3",
             "-y", str(f)])
        if f.exists():
            frames.append({"t": t, "loai": kind, "file": f"khung/{f.name}", "file_abs": str(f)})
    grids = _grids(frames, out)
    bounds = [0.0, *cuts, dur]
    shots = [round(b - a, 2) for a, b in zip(bounds, bounds[1:])]
    silences = _silences(video) if has_audio else []
    if has_audio:
        _ff(["-i", str(video), "-vn", "-ac", "1", "-ar", "16000", "-y", str(out / "am-thanh.wav")])
    info = {
        "video": str(video), "thoi_luong": round(dur, 2), "khung_hinh": f"{w}x{h}",
        "doc": h > w, "co_am_thanh": has_audio, "nguong_cat": threshold,
        "so_cut": len(cuts), "so_shot": len(shots), "cut_luc": cuts,
        "shot_trung_binh": round(dur / len(shots), 2), "shot_dai_nhat": max(shots), "shot_ngan_nhat": min(shots),
        "cut_trong_3s_dau": sum(1 for c in cuts if c <= HOOK_END),
        "im_lang": silences, "luoi": grids,
        "khung": [{k: f[k] for k in ("t", "loai", "file")} for f in frames],
    }
    (out / "canh.json").write_text(json.dumps(info, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Tách xong: {dur:.1f}s · {w}x{h} · {len(cuts)} cut · shot TB {info['shot_trung_binh']}s · "
          f"{len(frames)} khung → {len(grids)} lưới · im lặng {len(silences)} đoạn")


# ---------------------------------------------------------------- chep (transcribe)

def chep(out, model="small"):
    wav = out / "am-thanh.wav"
    if not wav.exists():
        (out / "loi.json").write_text(json.dumps({"ghi_chu": "video không có âm thanh", "doan": []},
                                                 ensure_ascii=False, indent=2), encoding="utf-8")
        print("Không có âm thanh, bỏ qua chép lời.")
        return
    import wave

    import numpy as np
    os.environ.setdefault("HF_HUB_DISABLE_SYMLINKS_WARNING", "1")
    os.environ.setdefault("HF_HUB_DISABLE_IMPLICIT_TOKEN", "1")
    from faster_whisper import WhisperModel
    MODELS.mkdir(parents=True, exist_ok=True)
    # Decode the 16 kHz mono wav ourselves: faster-whisper's own decoder breaks on newer PyAV releases.
    with wave.open(str(wav)) as w:
        audio = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768.0
    print(f"Chép lời bằng whisper '{model}' (lần đầu tải mô hình) ...")
    m = WhisperModel(model, device="cpu", compute_type="int8", download_root=str(MODELS))
    segs, info = m.transcribe(audio, vad_filter=True, beam_size=5, word_timestamps=True)
    # Whisper segments can span 8+ seconds; re-split on pauses and sentence ends for usable timestamps.
    doan = []
    for s in segs:
        cur = []
        for w in s.words or []:
            if cur and (w.start - cur[-1].end >= LINE_GAP or cur[-1].word.strip()[-1:] in ".?!…"):
                doan.append(cur)
                cur = []
            cur.append(w)
        if cur:
            doan.append(cur)
    doan = [{"bat_dau": round(ws[0].start, 2), "ket_thuc": round(ws[-1].end, 2),
             "loi": "".join(w.word for w in ws).strip(),
             "xac_suat_tu_thap_nhat": round(min(float(w.probability) for w in ws), 2)} for ws in doan]
    gaps = [[a["ket_thuc"], b["bat_dau"]] for a, b in zip(doan, doan[1:])
            if b["bat_dau"] - a["ket_thuc"] >= NO_SPEECH_MIN]
    data = {"ngon_ngu": info.language, "xac_suat_ngon_ngu": round(info.language_probability, 2),
            "model": model, "doan": doan, "khong_thoai": gaps,
            "ghi_chu": "khong_thoai = quãng không có lời nói (vẫn có thể có nhạc / tiếng nền); "
                       "tắt tiếng thật nằm ở im_lang trong canh.json"}
    (out / "loi.json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [f"[{d['bat_dau']:.1f}–{d['ket_thuc']:.1f}s] {d['loi']}"
             + (" (nghe không chắc)" if d["xac_suat_tu_thap_nhat"] < 0.4 else "") for d in doan]
    (out / "loi.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Chép xong: {len(doan)} đoạn lời · ngôn ngữ {info.language} ({info.language_probability:.0%})")


# ---------------------------------------------------------------- main

def _opt(args, name, default):
    if name in args:
        i = args.index(name)
        val = args[i + 1]
        del args[i:i + 2]
        return val
    return default


def main():
    argv = sys.argv[1:]
    if not argv:
        print(__doc__)
        sys.exit(2)
    cmd = argv[0]
    if cmd == "cai":
        return cai()
    if cmd == "kiem-cai":
        return kiem_cai()
    _ensure_venv_and_reexec(argv)

    args = argv[1:]
    threshold = float(_opt(args, "--nguong", "0.3"))
    model = _opt(args, "--model", "small")
    skip_chep = "--khong-chep" in args
    args = [a for a in args if a != "--khong-chep"]
    if cmd == "tai" and len(args) == 2:
        tai(args[0], Path(args[1]))
    elif cmd == "tach" and len(args) == 2:
        tach(args[0], Path(args[1]), threshold)
    elif cmd == "chep" and len(args) == 1:
        chep(Path(args[0]), model)
    elif cmd == "chay" and len(args) == 2:
        src, out = args[0], Path(args[1])
        if re.match(r"https?://", src):
            video = tai(src, out)
        else:
            out.mkdir(parents=True, exist_ok=True)
            video = Path(src)
            (out / "meta.json").write_text(json.dumps({"nguon": str(video.resolve()), "file": video.name},
                                                      ensure_ascii=False, indent=2), encoding="utf-8")
        tach(video, out, threshold)
        if not skip_chep:
            chep(out, model)
        names = ["canh.json", "luoi-*.jpg", "loi.txt", "meta.json", "binh-luan.json", "video*.vtt"]
        found = [n for n in names if list(out.glob(n))]
        print(f"Đọc tiếp trong {out}: {', '.join(found)}")
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
