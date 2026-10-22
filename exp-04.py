
def generate_keystream(key, length):
    """Generate a simple repeating keystream for demonstration."""
    return (key * (length // len(key) + 1))[:length]


def encrypt(plaintext, key):
    data = plaintext.encode()
    keystream = generate_keystream(key, len(data))

    ciphertext = bytes(
        b ^ k for b, k in zip(data, keystream)
    )
    return ciphertext


def decrypt(ciphertext, key):
    keystream = generate_keystream(key, len(ciphertext))

    plaintext = bytes(
        c ^ k for c, k in zip(ciphertext, keystream)
    )
    return plaintext.decode()


# Original message sent through the VPN tunnel
message = "Transfer amount is 5000"
shared_key = b"SECURE"

print("Original Message:", message)

# Sender encrypts the message
encrypted_data = encrypt(message, shared_key)
print("Captured Encrypted Data:", encrypted_data.hex())

# Authorized receiver decrypts using the shared key
decrypted_message = decrypt(encrypted_data, shared_key)
print("Decrypted with Correct Key:", decrypted_message)

# Demonstrate decryption with an incorrect key
wrong_key = b"PUBLIC"

try:
    wrong_message = decrypt(encrypted_data, wrong_key)
    print("Decrypted with Wrong Key:", repr(wrong_message))
except UnicodeDecodeError:
    print("Wrong key: Data is unreadable.")

print("\nConfidentiality demonstration completed.")
