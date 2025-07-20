import random
import time

maskerkey = 0
passhash = ""
hashedpass = ""
securityquestion = ""
securityanswer = ""
decryption = ""

def ping():
  return True

def encryptpass(password):
  global masterkey, passhash, hashedpass
  passhash = ""
  for passes in password:
    passhash += str(ord(passes))
  masterkey = random.randint(1, len(passhash)) * round(time.time())
  hashedpass = passhash * str(masterkey)
  print("THIS IS YOUR MASTER KEY, DO NOT LOSE IT. THIS WILL BE YOUR TWO-FACTOR AUTHENTICATION: " + masterkey)
  with open("hash.txt", "w") as encryptingpass:
    encryptingpass.write(hashedpass)

def encryptnotes():
  with open("notepad.txt", "r") as readnotes:
    if not readnotes:
      print("ERROR - NOTEPAD BLANK, CANNOT ENCRYPT")
      return
    else:
      notesread = readnotes.read().strip()
  for notes in notesread:
    encryptingnotes += str(ord(notes))
  encryptingthenotes = encryptingnotes * str(masterkey)
  print("NOTES SAVED")

def decryptpass(password):
  with open("hash.txt", "r") as decryptionhash:
    dehash = decryptionhash.read().strip()
  stage1de += dehash // int(masterkey)
  stage2de += str(stage1de)

  while len(stage2de) % 3 != 0:
    stage2de = "0" + stage2de

  for stage3de in range(0, len(stage2de), 3):
    depassout = stage3de[stage3de:stage3de+3]
    finaldepass += chr(int(depassout))
