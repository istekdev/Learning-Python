import time
import uploads
import encrypt
import random

def strength():
  length = len(newpass)
  hascap = False
  haslow = False
  hasnum = False
  hassym = False
  syms = "/.,<>?:;][{}|\)(*&^%$#@!~`+_"
  for cri in range(length):
    

def signup():
  global newpass
  print("Ensure - Password is > 12 characters with at least one capital letter, lowercase letter, number, and symbol")
  time.sleep(1)
  newpass = input("NEW PASSWORD: ")
  strength()

def ver():
  with open("pass.txt", "r") as psw:
    pswr = psw.read()
  if not pswr:
    signup()
  else:
    signin()

print("WELCOME TO PYPASS")
time.sleep(1)
print("Where your passwords are safest.")
time.sleep(1)
uploads.check()
time.sleep(1)
ver()
