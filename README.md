# base64-tool

A tiny terminal tool to encode and decode text with base64. No dependencies, one file, works from arguments or a pipe.

## What it does

- `encode` — turns text into a base64 string
- `decode` — turns a base64 string back into text (auto-fixes missing `=` padding)

## How to run

Needs Python 3 only.

```bash
python base64_tool.py encode "hello world"
python base64_tool.py decode aGVsbG8gd29ybGQ=
echo "pipe me" | python base64_tool.py encode
```

## Example output

```
$ python base64_tool.py encode "hello world"
aGVsbG8gd29ybGQ=

$ python base64_tool.py decode aGVsbG8gd29ybGQ
hello world

$ echo "pipe me" | python base64_tool.py encode
cGlwZSBtZQo=

$ python base64_tool.py decode cGlwZSBtZQo
pipe me
```

## Notes

- Invalid input prints `error: ...` and exits with code 1.
- No flags prints the built-in usage help and exits with code 2.
