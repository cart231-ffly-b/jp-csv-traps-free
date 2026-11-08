# 22: japanese-dates

Date-looking strings in several formats.

Date inference rewrites the input and depends on locale.
The serial is a literal; no date equivalence is asserted.

Fix: Preserve all five values as strings.
Encoding: `utf-8`; record endings: CRLF; delimiter: `','`.
Free sample: true. Exact parsed strings are in expected.json.
