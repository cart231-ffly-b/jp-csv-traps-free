# Japanese CSV traps (free samples)

Five small CSV files that break naive Japanese CSV importers, each with the exact rows a correct importer must return.

Run your importer against them in one command:

```text
python check_parser.py -- python your_parser.py
```

Your command gets the CSV path as its last argument and must print a UTF-8 JSON array of rows (header included, every value a string) to stdout.

Two example parsers are included:

```text
python check_parser.py -- python naive_parser.py       # 0 PASS, 5 FAIL
python check_parser.py -- python reference_parser.py   # 5 PASS, 0 FAIL
```

`python verify.py` checks that every `input.csv` decodes and parses to its `expected.json`. Python 3, standard library only, no network.

## The five traps

| Case | Trap |
| --- | --- |
| 01-cp932 | Japanese text saved as cp932 (Shift_JIS as written by Windows and Excel), not UTF-8 |
| 05-backslash-byte | 表, ソ, 能, 予 in cp932 have `0x5C` (backslash) as the second byte, which breaks byte-level escaping |
| 09-halfwidth-katakana | Half-width katakana such as ﾃｽﾄ in cp932 |
| 14-quoted-newline | A quoted address field that contains a line break |
| 22-japanese-dates | 令和8年1月2日, R8.1.2, 2026/1/2 and an Excel serial number that must stay as strings |

Each case folder has `input.csv`, `expected.json` (encoding, rows, trap and why it breaks) and a short `README.md`.

## Full pack

The full pack has 30 cases. It adds cp932 extension characters, BOMs, UTF-16 tab files, wave dash collapse, characters outside cp932, mixed and lone-CR newlines, leading zeros, 19-digit IDs, full-width digits, formula-looking cells, duplicate headers and more. It also includes the generator that rebuilds every file byte for byte.

All data is fictional.

## License

MIT
