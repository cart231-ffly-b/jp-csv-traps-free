"""Check declared decode + CSV parse against independently declared rows."""
import csv
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def verify(root=ROOT):
    folders = sorted((root / "cases").glob("[0-9][0-9]-*"))
    passed = 0
    for folder in folders:
        try:
            expected = json.loads((folder / "expected.json").read_bytes())
            text = (folder / "input.csv").read_bytes().decode(expected["encoding"])
            rows = list(csv.reader(io.StringIO(text, newline=""),
                                   delimiter=expected.get("delimiter", ","), strict=True))
            if rows != expected["rows"]:
                raise ValueError("parsed rows differ from expected.json")
        except (OSError, ValueError, UnicodeError, csv.Error, KeyError) as exc:
            print("FAIL %s: %s" % (folder.name, ascii(str(exc))))
        else:
            passed += 1
            print("OK " + folder.name)
    print("%d/%d OK" % (passed, len(folders)))
    return 0 if folders and passed == len(folders) else 1


if __name__ == "__main__":
    raise SystemExit(verify())
