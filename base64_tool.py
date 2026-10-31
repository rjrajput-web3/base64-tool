#!/usr/bin/env python3
"""base64-tool: encode and decode text with base64 from the terminal.

Usage:
    python base64_tool.py encode "hello world"      -> aGVsbG8gd29ybGQ=
    python base64_tool.py decode aGVsbG8gd29ybGQ=    -> hello world
    echo hello | python base64_tool.py encode        -> aGVsbG8K

Reads from stdin when no text argument is given.
"""

import base64
import sys


def encode(text: str) -> str:
    return base64.b64encode(text.encode("utf-8")).decode("ascii")


def decode(text: str) -> str:
    text = text.strip()
    # add missing padding so copied strings without "=" still decode
    text += "=" * (-len(text) % 4)
    return base64.b64decode(text.encode("ascii")).decode("utf-8")


def main(argv):
    if len(argv) < 2 or argv[1] not in ("encode", "decode"):
        print(__doc__.strip())
        return 2
    text = argv[2] if len(argv) > 2 else sys.stdin.read()
    try:
        print(encode(text) if argv[1] == "encode" else decode(text))
    except Exception as exc:  # bad input, not a secret: print plainly
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))





















