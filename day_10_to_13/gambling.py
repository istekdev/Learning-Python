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
    while cr < bet:
        print("YOU DO NOT HAVE ENOUGH")
        time.sleep(1)
        roulette()
    color = ""
    spinner = random.randint(1, 10)
    uchoose = input("BLACK OR RED: ")
    if spinner in [2, 4, 6, 8, 10]:
        color = "BLACK"
    elif spinner == [1, 3, 5, 7, 9]:
        color = "RED"
    if uchoose == color:
        with open("money.txt", "r") as readb:
            balance = readb.read()
        addwins = float(balance) * 2
        with open("money.txt", "w") as addwinnings:
            addwinnings.write(str(addwins))
        print("YOU JUST WON $" + str(addwins))
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
        print("YOU JUST LOST $" + str(addloss))
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
    while cr < bet:
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
        addwins = float(balance) * 2
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
        print("YOU JUST LOST $" + str(addloss))
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

def options():
    print("GAMBLEPY MENU")
    print("---")
    time.sleep(1)
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
        bitcoin.menu()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        options()
