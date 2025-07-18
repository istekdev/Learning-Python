import encrypt
import time
import os

def detpass():
  new = input("SET PASSWORD: ")
  encrypt.encode()

print("WELCOME TO PYVAULT")
time.sleep(1)

with open("pass.txt", "r") as password:
  psw = password.read()
  if not psw:
    detpass()
  else:
    enter = input("YOUR PASSWORD: ")
    encrypt.verify()

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
        enter = input("YOUR PASSWORD: ")
        encrypt.verify()
      elif choosenew.upper() == "NEW":
        new()
    else:
      choosenow = input("CHOOSE ACTION (WRITE/LEAVE/SAVED): ")
      if choosenew.upper() == "WRITE":
        write()
      elif choosenew.upper() == "LEAVE":
        enter = input("YOUR PASSWORD: ")
        encrypt.verify()
      elif choosenew.upper() == "SAVED":
        saved()

def write():
  with open("vault.txt", "r") as previous:
      encrypt.decrypt()
  print(str(encrypt.decrypted))
  time.sleep(1)
  writein = input("")
  writeaction = input("CHOOSE ACTION (SAVE/LEAVE): "
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
  newaction = input("CHOOSE ACTION (SAVE/LEAVE): "
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
  else:
    except Exception as e:
      print("ERR", e)

