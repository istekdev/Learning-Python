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

def rng():
    rngin = input("CHOOSE METHOD OF RNG [ENTROPY/RANGE] OR [LEAVE] TO LEAVE: ")
    if rngin.upper() == "ENTROPY":
        entropy1 = time.time()
        entropy2 = encryption.masterkey
        entropy3 = random.randint(1, len(str(round(time.time()))))
        entropyf = round((entropy1 * entropy2) / entropy3)
        print("YOUR NUMBER IS " + entropyf)
        time.sleep(1)
        rng()
    elif rngin.upper() == "RANGE":
        rngr = input("CHOOSE A RANGE: ")
        rngrr = random.randint(1, int(rngr))
        print("YOUR NUMBER IS " + str(rngrr))
        time.sleep(1)
        rng()
    elif rngin.upper() == "LEAVE":
        os()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        rng()


def btcw():
    with open("bitcoin.txt", "r") as wallet:
        balance = wallet.read().strip()
    print("YOU HAVE" + balance + " BTC")
    time.sleep(1)
    os()

def btcm():
    nonce = random.randint(1, len(str(round(time.time()))))
    guess = -1
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

def nuke():
    for counts in range(5, 0, -1):
        print(counts)
        time.sleep(1)
    print("ALLAHU AKBAR!")
    with open("hash.txt", "w") as nuke1, open("secq.txt", "w") as nuke2, open("bitcoin.txt", "w") as nuke3, open("seca.txt", "w") as nuke4, open("notepad.txt", "w") as nuke5:
        nuke1.write("")
        nuke2.write("")
        nuke3.write("")
        nuke4.write("")
        nuke5.write("")
    while True:
        nuke6 = random.randint(1, len(str(round(time.time()))))
        print(nuke6)

def lottery():
    guess = []
    winnings = []
    while len(winnings) < 5:
        winnings.append(str(random.randint(1, 50)))
    guess1 = input("YOUR NUMBER 1: ")
    guess2 = input("YOUR NUMBER 2: ")
    guess3 = input("YOUR NUMBER 3: ")
    guess4 = input("YOUR NUMBER 4: ")
    guess5 = input("YOUR NUMBER 5: ")
    guess = [str(guess1), str(guess2), str(guess3), str(guess4), str(guess5)]
    print("YOUR NUMBERS: ", guess)
    time.sleep(1)
    print("WINNING NUMBERS: ", winnings)
    time.sleep(1)
    if guess == winnings:
        print("YOU JUST WON 170 BTC! CONGRATS!")
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
        choosepostwin = input("WOULD YOU LIKE TO PLAY AGAIN? [Y/N]: ")
        if choosepostwin.upper() == "Y":
            lottery()
        elif choosepostwin.upper() == "N":
            os()
        else:
            print("ERROR - DOES NOT EXIST")
    else:
        print("YOU DID NOT WIN :(")
        choosepostloss = input("WOULD YOU LIKE TO PLAY AGAIN? [Y/N]: ")
        if choosepostloss.upper() == "Y":
            lottery()
        elif choosepostloss.upper() == "N":
            os()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            os()

def notepad():
    with open("notepad.txt", "r") as readingnotes:
        readnotes = readingnotes.read().strip()
    if not readnotes:
        notepadin = input("CHOOSE ACTION [NEW/LEAVE]: ")
        if notepadin.upper() == "NEW":
            new()
        elif notepadin.upper() == "LEAVE":
            os()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            notepad()
    else:
        notepadin = input("CHOOSE ACTION [WRITE/SAVED/LEAVE]: ")
        if notepadin.upper() == "WRITE":
            write()
        elif notepadin.upper() == "SAVED":
            saved()
        elif notepadin.upper() == "LEAVE":
            os()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            notepad()

def saved():
    encryption.decryptnotes()
    print(encryption.decryptednotes)
    time.sleep(1)
    notepad()


def write():
    encryption.decryptnotes()
    print(encryption.decryptednotes)
    time.sleep(1)
    writein = input("")
    writeinin = input("DO YOU WANT TO SAVE? [Y/N]: ")
    if writeinin.upper() == "Y":
        encryption.encryptnotes(writein)
        time.sleep(1)
        notepad()
    elif writeinin.upper() == "N":
        notepad()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        notepad()


def new():
    newin = input("")
    newinin = input("DO YOU WANT TO SAVE? [Y/N]: ")
    if newinin.upper() == "Y":
        encryption.encryptnotes(newin)
        time.sleep(1)
        notepad()
    elif newinin.upper() == "N":
        notepad()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        notepad()

