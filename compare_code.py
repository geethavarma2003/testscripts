#!/usr/bin/env python3
import sys
from difflib import SequenceMatcher

# Paths to the developer's code and reference code
developer_file = sys.argv[1]       # e.g., geetha
reference_file = sys.argv[2]       # e.g., /tmp/chatgpt/geetha.txt

# Read files
with open(developer_file, "r") as f:
    dev_code = f.read()

with open(reference_file, "r") as f:
    ref_code = f.read()

# Calculate similarity (0-100%)
similarity = SequenceMatcher(None, dev_code.lower(), ref_code.lower()).ratio() * 100
print(f"Similarity: {similarity:.2f}%")

# Exit with 1 if similarity is high (copied), else 0
if similarity >= 70:
    print("Copied code detected!")
    sys.exit(1)
else:
    print("Code is acceptable")
    sys.exit(0)
