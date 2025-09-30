import time
import random

class PYDAY:
    def __init__(self, day):
        self.day = day
        
    def learningday(self):
        print(f"AS OF NOW, TODAY IS DAY {self.day} OF LEARNING PYTHON.")
        
def twofa():
    twofakey = ""
    yourpass = "ILoveCalicos"
    for characters in yourpass:
        twofakey += str(ord(characters)) # Since twofakey is an integer (and integers + strings don't mix well), we gotta make twofakey a string too
    print("KEEP THIS KEY WITH YOU FOR 2 FACTOR AUTHENTICATION: " + twofakey)
    time.sleep(1)
    twofaask = input("2FA - WHAT IS YOUR KEY: ")
    while twofaask != twofakey:
        twofaask = input("INFORRECT - WHAT IS YOUR KEY: ")
    menu()
    
def currenttime():
    epoch = time.time()
    local = time.localtime(epoch)
    strf = time.strftime("%H:%M:%S", local)
    print("THE TIME IS (IN MILITARY TIME): " + strf)
    time.sleep(1)
    menu()
    
saved = []
    
def notepad():
    print("WELCOME TO PYOS NOTEPAD - [SAVED]/[NEW]/[EXIT]")
    time.sleep(1)
    notes = input(">> ")
    if notes == "[SAVED]":
        showsaves()
        time.sleep(1)
        choicesaved = input("LEAVE OR NEW: ")
        if choicesaved == "LEAVE":
            notepad()
        elif choicesaved == "NEW":
            new()
        else:
            print("ERR - ACTION DOSEN'T EXIST")
            time.sleep(1)
            notepad()
    elif notes == "[NEW]":
        new()
    elif notes == "[EXIT]":
        menu()
    else:
        print("ERR - ACTION DOSEN'T EXIST")
        
def new():
    newin = input("")
    choicenew = input("ARE YOU SURE YOU WANT TO SAVE? [Y/N/E]")
    if choicenew == "Y":
        saved.append(str(newin))
        time.sleep(1)
        menu()
    elif choicenew == "N":
        new()
    elif choicenew == "E":
        menu()

def showsaves(): # Aparrently, you can't name a function and variable the same thing
    if not saved: # This literally means if nothing is in saved, much more better than if saved == "":
        print("NOTHING WAS SAVED.")
        time.sleep(1)
        notepad()
    else:
        print(saved)
        time.sleep(1)
        choicesave = input("LEAVE OR NEW: [L/N]")
        if choicesave == "L":
            menu()
        elif choicesave == "N":
            new()
        else:     
            print("ERR - ACTION DOSEN'T EXIST")

def btcminer():
    nonce = random.randint(1, 100000)
    guess = 0
    while guess != nonce:
        guess = random.randint(1, 100000)
        print("GUESSING NONCE - CURRENT GUESS: " + str(guess))
    print("NONCE SOLVED - 3.125 BTC ARRIVING SHORTLY.") 
    time.sleep(1)
    menu()

def rng():
    chooserng1 = input("CHOOSE MODE [ENTROPY/RANGE]")
    if chooserng1 == "RANGE":
        chooserng = input("WHAT IS THE MAX RANGE YOU WANT: ")
        rng1 = random.randint(1, int(chooserng)) # So even arguments aren't safe from int()
        print("YOUR RANDOM NUMBER IS: " + str(rng1))
        time.sleep(1)
        menu()
    elif chooserng1 == "ENTROPY":
        ent1 = time.time()
        ent2 = random.randint(1, 1000000)
        finality = (ent1 + ent2) * ent2
        print("YOUR RANDOM NUMBER IS: " + str(round(finality)))
        time.sleep(1)
        menu()
    else:
        print("YEAH... NO")

def lottery():
    winning = []
    yours = []
    while len(winning) < 5:
        winning.append(str(random.randint(1, 50)))
    guess1 = input("NUMBER 1: ")
    guess2 = input("NUMBER 2: ")
    guess3 = input("NUMBER 3: ")
    guess4 = input("NUMBER 4: ")
    guess5 = input("NUMBER 5: ")
    yours = [str(guess1), str(guess2), str(guess3), str(guess4), str(guess5)]
    time.sleep(1)
    print("YOUR NUMBERS: ", yours)
    time.sleep(1)
    print("WINNING NUMBERS: ", winning)
    if yours == winning:
        print("YOU JUST WON 5.2 BILLION DOLLARS IN PYTHON CURRENCY")
    else:
        print("YEAH, KEEP TRYING BOZO")
    time.sleep(1)
    menu()

def calc():
    calcin = input("CALCULATE (L TO LEAVE):")
    if calcin == "L":
        menu()
        return
    try:
        output = eval(calcin)
        print(output)
        time.sleep(1)
        calc()
    except Exception as e:
        print("ERR - ", e)

def nuke():
    for i in range(5, 0, -1): # So this should count down..?
        print(i)
        time.sleep(1) # Counts down every second ig
    print("ALLAHU AKBAR")
    time.sleep(1)
    while True:
        nukevals = random.randint(1, 100000000)
        print(nukevals)


def menu():
    print("OPTIONS:")
    time.sleep(1)
    print("[DAY] - CURRENT DAY OF LEARNING PYTHON")
    print("[TIME] - CURRENT TIME (MILITARY TIME)")
    print("[NOTES] - NOTEPAD")
    print("[BTC] - TOTALLY REAL BITCOIN MINING")
    print("[RNG] - RANDOM NUMBER GENERATOR")
    print("[LOT] - LOTTERY")
    print("[CALC] - CALCULATOR")
    print("[NUKE] - NUKE")
    time.sleep(1)
    choosemenu = input(">> ")
    if choosemenu == "[DAY]":
        you = PYDAY(7)
        you.learningday()
        time.sleep(1)
        menu()
    elif choosemenu == "[TIME]":
        currenttime()
    elif choosemenu == "[NOTES]":
        notepad()
    elif choosemenu == "[BTC]":
        btcminer()
    elif choosemenu == "[RNG]":
        rng()
    elif choosemenu == "[LOT]":
        lottery()
    elif choosemenu == "[CALC]":
        calc()
    elif choosemenu == "[NUKE]":
        nuke()
    else:
        print("ERR - FEATURE DOES NOT EXIST")
        time.sleep(1)
        menu()

print("WELCOME TO PYOS XP")
time.sleep(1)
password = input("PASSWORD:")
while password != "ILoveCalicos":
    password = input("TRY AGAIN - PASSWORD:")
twofa()

# Utilizied concepts from days 1-6: def, if, else, elif, class, len, print, input, str, int, round, for, in, while, time, random, range, and ord
# Utilized New Concepts I learned today like: try, except, and as
# Utilized concepts I didn't plan on learning (but learned anyway): eval, return, and not

  