def roulette():
    rw = ""
    rin = input("HOW MUCH BTC DO YOU WANT TO BET: ")
    with open("bitcoin.txt", "r") as balances:
        rb = balances.read().strip()
    while rb < rin:
        print("YOU DO NOT HAVE ENOUGH")
        time.sleep(1)
        rin = input("HOW MUCH BTC DO YOU WANT TO BET: ")
    rwin = random.randint(1, 2)
    if rwin == 1:
        rw = "BLACK"
    elif rwin == 2:
        rw = "RED"
    rchoose = input("CHOOSE A BET (RED/BLACK): ")
    if rchoose.upper() == "RED":
        for count in range(5, 0, -1):
            print(count)
            time.sleep(1)
            print("YOUR BET: " + rchoose)
            time.sleep(1)
            print("SELECTED: " + rw)
            time.sleep(1)
            if rchoose == rw:
                with open("bitcoin.txt", "r") as btcr:
                    balance = btcr.read().strip()
                with open("bitcoin.txt", "w") as wbtc:
                    rb = float(balance) * 2
                    wbtc.write(str(rb))
                print("YOU JUST WON")
                time.sleep(1)
                rchoosepost = input("PLAY AGAIN (Y/N): ")
                if rchoosepost.upper() == "Y":
                    gambling()
                elif rchoosepost.upper() == "N":
                    os()
                else:
                    print("ERROR - DOES NOT EXIST")
                    time.sleep(1)
                    gambling()
            else:
                with open("bitcoin.txt", "r") as btcr:
                    balance = btcr.read().strip()
                with open("bitcoin.txt", "w") as wbtc:
                    rb = float(balance) - int(rin)
                    wbtc.write(str(rb))
                print("YOU JUST LOST")
                time.sleep(1)
                rchoosepost = input("PLAY AGAIN (Y/N): ")
                if rchoosepost.upper() == "Y":
                    gambling()
                elif rchoosepost.upper() == "N":
                    os()
                else:
                    print("ERROR - DOES NOT EXIST")
                    time.sleep(1)
                    gambling()
    elif rchoose.upper() == "BLACK":
        for count in range(5, 0, -1):
            print(count)
            time.sleep(1)
            print("YOUR BET: " + rchoose)
            time.sleep(1)
            print("SELECTED: " + rw)
            time.sleep(1)
            if rchoose == rw:
                with open("bitcoin.txt", "r") as btcr:
                    balance = btcr.read().strip()
                with open("bitcoin.txt", "w") as wbtc:
                    rb = float(balance) * 2
                    wbtc.write(str(rb))
                print("YOU JUST WON")
                time.sleep(1)
                rchoosepost = input("PLAY AGAIN (Y/N): ")
                if rchoosepost.upper() == "Y":
                    gambling()
                elif rchoosepost.upper() == "N":
                    os()
                else:
                    print("ERROR - DOES NOT EXIST")
                    time.sleep(1)
                    gambling()
            else:
                with open("bitcoin.txt", "r") as btcr:
                    balance = btcr.read().strip()
                with open("bitcoin.txt", "w") as wbtc:
                    rb = float(balance) - int(rin)
                    wbtc.write(str(rb))
                print("YOU JUST LOST")
                time.sleep(1)
                rchoosepost = input("PLAY AGAIN (Y/N): ")
                if rchoosepost.upper() == "Y":
                    gambling()
                elif rchoosepost.upper() == "N":
                    os()
                else:
                    print("ERROR - DOES NOT EXIST")
                    time.sleep(1)
                    gambling()

def guess():
    gin = input("HOW MUCH BTC DO YOU WANT TO BET: ")
    with open("bitcoin.txt", "r") as balances:
        gb = balances.read().strip()
    while gb < gin:
        print("YOU DO NOT HAVE ENOUGH")
        time.sleep(1)
        gin = input("HOW MUCH BTC DO YOU WANT TO BET: ")
    gw = random.randint(1, 50)
    time.sleep(1)
    gchoose = input("GUESS A NUMBER FROM 1-50: ")
    if gchoose == gw:
        with open("bitcoin.txt", "r") as btcr:
            balance = btcr.read().strip()
        with open("bitcoin.txt", "w") as wbtc:
            rb = float(balance) * 2
            wbtc.write(str(rb))
        print("YOU JUST WON")
        time.sleep(1)
        rchoosepost = input("PLAY AGAIN (Y/N): ")
        if rchoosepost.upper() == "Y":
            gambling()
        elif rchoosepost.upper() == "N":
            os()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            gambling()
    else:
        with open("bitcoin.txt", "r") as btcr:
            balance = btcr.read().strip()
        with open("bitcoin.txt", "w") as wbtc:
            rb = float(balance) - int(gin)
            wbtc.write(str(rb))
        print("YOU JUST LOST")
        time.sleep(1)
        rchoosepost = input("PLAY AGAIN (Y/N): ")
        if rchoosepost.upper() == "Y":
            gambling()
        elif rchoosepost.upper() == "N":
            os()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            gambling()


