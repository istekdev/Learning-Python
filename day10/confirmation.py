# Blueprint:
# This is responsible for checking the existence of each and every major file.
import encryption
import system
import os

def encryption():
    encryption.ping()
    if encryption.ping() == True:
        print("encryption.py Downloaded")
        return True
    else:
        print("encryption.py Failed to Download")
        return False
    
def system():
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
    if os.path.exists("hash.txt"):
        hashtxt = "exists"
        print("hash.txt Downloaded")
    elif os.path.exists("bitcoin.txt"):
        print("bitcoin.txt Downloaded")
        btctxt = "exists"
    elif os.path.exists("notepad.txt"):
        print("notepad.txt Downloaded")
        notepadtxt = "exists"
    elif os.path.exists("secq.txt"):
        print("secq.txt Downloaded")
        secqtxt = "exists"
    elif os.path.exists("seca.txt"):
        print("seca.txt Downloaded")
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
    if txt() and system() and encryption() == True:
        print("5/5 Files Successfully Downloaded")
        return "All"
    else:
        print("Error - Files Failed to Download")
        return "Fails"
