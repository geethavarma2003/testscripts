import sys
def read_file(path):
    with open(path, "r") as f:
        return f.read()
def similarity(a, b):
    a_tokens = set(a.split())
    b_tokens = set(b.split())
    return (len(a_tokens & b_tokens) / len(a_tokens | b_tokens)) * 100
if len(sys.argv) != 3:
    print("Usage: python compare_code.py <file1> <file2>")
    sys.exit(1)
file1 = sys.argv[1]
file2 = sys.argv[2]
code1 = read_file(file1)
code2 = read_file(file2)
score = similarity(code1, code2)
print(f"Token-based similarity: {score:.2f}%")
if score >= 80:
    print("❌ Code is too similar")
    sys.exit(1)
else:
    print("✅ Code is acceptable")
