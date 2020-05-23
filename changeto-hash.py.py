#python project
#mehraan kiya
#roshanamooz

import hashlib, bcrypt

password = input("Input the password to hash\n>")
print("\nSHA1:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.sha1(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
print("\nMD5:\n")
for i in range(3):
    setpass = bytes(password, 'utf-8')
    hash_object = hashlib.md5(setpass)
    guess_pw = hash_object.hexdigest()
    print(guess_pw)
print("\nBCRYPT:\n")
for i in range(3):
    hashed = bcrypt.hashpw(setpass, bcrypt.gensalt(10))