# 09: halfwidth-katakana

Half-width katakana and an ASCII space in cp932.

UTF-8 decoding rejects the bytes.
Automatic width normalization changes the answer.

Fix: Decode cp932 and preserve character widths and spaces.
Encoding: `cp932`; record endings: CRLF; delimiter: `','`.
Free sample: true. Exact parsed strings are in expected.json.
