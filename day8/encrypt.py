import time
import random
import os
import main

masterkey = None
encryptedpass = None # Something to do with making it a global var

def encode(password):
  global masterkey, encryptedpass # Ohh this makes it global, nice
  for newchars in password:
    encryptedpass += str(ord(newchars))
    masterkey = str(random.randint(1, len(encryptedpass)))
  encodefinal = int(encryptedpass) * int(masterkey) # In the end, these are still numbers
  with open("pass.txt", "w") as encryption:
    encryption.write(encodefinal)
  print("THIS IS YOUR MASTER KEY, THE ONLY KEY THAT CAN VERIFY YOUR PASSWORD, KEEP IT SAFE: ", encodefinal)
  time.sleep(1)
  main.currpass()

def verify(password):
  verification = input("WHAT IS YOUR MASTER KEY: ")
  with open("pass.txt", "r") as verifypass:
    passhash = verifypass.read()
  dehash = int(passhash) / int(verification) # Still numbers
  while dehash != encryptedpass:
    wrong1 = input("INCORRECT - CHOOSE ACTION (REDOPASS/REDOKEY): ")
    if wrong1.upper() == "REDOPASS":
      main.currpass()
    elif wrong1.upper() == "REDOKEY":
      verification = input("WHAT IS YOUR MASTER KEY: ")
      verify()
  granted()

def encryptsaves():
  with open("vault.txt", "r") as toencrypt:
    toencode = toencrypt.read()
  for encryptors in toencode:
      stage1 += str(ord(encryptors))
      stage2 = stage1 * masterkey
  with open("vault.txt", "w") as todoencrypt:
    todoencrypt.write(str(stage2))

def decrypt():
  with open("vault.txt", "r") as writing:
    encryptedshi = writing.read()
  for blobs in encryptedshi:
    decrypt1 = encryptedshi // masterkey
    decrypt2 = chr(decrypt1)
    decrypted += decrypt2

# This uses concepts from day 1-7: def, for, in, while, ord, str, time, random, if, else, elif, , import (external), and len
# This uses new concepts like: with, upper, import (local), global, and chr
# Sadly couldn't use class, eval, try, int, except, and range since idk what to do with those
  
