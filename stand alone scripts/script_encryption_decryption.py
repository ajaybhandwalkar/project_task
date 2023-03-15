import os
from cryptography.fernet import Fernet


class EncryptionAndDecryption:

    def __init__(self):
        key = self.get_encryption_key()
        self.f = Fernet(key)


    @staticmethod
    def get_encryption_key():
        enc_key = None
        if os.path.exists("encryption_key.txt"):
            if os.path.getsize('encryption_key.txt') == 0:
                res = input("Encryption key not found!\n\nDo you want to generate new key (y/n) : ")
                if res in "yY":
                    key = Fernet.generate_key()
                    enc_key = key
                    open("encryption_key.txt", "w").write(key.decode('UTF-8'))
            else:
                enc_key = str.encode(open("encryption_key.txt", "r").read())
        else:
            print("Encryption_key file missing...")
        if enc_key is not None:
            return enc_key
        else:
            raise Exception("Exception Occurred")

    def encrypt(self, word):
        return self.f.encrypt(str.encode(word))

    def decrypt(self, word):
        return self.f.decrypt(str.encode(word))

    def main(self):
        while True:
            option = input("\nSelect Option -\n1.Encrypt\n2.Decrypt\n3.Exit\n: ")
            if option == "3":
                break
            if option == "1":
                word = input("Enter Word : ")
                encrypted_word = self.encrypt(word)
                print("\n", encrypted_word.decode('UTF-8'))
            if option == "2":
                word = input("Enter Word : ")
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
