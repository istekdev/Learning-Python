import time
import random
# Just removed import main, ciruclar imports (which means both files import each other and make a loop)

masterkey = ""
encryptedpass = "" # Something to do with making it a global var
decrypted = ""

def encode(password):
  global masterkey, encryptedpass # Ohh this makes it global, nice
  encryptedpass = ""
  for newchars in password:
    encryptedpass += str(ord(newchars)).zfill(3) # I believe ZFill is where I add a zero three digits back of a number (eg: 073)
  masterkey = str(random.randint(1, 100000))
  encodefinal = int(encryptedpass) * int(masterkey) # In the end, these are still numbers
  with open("pass.txt", "w") as encryption:
    encryption.write(str(encodefinal))
  print("THIS IS YOUR MASTER KEY, THE ONLY KEY THAT CAN VERIFY YOUR PASSWORD, KEEP IT SAFE: ", masterkey)
  time.sleep(1)
  return masterkey

def verify(password):
  encryptedpass = ""
  for c in password:
    encryptedpass += str(ord(c)).zfill(3)
  verification = input("WHAT IS YOUR MASTER KEY: ")
  if not verification:
    print("MASTER KEYS ARE NEVER ZERO")
    time.sleep(1)
    verify(password)
  with open("pass.txt", "r") as verifypass:
    passhash = int(verifypass.read())
  dehash = passhash // int(verification) # Still numbers
  while dehash != int(encryptedpass):
    wrong1 = input("INCORRECT - CHOOSE ACTION (REDOPASS/REDOKEY): ")
    if wrong1.upper() == "REDOPASS":
      enter = input("YOUR PASSWORD: ")
      verify(enter)
    elif wrong1.upper() == "REDOKEY":
      return verify(password) # Stops a logic bomb, calling it but not giving it anything in the argument params. It's like Python's paradox.

def encryptsaves(data):
  stage1 = ""
  with open("vault.txt", "r"):
    toencode = data.strip()
  if not toencode:
    return
  for encryptors in toencode:
      stage1 += str(ord(encryptors)).zfill(3)
  if not stage1 or not masterkey: # New use, or. Self explanatory
    return
  stage2 = int(stage1) * int(masterkey)
  with open("vault.txt", "w") as todoencrypt:
    todoencrypt.write(str(stage2))

def decrypt():
  global decrypted
  decrypted = ""
  decrypt1 = 0
  with open("vault.txt", "r") as writing:
    if not writing: # This has been bugging me a lot, now, it checks if vault.txt has shit in it, if not, then nothing happens
      decrypted = ""
      return
    encryptedshi = int(writing.read())
  decrypt1 += encryptedshi // int(masterkey)
  decrypt2 = str(decrypt1) # Convert the numerical result as a string

  while len(decrypt2) % 3 != 0: # Checks if the string isn't divisible by 3
    decrypt2 = "0" + decrypt2 # Adds a zero before if divisible by 3..?

  for finalities in range(0, len(decrypt2), 3): # Start, stop, and step. 0 is placed at the start of the number, accompanied by the ASCII length of the string, step is splitting it every 3 characters
    comp = decrypt2[finalities:finalities+3] # I suppose this is responsible for making sure I get exactly 3 characters per encoded letter..?
    decrypted += chr(int(comp))

# This uses concepts from day 1-7: def, for, in, while, ord, str, time, random, if, else, elif, int, import (external), range, and len
# This uses new concepts like: with, upper, import (local), global, or, and chr
# Sadly couldn't use class, eval, try, and except since idk what to do with those
  
