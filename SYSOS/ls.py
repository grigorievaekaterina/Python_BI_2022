#!/usr/bin/env python
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("dirname", nargs="?", default=os.getcwd())
parser.add_argument("-a", action="store_true")
args = parser.parse_args()

if args.a:
    print(".", "..", sep="\n", end="\n")
print(*os.listdir(args.dirname), sep="\n")
