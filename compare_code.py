import sys
import re

THRESHOLD = 70  # similarity percentage


def tokenize(code):
    return re.findall(r'\w+', code.lower())


def similarity(tokens1, tokens2):
    set1, set2 = set(tokens1), set(tokens2)
    if not set1 or not set2:
        return 0
    return (len(set1 & set2) / len(set1 | set2)) * 100


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if len(sys.argv) < 3:
    print("Usage: python compare_code.py <repo_file> <ref_file1> [ref_file2] ...")
    sys.exit(1)

repo_file = sys.argv[1]
reference_files = sys.argv[2:]

repo_code = read_file(repo_file)
repo_tokens = tokenize(repo_code)

failed = False

for ref in reference_files:
    ref_code = read_file(ref)
    ref_tokens = tokenize(ref_code)

    score = similarity(repo_tokens, ref_tokens)
    print(f"Similarity with {ref}: {score:.2f}%")

    if score >= THRESHOLD:
        print("❌ Code is too similar (>= 70%)")
        failed = True

if failed:
    sys.exit(1)
else:
    print("✅ Code is acceptable miss Geetha Varma")
    sys.exit(0)

