# Day 8 of Python
# This is by far the most mentally draining things I made. And worst of all, this is just a warmup.
# I planned to learn how to locally import Python files using import, and interact with txt files using with. 
# But instead, I got bombareded with new concepts. It's like giving a Pre-Algebra student College Calculus when they got a 100% on their test.
# Hell, I don't even understand some of them. Like look at these:
# zfill, [i:i+3], % 3, //, return, and global
# But some were also unexpected yet easier to learn, like eval, which acted as a non-linear equation calculator. And the function "or", which, as it sounds, gives an alternative. 
# ---
# Aparrently, zfill() "pads" a string, basically adds zeroes behind a number (eg: 5 -> 005)
# For [i:i+3], it looks Calculus-like, but it just splits strings. So if I were to have a variable equaling to "abcde," and I did [0:3], i'd get "abc." The +3 means that I only get a chunk of 3.
# % 3 is more complex, % returns the remainder of an equation (eg: 7 % 3 = 1, basically 7/3 is 2, the remainder is 1.. we on the same page..?)
# // is floor divison, removes the decimal. No rounding.
# return.. well.. returns a value or function
# global makes a variable globally usable.


import encrypt
import time

def granted():
  print("ACCESS GRANTED - WELCOME TO MY VAULT")
  time.sleep(1)
  with open("vault.txt", "r") as valuables:
    notes = valuables.read()
    if not notes:
      choosenew = input("CHOOSE ACTION (NEW/LEAVE): ")
      if choosenew.upper() == "LEAVE":
        currpass()
      elif choosenew.upper() == "NEW":
        new()
    else:
      choosenow = input("CHOOSE ACTION (WRITE/LEAVE/SAVED): ")
      if choosenow.upper() == "WRITE":
        write()
      elif choosenow.upper() == "LEAVE":
        currpass()
      elif choosenow.upper() == "SAVED":
        saved()

def write():
  encrypt.decrypt()
  print(str(encrypt.decrypted))
  time.sleep(1)
  writein = input("")
  writeaction = input("CHOOSE ACTION (SAVE/LEAVE): ")
  if writeaction.upper() == "SAVE":
    with open("vault.txt", "a") as writing:
        encrypt.encryptsaves(writein)
        print("CONTENT SAVED")
        time.sleep(1)
        granted()
  elif writeaction.upper() == "LEAVE":
    granted()

def new():
  newin = input("")
  newaction = input("CHOOSE ACTION (SAVE/LEAVE): ")
  if newaction.upper() == "SAVE":
    with open("vault.txt", "w") as overwrote:
        encrypt.encryptsaves(newin)
        print("CONTENT SAVED")
        time.sleep(1)
        granted()
  elif newaction.upper() == "LEAVE":
    granted()

def saved():
  with open("vault.txt", "r") as previous:
      encrypt.decrypt()
  print(str(encrypt.decrypted))
  time.sleep(1)
  savedaction = input("WOULD YOU LIKE TO LEAVE? (Y/N): ")
  if savedaction.upper() == "Y":
    granted()
  elif savedaction.upper() == "N":
    saved()

def detpass():
  new = input("SET PASSWORD: ")
  encrypt.encode(new) # Needs argument, I think it's to tell the function what varaible is being used?
  currpass()

def currpass():
  enter = input("YOUR PASSWORD: ")
  encrypt.verify(enter)
  granted()

print("WELCOME TO PYVAULT")
time.sleep(1)

with open("pass.txt", "r") as password:
  psw = password.read()
  if not psw:
    detpass()
  else:
    currpass()

# This uses concepts from days 1-7: def, if, else, elif, print, input, import (external), random, time, not, and str
# This uses new concepts like upper, with, and import (locally)
# Could not use for, ord, int, range, while, and random since encrypt.py uses it
# Could not use eval since I don't know what do use it for (no non-linear math here) class, try, and except
