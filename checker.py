import hashlib
import json
import os

def calculate_hash(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

filename = "test.txt"
hash_file = "baseline.json"

if not os.path.exists(hash_file):
    original_hash = calculate_hash(filename)
    with open(hash_file, "w") as file:
        json.dump({filename: original_hash}, file, indent=4)
    print("Baseline saved!")
else:
    with open(hash_file, "r") as file:
        saved_hashes = json.load(file)

    current_hash = calculate_hash(filename)
    if saved_hashes.get(filename) == current_hash:
        print("File is unchanged.")
    else:
        print("WARNING: File has changed!")
