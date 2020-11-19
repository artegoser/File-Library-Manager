import random

def gensteam1():
    out = ""
    keys = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    for i in range(3):
        for g in range(5):
            out += random.choice(keys)
        out += "-"
    return out[:-1]
    
def gensteam2():
    out = ""
    keys = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    for i in range(5):
        for g in range(5):
            out += random.choice(keys)
        out += "-"
    return out[:-1]
    
def gensteam3():
    out = ""
    keys = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    num = "1234567890"
    for i in range(15):
        out += random.choice(keys)
    out += " "
    for i in range(2):
        out += random.choice(num)
    return out
    
def genpass(length):
    password=''
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(length):
        password += random.choice(chars)
    return password
    
def xor_cipher(str, key):
    encript_str = ""
    for letter in str:
        encript_str += chr(ord(letter)^key)
    return encript_str
    
def SimpleStrHash(stre):
    hash = 0
    for i in stre:
        hash += ord(i)
        
    return hex(hash)