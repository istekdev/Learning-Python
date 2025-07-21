import time
import random
import encryption

registerin = ""
loginin = ""
masterin = ""
secqin = ""
secq = ""
seca = ""

def ping():
    return True

def lock():
    with open("hash.txt", "r") as readhash:
        read = readhash.read()
    if not read:
        register()
    else:
        login()

def register():
    global registerin, secq, seca
    registerin = input("PLEASE SET A PASSWORD: ")
    secq = input("SET YOUR SECURITY QUESTION: ")
    seca = input("SET YOUR ANSWER TO THE SECURITY QUESTION: ")
    encryption.encryptpass(registerin)
    with open("secq.txt", "w") as q:
        q.write(secq)
    encryption.encryptseca(seca)
    time.sleep(1)
    login()

def login():
    global loginin, masterin, secqin
    with open("secq.txt", "r") as sq:
        secqu = sq.read().strip()
    with open("seca.txt", "r") as sa:
        secqa = sa.read().strip()
    encryption.decryptsa(secqa)
    loginin = input("WHAT IS YOUR PASSWORD: ")
    masterin = input("WHAT IS YOUR MASTER KEY: ")
    secqin = input(secqu + " ")
    encryption.verification()
    while loginin != encryption.finaldepass:
        print("INCORRECT")
        loginin = input("WHAT IS YOUR PASSWORD: ")
    while masterin != encryption.masterkey:
        print("INCORRECT")
        masterin = input("WHAT IS YOUR MASTER KEY: ")
    while masterin != encryption.finaldespass:
        print("INCORRECT")
        secqin = input(secqu + " ")
    os()

def gettime():
    epoch = time.time()
    local = time.localtime(epoch)
    structure = time.strftime("%M/%D/%Y - %H:%M:%S", local)
    print(structure)

def calculator():
    print("WELCOME TO PYOS CALCULATOR - L to Leave")
    time.sleep(1)
    calc = input(">> ")
    if calc.upper() == "L":
        os()
    try:
        calcout = eval(calc)
        print(calcout)
        time.sleep(1)
        calc = input(">> ")
    except Exception as e:
        print(e)

def btcm():
    nonce = random.randint(1, len(str(round(time.time()))))
    guess = 0
    while guess != nonce:
        guess = random.randint(1, nonce)
        print("MINING. CURRENT GUESS - " + str(guess))
    print("BLOCK HAS BEEN SOLVED! 3.125 BTC ARRIVING TO YOUR WALLET SHORTLY...")
    with open("bitcoin.txt", "r") as btcr:
        balance = btcr.read().strip()
    if not balance:
        with open("bitcoin.txt", "w") as bbtc:
            bbtc.write("3.125")
    elif float(balance) > 0:
        with open("bitcoin.txt", "w") as wbtc:
            nb = float(balance) + 3.125
            wbtc.write(str(nb))
    time.sleep(1)
    os()
    

def os():
    gettime()
    print("PYOS VERSION 10")
    print("---")
    print("[BTCW] - Bitcoin Wallet")
    print("[BTCM] - Bitcoin Mining")
    print("[NOTE] - Notepad")
    print("[RNG] - Random Number Generator")
    print("[LOTTO] - Bitcoin Lottery")
    print("[GAMB] - Gambling (Bitcoin Reward)")
    print("[CALC] - Calculator")
    print("[SETTINGS] - Settings")
    print("[LOG OUT] - Log Out")
    print("[NUKE] - Nuke")
    time.sleep(1)
    oschoose = input(">> ")
    if oschoose.upper() == "[BTCW]":
        btcw()
    elif oschoose.upper() == "[BTCM]":
        btcm()
    elif oschoose.upper() == "[NOTE]":
        notepad()
    elif oschoose.upper() == "[RNG]":
        rng()
    elif oschoose.upper() == "[LOTTO]":
        lottery()
    elif oschoose.upper() == "[GAMB]":
        gambling()
    elif oschoose.upper() == "[CALC]":
        calculator()
    elif oschoose.upper() == "[SETTINGS]":
        settings()
    elif oschoose.upper() == "[LOG OUT]":
        lock()
    elif oschoose.upper() == "[NUKE]":
        nuke()

    
    
