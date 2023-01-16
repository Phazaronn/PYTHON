# @phazaronn
# -*- coding: utf-8 -*-
# bhc.py
import hashlib, sys
def TakeWords(filename=str(sys.argv[1])):
    with open(filename) as fopen:
        output = fopen.read().splitlines()
    return output
def CreateHash(word = "null"):
    return hashlib.sha512(word.encode()).hexdigest()
# fonksiyonlarin tanimlanmasi
f, h = False, sys.argv[2]
for i in TakeWords():
    if CreateHash(i) == str(h):
        word = i
        f = True
        break
if f:
    print(f"Hash Cracked: {word}")
else:
    print("Hash not cracked")