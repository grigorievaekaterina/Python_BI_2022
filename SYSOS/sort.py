#!/usr/bin/env python
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("files", nargs="+")
args = parser.parse_args()

if any(os.path.isdir(file) for file in args.files):
    raise ValueError("Directory found in list of files")

lines = []
for file in args.files:
    with open(file) as f:
        lines.extend(map(str.strip, f.readlines()))

print(*sorted(lines, key=str.lower), sep="\n")
