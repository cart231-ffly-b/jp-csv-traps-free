"""A correct reference: decode with the declared encoding, parse with csv.reader(newline='')."""
import csv
import io
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
meta = json.loads((path.parent / "expected.json").read_bytes())
text = path.read_bytes().decode(meta["encoding"])
rows = list(csv.reader(io.StringIO(text, newline=""), delimiter=meta.get("delimiter", ",")))
sys.stdout.buffer.write(json.dumps(rows, ensure_ascii=False).encode("utf-8"))
