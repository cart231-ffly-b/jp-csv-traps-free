# 01: cp932

Japanese text encoded as cp932.

UTF-8 decoding rejects these bytes.
ASCII-only samples hide this error.

Fix: Use the declared cp932 codec.
Encoding: `cp932`; record endings: CRLF; delimiter: `','`.
Free sample: true. Exact parsed strings are in expected.json.
