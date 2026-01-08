#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py input.mfa")
    sys.exit(1)

fasta_file = sys.argv[1]
count = 0

with open(fasta_file, "r") as f:
    for line in f:
        if line.startswith(">"):
            count += 1

print("Number of sequence records:", count)