def gambling(): # This.. this is the best part of PYOS 10. I'm glad Pycrosoft added this.
    print("PYOS BTC GAMBLING SERVICES")
    time.sleep(1)
    print("[ROULETTE] - Roulette")
    print("[GUESS] - Guess RNG")
    time.sleep(1)
    gamblingin = input(">> ")
    if gamblingin.upper() == "ROULETTE":
        roulette()
    elif gamblingin.upper() == "GUESS":
        guess()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        gambling()

class PYDAY:
    def __init__(self, day):
        self.day = day
    
    def today(self):
        print(f"PYTHON PROGRESS: DAY {self.day}")

def settings():
    print("PYOS SETTINGS")
    tdy = PYDAY(11)
    tdy.today()
    print("---")
    print("[SECQ] - Change Security Question")
    print("[SECA] - Change Security Answer")
    print("[PASS] - Change Password")
    print("[MK] - New Master Key")
    print("[LEAVE] - Exit Settings")
    time.sleep(1)
    settingin = input(">> ")
    if settingin.upper() == "[SECQ]":
        choosesecq = input("NEW SECURITY QUESTION (L To Return): ")
        if choosesecq.upper() == "L":
            settings()
            return
        else:
            with open("secq.txt", "w") as q:
                q.write(choosesecq)
                print("SUCCESSFULLY CHANGED SECURITY QUESTION")
                time.sleep(1)
                settings()
    elif settingin.upper() == "[SECA]":
        verifysa = input("OLD SECURITY ANSWER (L To Return): ")
        if verifysa.upper() == "L":
            settings()
            return
        encryption.decryptseca(seca)
        while verifysa != encryption.finaldespass:
            print("INCORRECT")
            time.sleep(1)
            verifysa = input("OLD SECURITY ANSWER (L To Return): ")
        chooseseca = input("NEW SECURITY ANSWER: ")
        encryption.encryptseca(chooseseca)
        print("SUCCESSFULLY CHANGED SECURITY ANSWER")
        time.sleep(1)
        settings()
    elif settingin.upper() == "[PASS]":
        verifypass = input("WHAT IS YOUR PASSWORD (L to Leave): ")
        if verifypass.upper() == "L":
            settings()
            return
        encryption.decryptpass()
        while verifypass != encryption.finaldepass:
            print("INCORRECT PASSWORD")
            time.sleep(1)
            verifypass = input("WHAT IS YOUR PASSWORD (L to Leave): ")
        newpass = input("NEW PASSWORD: ")
        encryption.encryptpass(newpass)
        print("SUCCESSFULLY CHANGED PASSWORD")
        time.sleep(1)
        settings()
    elif settingin.upper() == "[MK]":
        verifymk = input("WHAT IS YOUR MASTER KEY (L to Leave): ")
        if verifymk.upper() == "L":
            settings()
            return
        while int(verifymk) != encryption.masterkey:
            print("INCORRECT")
            time.sleep(1)
            verifymk = input("WHAT IS YOUR MASTER KEY (L to Leave): ")
        with open("hash.txt", "r") as passhash:
            passwa = passhash.read().strip()
        depassed = encryption.decryptpass()
        denotes = encryption.decryptnotes()
        deseca = encryption.decryptsa()
        newmk = random.randint(1, len(passwa)) * round(time.time())
        encryption.masterkey = int(newmk)
        encryption.encryptpass(depassed)
        encryption.encryptseca(deseca)
        encryption.encryptnotes(denotes)
        print("THIS IS YOUR NEW MASTER KEY, DO NOT LOSE IT: " + str(encryption.masterkey))
        time.sleep(1)
        settings()
    elif settingin.upper() == "[LEAVE]":
        os()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        settings()


def os():
    gettime()
    print("PYOS VERSION 10")
    print("MADE BY PYCROSOFT")
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
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        os()

    
    
