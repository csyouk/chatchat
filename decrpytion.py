from Crypto.Cipher import AES

key = input("Enter password to decrpyt : ")
l = len(key)
if l < 16:
    key = key + " " * (16 - l)
elif l > 16:
    key = key[0:16]
else:
    pass

with open('encrypted', 'rb') as f:
    data = f.read()


decryption_suite = AES.new(key, AES.MODE_CFB, 'This is an IV456')
plain_text = decryption_suite.decrypt(data)

deciphered_txt = open("chat.csv", 'wb')
deciphered_txt.write(plain_text)
deciphered_txt.close()
