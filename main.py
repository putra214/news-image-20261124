#!/usr/bin/env python3
"""Copy entry.png to the output directory (deterministic, stdlib only)."""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def sha256(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    os.makedirs(OUT, exist_ok=True)
    dst = os.path.join(OUT, "entry.png")
    shutil.copyfile(SRC, dst)
    src_hash, dst_hash = sha256(SRC), sha256(dst)
    if src_hash != dst_hash:
        print("error: copy mismatch", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)"
          % (dst, os.path.getsize(dst), dst_hash))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
