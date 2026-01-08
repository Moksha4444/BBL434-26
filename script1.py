#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py seq.fa")
    sys.exit(1)

fasta_file = sys.argv[1]

sequence = ""

with open(fasta_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            continue
        sequence += line

print("Sequence length:", len(sequence))

