import base64
import hashlib


# Encode using SHA-512 and base64
def encode(input_string):
    # Hash the input string using SHA-512
    hash_object = hashlib.sha512(input_string.encode("ascii"))
    hash_bytes = hash_object.digest()

    # Encode the hash in base64
    base64_bytes = base64.b64encode(hash_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


# "Decode" by verifying if a given input matches the original encoded hash
def decode(input_string, encoded_string):
    # Hash the input string again using SHA-512
    hash_object = hashlib.sha512(input_string.encode("ascii"))
    hash_bytes = hash_object.digest()

    # Encode the hash in base64
    base64_bytes = base64.b64encode(hash_bytes)
    base64_string = base64_bytes.decode("ascii")

    # Compare the new base64 string with the original encoded string
    return base64_string == encoded_string
