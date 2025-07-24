import time
import random

marketprice = float(0)

def ping():
    return "exists"

def price():
    global marketprice
    market = 100000
    multiplier = random.random() * (20.0 - 10.0) + 10.0
    mprice = market * float(multiplier)
    marketprice = float(mprice)

def wallet():
    with open("btc.txt", "r") as balance:
        rbalance = float(balance.read())
    if not rbalance:
        print("BALANCE: 0 BTC")
        time.sleep(1)
        menu()
    elif rbalance > 0:
        print("BALANCE: " + str(rbalance) + " BTC")
        time.sleep(1)
        menu()

def mine():
    guess = 0
    nonce = random.randint(1, len(time.time()))
    with open("money.txt", "r") as bank:
        bankr = bank.read()
    if bankr < 200:
        print("ERROR - YOU DO NOT HAVE ENOUGH MONEY TO MINE")
        time.sleep(1)
        menu()
    else:
        with open("money.txt", "w") as take:
            equ = int(balance) - 200
            take.write(str(equ))
            print("TRANSACTION COMPLETED - STARTING MINER...")
    while guess != nonce:
        guess = random.randint(1, len(time.time()))
        print("MINING - CURRENT GUESS: " + guess)
    with open("btc.txt", "r") as balance:
        if not balance:
            with open("btc.txt", "w") as add:
                add.write("3.125")
                print("YOU JUST WON 3.125 BTC - ADDING TO YOUR WALLET...")
                time.sleep(1)
                menu()
        elif balance > 0:
            with open("btc.txt", "w") as addb:
                eq = float(balance) + 3.125
                addb.write(str(eq))
                print("YOU JUST WON 3.125 BTC - ADDING TO YOUR WALLET...")
                time.sleep(1)
                menu()

def buy():
    currentprice = marketprice
    print("CURRENT PRICE: $" + str(currentprice))
    time.sleep(1)
    buyin = input("HOW MUCH DO YOU WANT TO BUY? (L to Leave): ")
    if buyin.upper() == "L":
        menu()
    with open("money.txt", "r") as balance:
        rb = balance.read()
    with open("btc.txt", "r") as btcb:
        btcba = btcb.read()
    if int(buyin) > int(rb):
        print("ERROR - YOU DO NOT HAVE ENOUGH MONEY")
        time.sleep(1)
        buy()
    if not float(btcba):
        with open("btc.txt", "w") as add:
            equation = int(rb) / int(currentprice)
            add.write(str(equation))
            print("YOU JUST BOUGHT " + str(equation) + " BTC")
            time.sleep(1)
            menu()
    else:
        with open("btc.txt", "w") as add:
            equation = int(rb) / int(currentprice)
            equation2 = float(btcba) + float(equation)
            add.write(str(equation2))
            print("YOU JUST BOUGHT " + str(equation) + " BTC")
            time.sleep(1)
            menu()

def sell():
    currentprice = marketprice
    print("CURRENT PRICE: $" + str(currentprice))
    time.sleep(1)
    sellin = input("HOW MUCH DO YOU WANT TO SELL? (L to Leave): ")
    if sellin.upper() == "L":
        menu()
    with open("money.txt", "r") as balance:
        rb = balance.read()
    with open("btc.txt", "r") as btcb:
        btcba = btcb.read()
    if int(sellin) > int(rb):
        print("ERROR - YOU DO NOT HAVE ENOUGH BTC")
        time.sleep(1)
        buy()
    if not float(btcba):
        with open("money.txt", "w") as add:
            equation = int(sellin) * int(currentprice)
            add.write(str(equation))
            print("YOU JUST SOLD " + str(equation) + " BTC")
            time.sleep(1)
            menu()
    else:
        with open("money.txt", "w") as add:
            equation = int(sellin) * int(currentprice)
            equation2 = float(rb) + float(equation)
            add.write(str(equation2))
            print("YOU JUST SOLD " + str(equation) + " BTC")
            time.sleep(1)
            menu()

def menu():
    print("BITCOIN MENU")
    print("---")
    time.sleep(1)
    print("[BUY] - Buy BTC")
    print("[SELL] - Sell BTC")
    print("[MINE] - Mine BTC (At $200)")
    print("[WALLET] - Bitcoin Wallet")
    time.sleep(1)
    btcin = input(">> ")
    if btcin.upper() == "[BUY]":
        buy()
    elif btcin.upper() == "[SELL]":
        sell()
    elif btcin.upper() == "[MINE]":
        mine()
    elif btcin.upper() == "[WALLET]":
        wallet()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        menu()

while True:
    price()
    time.sleep(1)
