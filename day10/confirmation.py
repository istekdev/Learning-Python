# Blueprint:
# This is responsible for checking the existence of each and every major file.
import encryption
import system
import os

def enping():
    encryption.ping()
    if encryption.ping() == True:
        print("encryption.py Downloaded")
        return True
    else:
        print("encryption.py Failed to Download")
        return False
    
def sysping():
    system.ping()
    if system.ping() == True:
        print("system.py Downloaded")
        return True
    else:
        print("system.py Failed to Download")
        return False
    
def txt():
    hashtxt = ""
    btctxt = ""
    notepadtxt = ""
    secqtxt = ""
    secatxt = ""
    if os.path.exists("hash.txt") and os.path.exists("bitcoin.txt") and os.path.exists("notepad.txt") and os.path.exists("secq.txt") and os.path.exists("seca.txt"):
        hashtxt = "exists"
        btctxt = "exists"
        notepadtxt = "exists"
        secqtxt = "exists"
        secatxt = "exists"
    else:
        hashtxt = "fail"
        btctxt = "fail"
        notepadtxt = "fail"
        secqtxt = "fail"
        secatxt = "fail"
        print(".txt Files Failed to Download")
    if hashtxt and btctxt and notepadtxt and secqtxt and secatxt == "exists":
        return True
    else:
        return False
    
def verification():
    if txt() and sysping() and enping() == True:
        print("5/5 Files Successfully Downloaded")
        return "All"
    else:
        print("Error - Files Failed to Download")
        return "Fails"
