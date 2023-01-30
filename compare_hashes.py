#!/usr/bin/env python3


import sys
import os


def getdict(f):
    cwd = os.getcwd() + "/"
    d = {}

    with open(f) as h:
        for line in h:
            sha1 = line[:41]
            filename = line[41:].strip()
            filename = filename.removeprefix(cwd)
            if filename in d:
                print("warning: duplicated file {filename}")
            d[filename] = sha1

    return d


if __name__ == "__main__":
    f1 = sys.argv[1]
    f2 = sys.argv[2]

    d1 = getdict(f1)
    d2 = getdict(f2)

    if d1 == d2:
        print("[INFO] all checksum validated.")
    else:
        print("[WARN] corrupted backup.")
        for fn in d1.keys():
            if fn not in d2:
                print(f"[WARN] {fn} not found in second (new) hash table")
            elif d1[fn] != d2[fn]:
                print(f"[WARN] {fn} not match: {d1[fn]} vs {d2[fn]}")
        for fn in d2.keys():
            if fn not in d1:
                print(f"[WARN] {fn} not found in first (old) hash table")
