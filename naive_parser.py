"""Deliberately wrong: UTF-8 only, literal LF and comma splitting."""
import json
from pathlib import Path
import sys

text = Path(sys.argv[1]).read_bytes().decode("utf-8")
if text.endswith("\n"):
    text = text[:-1]
rows = [line.split(",") for line in text.split("\n")]
sys.stdout.buffer.write((json.dumps(rows, ensure_ascii=True) + "\n").encode("utf-8"))
