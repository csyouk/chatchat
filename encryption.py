from Crypto.Cipher import AES
# Encryption

key = input("Enter password to encrpyt : ")
l = len(key)
if l < 16:
    key = key + " " * (16 - l)
elif l > 16:
    key = key[0:16]
else:
    pass

encryption_suite = AES.new(key, AES.MODE_CFB, 'This is an IV456')

with open('chat.csv', 'r') as f:
    data = f.read()

cipher_text = encryption_suite.encrypt(data)

ciphered_txt = open("encrypted.txt", 'wb')
ciphered_txt.write(cipher_text)
ciphered_txt.close()
