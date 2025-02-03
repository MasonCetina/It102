"""
We are going to create a AES encryption and decryption tool
"""


# Are the nec modules and libraries we need to run our code
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Create he aes key to encrypt our data

def generate_key():
    #This is pulling a 128 bit key!
    return os.urandom(16)

def encrypt(plaintext: str, key: bytes) -> str:
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext.encode()) + padder.finalize()
    ciphertext = cipher.update(padded_data) + cipher.finalize()
    return base64.b64encode(iv + ciphertext).decode()


def decrypt(encrypted_text: str, key: bytes) -> str:
    encrypted_data = base64.b64decode(encrypted_text)
    iv, ciphertext = encrypted_data[:16], encrypted_data[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend()).decryptor()
    padded_plaintext = cipher.update(ciphertext) + cipher.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return (unpadder.update(padded_plaintext) + unpadder.finalize()).decode()


key = generate_key()
print(f"Generated AES Key: {key}")
plaintext = input("enter a plaintext message: ")
encrypted_message = encrypt(plaintext, key)
print(f"encrypted message {encrypted_message}")
decrypted_message = decrypt(encrypted_message, key)
print(f"Decrypyted message: {decrypted_message}")
