import boto3
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read GitHub file (ONLY file)
with open("geetha", "r") as f:
    github_text = f.read()

# Read S3 file
s3 = boto3.client("s3")
obj = s3.get_object(
    Bucket="testscripts-geetha",   # <-- change bucket name
    Key="getha.txt"                    # <-- S3 file name
)
s3_text = obj["Body"].read().decode("utf-8")

# Compare similarity
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform([github_text, s3_text])

similarity = cosine_similarity(vectors[0], vectors[1])[0][0] * 100

print(f"Similarity: {similarity:.2f}%")

if similarity >= 70:
    print("STOP ❌")
    sys.exit(1)
else:
    print("CONTINUE ✅")
    sys.exit(0)
