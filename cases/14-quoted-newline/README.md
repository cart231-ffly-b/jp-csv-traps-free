# 14: quoted-newline

A quoted address contains an embedded CRLF.

Line splitting creates a false extra record.
Universal newline translation changes the field's exact string.

Fix: Open text with newline='' and use a CSV reader.
Encoding: `utf-8`; record endings: CRLF; delimiter: `','`.
Free sample: true. Exact parsed strings are in expected.json.
