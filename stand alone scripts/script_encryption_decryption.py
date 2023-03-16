import os
from cryptography.fernet import Fernet


class EncryptionAndDecryption:

    def __init__(self):
        key = self.get_encryption_key()
        self.f = Fernet(key)

    @staticmethod
    def get_encryption_key():
        if not os.path.exists("encryption_key.txt"):
            return EncryptionAndDecryption.get_encryption_key()
        else:
            if not os.stat("encryption_key.txt").st_size == 0:
                return str.encode(open("encryption_key.txt", "r").read())
            else:
                return EncryptionAndDecryption.generate_encryption_key()

    @staticmethod
    def generate_encryption_key():
        key = Fernet.generate_key()
        enc_key = key
        open("encryption_key.txt", "w").write(key.decode('UTF-8'))
        return enc_key

    def encrypt(self, word):
        return self.f.encrypt(str.encode(word))

    def decrypt(self, word):
        return self.f.decrypt(str.encode(word))

    @staticmethod
    def get_word_to_encrypt():
        return input("Enter Word : ")

    def main(self):
        while True:
            option = input("\nSelect Option -\n1.Encrypt\n2.Decrypt\n9.Exit\n: ")
            if option == "9":
                break
            if option == "1":
                word = EncryptionAndDecryption.get_word_to_encrypt()
                encrypted_word = self.encrypt(word)
                print("\n", encrypted_word.decode('UTF-8'))
            elif option == "2":
                word = EncryptionAndDecryption.get_word_to_encrypt()
                decrypted_word = self.decrypt(word)
                print("\n", decrypted_word.decode('UTF-8'))
            else:
                print("Please Enter Valid Option")


if __name__ == '__main__':
    obj = EncryptionAndDecryption()
    obj.main()

# from hashlib import md5
# import requests
#
#
# class MD5EncryptionAndDecryption:
#
#     @staticmethod
#     def encode_word(password):
#         result = md5(password.encode())
#         print("The hexadecimal equivalent of Word is : ", end="")
#         return result.hexdigest()
#
#         # if result.hexdigest() == "f2b4ffb1fce6be175baac966150f9390":
#         #     print("Correct Password")
#
#     def main(self):
#         while True:
#             option = input("\nSelect Option -\n1.MD5 Encrypt\n2.MD5 Decrypt\n3.Exit\n: ")
#             if option == "3":
#                 break
#             word = input("Enter Word to Encrypt : ")
#             if option == "1":
#                 encoded_word = self.encode_word(word)
#                 print(encoded_word)
#
#
# if __name__ == '__main__':
#     obj = MD5EncryptionAndDecryption()
#     obj.main()
#
#
# """
# encode() : Converts the string into bytes to be acceptable by hash function.
# hexdigest() : Returns the encoded data in hexadecimal format.
# """
