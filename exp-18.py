
import hashlib
import os

# Database of known malicious SHA-256 hashes
malware_database = {
    "5d41402abc4b2a76b9719d911017c592"
    "7e562e4f",
    "e3b0c44298fc1c149afbf4c8996fb924"
    "27ae41e4649b934ca495991b7852b855"
}

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        for data in iter(lambda: file.read(4096), b""):
            sha256.update(data)

    return sha256.hexdigest()


filename = input("Enter file path: ")

if not os.path.isfile(filename):
    print("File not found!")

else:
    file_hash = calculate_hash(filename)

    print("\nSHA-256 Hash:", file_hash)

    if file_hash in malware_database:
        print("WARNING: Malicious file detected!")
    else:
        print("File not found in malware database.")
        print("No known-malicious hash match.")
