import time
import random
import bitcoin

def ping():
    return "exists"

def roulette():
    bet = input("PLACE YOUR BET (Or L to Leave): ")
    with open("money.txt", "r") as checkb:
        cr = checkb.read()
    if bet.upper() == "L":
        options()
    while float(cr) < float(bet):
        print("YOU DO NOT HAVE ENOUGH")
        time.sleep(1)
        roulette()
    color = ""
    spinner = random.randint(1, 10)
    uchoose = input("BLACK OR RED: ")
    if spinner in [2, 4, 6, 8, 10]:
        color = "BLACK"
    elif spinner in [1, 3, 5, 7, 9]:
        color = "RED"
    for countdown in range(5, 0, -1):
        print(countdown)
        time.sleep(1)
    print("YOUR BET WAS ON " + uchoose)
    time.sleep(1)
    print("THE COLOR SELECTED IS " + color)
    if uchoose == color:
        with open("money.txt", "r") as readb:
            balance = readb.read()
        addwins = (float(bet) * 2) + float(balance)
        with open("money.txt", "w") as addwinnings:
            addwinnings.write(str(addwins))
        print("YOU JUST WON $" + str(bet))
        time.sleep(1)
        playagain = input("PLAY AGAIN? (Y/N): ")
        if playagain.upper() == "Y":
            roulette()
        elif playagain.upper() == "N":
            options()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            roulette()
    else:
        with open("money.txt", "r") as readb:
            balance = readb.read()
        addloss = float(balance) - int(bet)
        with open("money.txt", "w") as addlosses:
            addlosses.write(str(addloss))
        print("YOU JUST LOST $" + str(bet))
        time.sleep(1)
        playagain = input("PLAY AGAIN? (Y/N): ")
        if playagain.upper() == "Y":
            roulette()
        elif playagain.upper() == "N":
            options()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            roulette()

def guess():
    bet = input("PLACE YOUR BET (Or L to Leave): ")
    with open("money.txt", "r") as checkb:
        cr = checkb.read()
    if bet.upper() == "L":
        options()
    while float(cr) < float(bet):
        print("YOU DO NOT HAVE ENOUGH")
        time.sleep(1)
        guess()
    winning = random.randint(1, 50)
    guessin = input("GUESS A NUMBER FROM 1-50: ")
    for counts in range(5, 0, -1):
        print(counts)
        time.sleep(1)
    print("YOUR NUMBER: " + str(guessin))
    time.sleep(1)
    print("WINNING NUMBER: " + str(winning))
    if int(guessin) == winning:
        with open("money.txt", "r") as readb:
            balance = readb.read()
        addwins = (float(bet) * 2) + balance
        with open("money.txt", "w") as addwinnings:
            addwinnings.write(str(addwins))
        print("YOU JUST WON $" + str(addwins))
        time.sleep(1)
        playagain = input("PLAY AGAIN? (Y/N): ")
        if playagain.upper() == "Y":
            guess()
        elif playagain.upper() == "N":
            options()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            guess()
    elif int(guessin) != winning:
        with open("money.txt", "r") as readb:
            balance = readb.read()
        addloss = float(balance) - int(bet)
        with open("money.txt", "w") as addlosses:
            addlosses.write(str(addloss))
        print("YOU JUST LOST $" + str(bet))
        time.sleep(1)
        playagain = input("PLAY AGAIN? (Y/N): ")
        if playagain.upper() == "Y":
            guess()
        elif playagain.upper() == "N":
            options()
        else:
            print("ERROR - DOES NOT EXIST")
            time.sleep(1)
            guess()
    else:
        print("ERROR - GOES NOT EXIST")
        time.sleep(1)
        guess()

def menu():
    print("BITCOIN MENU")
    print("---")
    print("[BUY] - Buy BTC")
    print("[SELL] - Sell BTC")
    print("[MINE] - Mine BTC (At $200)")
    print("[WALLET] - Bitcoin Wallet")
    print("[LEAVE] - Leave")
    time.sleep(1)
    btcin = input(">> ")
    if btcin.upper() == "[BUY]":
        bitcoin.buy()
    elif btcin.upper() == "[SELL]":
        bitcoin.sell()
    elif btcin.upper() == "[MINE]":
        bitcoin.mine()
    elif btcin.upper() == "[WALLET]":
        bitcoin.wallet()
    elif btcin.upper() == "[LEAVE]":
        options()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        menu()
        

def options():
    print("GAMBLEPY MENU")
    print("---")
    print("[ROULETTE] - Roulette")
    print("[GUESS] - Guess the Number")
    print("[BTC] - Bitcoin Menu")
    time.sleep(1)
    gambler = input(">> ")
    if gambler.upper() == "[ROULETTE]":
        roulette()
    elif gambler.upper() == "[GUESS]":
        guess()
    elif gambler.upper() == "[BTC]":
        menu()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        options()
