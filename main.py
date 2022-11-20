# Copyright © alfinkresna 2022
from halo import Halo
import os, time
import rsa


class Data:

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key


    def generate_keys(self):
        with open("publicKey.pem", "wb") as k:
            k.write(self.public_key.save_pkcs1("PEM"))
        with open("privateKey.pem", "wb") as k:
            k.write(self.private_key.save_pkcs1("PEM"))


    def load_public_key(self):
        with open("publicKey.pem", "rb") as k:
            public_key = rsa.PublicKey.load_pkcs1(k.read())
            return public_key


    def load_private_key(self):
        with open("privateKey.pem", "rb") as k:
            private_key = rsa.PrivateKey.load_pkcs1(k.read())
            return private_key


    def encrypt(self):
        with open("publicKey.pem", "rb") as f:
            pub = rsa.PublicKey.load_pkcs1(f.read())
        text = input("Input Text : ")
        enc = rsa.encrypt(text.encode(), pub)
        with open("encrypted.text", "wb") as w:
            w.write(enc)
        return "\nCek 'encrypted.text' File"


    def decrypt(self):
        with open("privateKey.pem", "rb") as f:
            priv = rsa.PrivateKey.load_pkcs1(f.read())
        rf = open("encrypted.text", "rb").read()
        dec = rsa.decrypt(rf, priv).decode("utf-8")
        return f"Decrypted Text : {dec}"


    def clear(self):
        if os.name.__eq__("posix"):
            os.system("clear")
        else:
            os.system("cls")


def main():
    public_key, private_key = rsa.newkeys(1024)
    data = Data(public_key, private_key)
    spin = Halo(text="Generating Keys", spinner="dots")
    try:
        while True:
            i = int(input("\n[1] Generate Keys\n\n[2] Load Public Key\n\n[3] Load Private Key\n\n[4] Encrypt Text\n\n[5] Decrypt Text\n\n>> Pilih Menu : "))
            if i == (1):
                print()
                spin.start()
                data.generate_keys()
                spin.stop()
                data.clear()
                print("\n-----Generate Keys Selesai-----")
                time.sleep(2)
                data.clear()
            elif i == (2):
                data.clear()
                print(data.load_public_key())
            elif i == (3):
                data.clear()
                print(data.load_private_key())
            elif i == (4):
                data.clear()
                print(data.encrypt())
            elif i == (5):
                data.clear()
                print(data.decrypt())
            else:
                print("\n[!] Pilihan Salah!")
    except ValueError as error:
        print(f"\n{error}")


if __name__ == "__main__":
    main()
