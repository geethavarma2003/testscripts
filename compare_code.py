#!/usr/bin/env python3
import sys
import tokenize
from difflib import SequenceMatcher

def extract_tokens(file_path):
    tokens = []
    with open(file_path, "rb") as f:
        for tok in tokenize.tokenize(f.readline):
            # Ignore comments, newlines, indentation
            if tok.type in (
                tokenize.NAME,      # variables, function names
                tokenize.OP,        # + - * / = == etc
                tokenize.NUMBER,    # numbers
                tokenize.STRING,    # strings
                tokenize.KEYWORD if hasattr(tokenize, "KEYWORD") else tokenize.NAME
            ):
                tokens.append(tok.string)
    return tokens

# Arguments
developer_file = sys.argv[1]     # developer code
reference_file = sys.argv[2]     # reference code from S3

dev_tokens = extract_tokens(developer_file)
ref_tokens = extract_tokens(reference_file)

# Token similarity
similarity = SequenceMatcher(None, dev_tokens, ref_tokens).ratio() * 100

print(f"Token-based similarity: {similarity:.2f}%")

# Decision
if similarity >= 70:
    print("❌ Copied logic detected")
    sys.exit(1)
else:
    print("✅ Code is acceptable")
    sys.exit(0)
