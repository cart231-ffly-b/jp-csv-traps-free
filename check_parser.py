"""Run a candidate parser against every fixture. JSON stdout must be UTF-8."""
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def check(command, root=ROOT):
    folders = sorted((root / "cases").glob("[0-9][0-9]-*"))
    passed = 0
    for folder in folders:
        try:
            expected = json.loads((folder / "expected.json").read_bytes())
            result = subprocess.run(command + [(folder / "input.csv").resolve().as_posix()],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
            if result.returncode:
                detail = result.stderr.decode("utf-8", errors="replace").strip().splitlines()
                raise ValueError("exit %d: %s" % (result.returncode, detail[-1] if detail else "no stderr"))
            rows = json.loads(result.stdout.decode("utf-8"))
            if rows != expected["rows"]:
                raise ValueError("JSON rows differ from expected.json")
        except (OSError, ValueError, UnicodeError, subprocess.TimeoutExpired) as exc:
            print("FAIL %s: %s" % (folder.name, ascii(str(exc))))
        else:
            passed += 1
            print("PASS " + folder.name)
    print("%d PASS, %d FAIL (%d cases)" % (passed, len(folders) - passed, len(folders)))
    return 0 if folders and passed == len(folders) else 1


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] != "--":
        print("Usage: python check_parser.py -- <command> [args...]", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(check(sys.argv[2:]))
