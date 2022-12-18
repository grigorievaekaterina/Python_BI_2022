#!/usr/bin/env python
import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("-r", action="store_true")
args = parser.parse_args()

if not os.path.exists(args.name):
    raise ValueError("Non-existent path provided")


def empty_directory(dirname: str):
    try:
        os.rmdir(dirname)
    except OSError:
        content = os.walk(dirname)
        for dir, _, files in content:
            if files:
                list(map(os.remove, (Path(dir) / file for file in files)))
            if dir != dirname:
                empty_directory(dir)


if args.r and os.path.isdir(args.name):
    empty_directory(args.name)
    os.rmdir(args.name)
elif not args.r and os.path.isfile(args.name):
    os.remove(args.name)
else:
    raise ValueError(
        "Provide sufficent options: use -r flag for directory and no flag for file"
    )
