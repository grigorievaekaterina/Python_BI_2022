#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser(description='wc')
parser.add_argument('file', type=argparse.FileType(), default=sys.stdin, nargs='?')
parser.add_argument('-l', action='store_true', default=False)
parser.add_argument('-w', action='store_true', default=False)
parser.add_argument('-c', action='store_true', default=False)
args = parser.parse_args()


def wc(lines_count, words_count, bytes_count, file):
    lines = words = bytes = 0
    for line in file:
        if lines_count:
            lines += 1
        if words_count:
            words += len(line.split())
        if bytes_count:
            bytes += len(line)
    return lines, words, bytes


if not (args.l or args.w or args.c):
    args.l = args.w = args.c = True
lines, words, chars = wc(args.l, args.w, args.c, args.file)
if args.l:
    print(lines)
if args.w:
    print(words)
if args.c:
    print(chars)