"""Create and repair <repo>/.cong-cu/venv, shared by kich_ban.py and phan_tich_mau.py.

The venv must survive what real machines do to it: a Homebrew upgrade removing the Python it points at, a folder copied
from another OS, a first install interrupted halfway, or a Python without ensurepip. Anything unusable is rebuilt.
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / ".cong-cu"
VENV = TOOLS / "venv"
VENV_PY = VENV / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
MIN_PYTHON = (3, 10)  # current yt-dlp needs this; macOS ships 3.9 with the Xcode command line tools
NEWER_PYTHONS = ["3.13", "3.12", "3.11", "3.10", "3.14"]  # 3.14 last: some wheels arrive later for a new Python
MAC_BIN_DIRS = ["/opt/homebrew/bin", "/usr/local/bin"]    # often missing from PATH of apps not started from a shell
HUONG_DAN_CAI = ("Cài Python 3 đầy đủ rồi chạy lại. macOS: brew install python, hoặc bộ cài ở python.org. "
                 "Linux: sudo apt install -y python3-venv. Windows: winget install -e --id Python.Python.3.12.")


def in_venv():
    return Path(sys.prefix).resolve() == VENV.resolve()


def venv_ok():
    if not VENV_PY.exists():
        return False
    return subprocess.run([str(VENV_PY), "-I", "-c", "import pip"], capture_output=True).returncode == 0


def _find_python():
    """The interpreter to build the venv from: this one if recent enough, else a newer one on the machine."""
    if sys.version_info >= MIN_PYTHON:
        return sys.executable
    for version in NEWER_PYTHONS:
        for search in (None, *MAC_BIN_DIRS):
            found = shutil.which(f"python{version}", path=search)
            if found:
                return found
    print(f"Lưu ý: Python {sys.version_info[0]}.{sys.version_info[1]} đã cũ, tải link video có thể lỗi. "
          "Nên cài Python mới hơn (macOS: brew install python).")
    return sys.executable


def _bootstrap_pip():
    """Install pip into a venv made without it (Debian / Ubuntu without python3-venv)."""
    with urllib.request.urlopen("https://pypi.org/pypi/pip/json", timeout=30) as r:
        url = next(u["url"] for u in json.load(r)["urls"] if u["packagetype"] == "bdist_wheel")
    with tempfile.TemporaryDirectory() as tmp:
        wheel = Path(tmp) / "pip.whl"
        urllib.request.urlretrieve(url, wheel)
        subprocess.run([str(VENV_PY), f"{wheel}/pip", "install", "--disable-pip-version-check", "-q", "pip"],
                       check=True, capture_output=True)


def ensure_venv():
    """Make sure the venv runs and has pip, rebuilding it when it does not. Exit with instructions if impossible."""
    if venv_ok():
        return
    TOOLS.mkdir(exist_ok=True)
    python = _find_python()
    print(f"Tạo môi trường riêng ở {VENV} ...")
    built = subprocess.run([python, "-m", "venv", "--clear", str(VENV)], capture_output=True)
    if built.returncode:   # no ensurepip: the venv itself can still be made
        built = subprocess.run([python, "-m", "venv", "--clear", "--without-pip", str(VENV)], capture_output=True)
    if built.returncode == 0 and not venv_ok():
        try:
            _bootstrap_pip()
        except Exception as e:  # network, SSL or pip failure all end in the same advice
            print(f"Không tải được pip: {e}", file=sys.stderr)
    if not venv_ok():
        sys.exit(f"LỖI: không tạo được môi trường Python ở {VENV}. {HUONG_DAN_CAI}")
    # An old pip (Xcode's Python) can miss the wheels of current packages.
    subprocess.run([str(VENV_PY), "-m", "pip", "install", "--disable-pip-version-check", "-q", "-U", "pip"],
                   capture_output=True)


def pip_install(*packages):
    r = subprocess.run([str(VENV_PY), "-m", "pip", "install", "--disable-pip-version-check", "-q", *packages])
    return r.returncode == 0
