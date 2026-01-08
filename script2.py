#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
    print("Usage: python script.py seq.fa")
    sys.exit(1)

fasta_file = sys.argv[1]

sequence = ""

# Read FASTA (single record)
with open(fasta_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith(">"):
            continue
        sequence += line

k = 3

if len(sequence) < k:
    print("Sequence is shorter than k =", k)
    sys.exit(1)

# Generate k-mers
kmers = set()
for i in range(len(sequence) - k + 1):
    kmer = sequence[i:i+k]
    kmers.add(kmer)

print("Unique 3-mer count:", len(kmers))

