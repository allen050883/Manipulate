from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode
import os
import argparse

# 將字串鹽轉換為固定長度的字節鹽
def get_fixed_length_salt(salt_str, length=16):
    salt = salt_str.encode()  # 將字串轉換為字節
    if len(salt) < length:
        salt = salt.ljust(length, b'\0')  # 如果鹽長度不足，右側填充0字節
    elif len(salt) > length:
        salt = salt[:length]  # 如果鹽長度超過，截斷
    return salt

# 加密函數
def encrypt(password, salt, salt_str):
    # 使用PBKDF2HMAC算法生成密鑰
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(salt_str.encode())

    # 使用固定IV
    iv = get_fixed_length_salt("example", length=16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # 使用PKCS7填充數據
    padder = PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(password.encode()) + padder.finalize()

    # 加密數據
    encrypted_passwd = encryptor.update(padded_data) + encryptor.finalize()

    # 返回加密數據、鹽和IV的組合
    return urlsafe_b64encode(iv + encrypted_passwd).decode()

# 解密函數
def decrypt(encrypted_passwd, salt, salt_str):
    # 解碼並提取IV和加密數據
    decoded_data = urlsafe_b64decode(encrypted_passwd)
    iv = decoded_data[:16]
    encrypted_passwd = decoded_data[16:]

    # 使用PBKDF2HMAC算法生成密鑰
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(salt_str.encode())

    # 解密數據
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_passwd) + decryptor.finalize()

    # 去除PKCS7填充
    unpadder = PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_passwd = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    return decrypted_passwd.decode()

# 主程序
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Encrypt or decrypt a password using AES.')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform: encrypt or decrypt')
    parser.add_argument('--passwd', help='Password to encrypt or encrypted password to decrypt')
    parser.add_argument('--salt', help='Salt for key derivation')

    args = parser.parse_args()

    if args.action == 'encrypt':
        password = args.passwd
        salt_str = args.salt
        salt = get_fixed_length_salt(salt_str)

        encrypted_passwd = encrypt(password, salt, salt_str)
        print(encrypted_passwd)

    elif args.action == 'decrypt':
        encrypted_passwd = args.passwd
        salt_str = args.salt
        salt = get_fixed_length_salt(salt_str)

        decrypted_passwd = decrypt(encrypted_passwd, salt, salt_str)
        print(decrypted_passwd)
