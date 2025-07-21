import random
import time

maskerkey = 0
passhash = ""
hashedpass = ""
securityquestion = ""
securityanswer = ""
decryption = ""
secahash = ""
hashedseca = ""
finaldepass = ""
decryptednotes = ""

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
  with open("notepad.txt", "w") as writenotes:
    writenotes.write(str(encryptingthenotes))
  print("NOTES SAVED")

def encryptseca(seca):
  global secahash, hashedseca
  secahash = ""
  for a in seca:
    secahash += str(ord(a))
  hashedseca = secahash * str(masterkey)
  with open("seca.txt", "w") as aa:
    aa.write(str(hashedseca))

def decryptpass(password):
  global finaldepass
  finaldepass = ""
  with open("hash.txt", "r") as password:
    dehash = password.read().strip()
  stage1de += dehash // int(masterkey)
  stage2de += str(stage1de)

  while len(stage2de) % 3 != 0:
    stage2de = "0" + stage2de

  for stage3de in range(0, len(stage2de), 3):
    depassout = stage3de[stage3de:stage3de+3]
    finaldepass += chr(int(depassout))
    return finaldepass

def decryptsa(seca):
  global finaldespass
  finaldespass = ""
  with open("seca.txt", "r") as seca:
    desa = seca.read().strip()
  stage1des += desa // int(masterkey)
  stage2des += str(stage1des)

  while len(stage2des) % 3 != 0:
    stage2des = "0" + stage2des

  for stage3des in range(0, len(stage2des), 3):
    despassout = stage3des[stage3des:stage3des+3]
    finaldespass += chr(int(despassout))
    return finaldespass
  
def decryptnotes():
  global decryptednotes
  decryptednotes = ""
  with open("notepad.txt", "r") as np:
    npdata = np.read().strip()
  s1np += npdata // int(masterkey)
  s2np += str(s1np)

  while len(s2np) % 3 != 0:
    s2np = "0" + s2np

  for s3np in range(0, len(s2np), 3):
    s4out = s3np[s3np:s3np+3]
    decryptednotes += chr(int(s4out))
    return decryptednotes
