import sys

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def similarity(a, b):
    a_tokens = set(a.split())
    b_tokens = set(b.split())

    if not a_tokens or not b_tokens:
        return 0.0

    return (len(a_tokens & b_tokens) / len(a_tokens | b_tokens)) * 100


if len(sys.argv) != 3:
    print("Usage: python compare_code.py <repo_file> <s3_file>")
    sys.exit(1)

repo_file = sys.argv[1]
s3_file = sys.argv[2]

code1 = read_file(repo_file)
code2 = read_file(s3_file)

score = similarity(code1, code2)

print(f"Token-based similarity: {score:.2f}%")

if score >= 70:
    print("❌ Code is too similar (>= 70%)")
    sys.exit(1)   # FAIL CodeBuild
else:
    print("✅ Code is acceptable (< 70%)")
    sys.exit(0)

