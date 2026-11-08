# 05: backslash-byte

Each selected cp932 character contains a 0x5C trail byte.

Byte-level backslash escaping splits multibyte characters.
The bytes are character data, not escape instructions.

Fix: Decode before operating on characters; CSV has no backslash escapes.
Encoding: `cp932`; record endings: CRLF; delimiter: `','`.
Free sample: true. Exact parsed strings are in expected.json.
