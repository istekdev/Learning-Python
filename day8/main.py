import encrypt
import time
import os

def detpass():
  new = input("SET PASSWORD: ")
  encrypt.encode(new)

def currpass():
  enter = input("YOUR PASSWORD: ")
  encrypt.verify(enter)

print("WELCOME TO PYVAULT")
time.sleep(1)

with open("pass.txt", "r") as password:
  psw = password.read()
  if not psw:
    detpass()
  else:
    currpass()


def granted():
  print("ACCESS GRANTED - WELCOME TO MY VAULT")
  time.sleep(1)
  with open("vault.txt", "r") as valuables:
    notes = valuables.read()
    if not notes:
      choosenew = input("CHOOSE ACTION (WRITE/LEAVE/NEW): ")
      if choosenew.upper() == "WRITE":
        write()
      elif choosenew.upper() == "LEAVE":
        currpass()
      elif choosenew.upper() == "NEW":
        new()
    else:
      choosenow = input("CHOOSE ACTION (WRITE/LEAVE/SAVED): ")
      if choosenow.upper() == "WRITE":
        write()
      elif choosenow.upper() == "LEAVE":
        encrypt.encryptsaves()
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
        writing.write(str(writein))
        print("CONTENT SAVED")
  elif writeaction.upper() == "LEAVE":
    granted()

def new():
  with open("vault.txt", "r") as previous:
      encrypt.decrypt()
  print(str(encrypt.decrypted))
  time.sleep(1)
  newin = input("")
  newaction = input("CHOOSE ACTION (SAVE/LEAVE): ")
  if newaction.upper() == "SAVE":
    with open("vault.txt", "w") as overwrote:
        overwrote.write(str(newin))
        print("CONTENT SAVED")
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

# This uses concepts from days 1-7: def, if, else, elif, print, input, import (external), random, time, not, and str
# This uses new concepts like upper, with, and import (locally)
# Could not use for, ord, while, and random since encrypt.py uses it
# Could not use eval since I don't know what do use it for (no non-linear math here) class, int, try, except, and range
