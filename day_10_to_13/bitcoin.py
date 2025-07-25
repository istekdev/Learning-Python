import time
import random
import gambling

def ping():
    return "exists"

def home():
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
        buy()
    elif btcin.upper() == "[SELL]":
        sell()
    elif btcin.upper() == "[MINE]":
        mine()
    elif btcin.upper() == "[WALLET]":
        wallet()
    elif btcin.upper() == "[LEAVE]":
        gambling.options()
    else:
        print("ERROR - DOES NOT EXIST")
        time.sleep(1)
        home()

def price():
    market = 100000
    multiplier = random.random() * (20.0 - 10.0) + 10.0
    mprice = market * float(multiplier)
    marketprice = float(mprice)
    return marketprice

def wallet():
    with open("btc.txt", "r") as balance:
        rbalance = balance.read()
    if float(rbalance) == float(0):
        print("BALANCE: 0 BTC")
        time.sleep(1)
        home()
    elif float(rbalance) > 0:
        print("BALANCE: " + str(rbalance) + " BTC")
        time.sleep(1)
        home()

def mine():
    guess = 0
    nonce = random.randint(1, 1000000)
    starting = time.time()
    with open("money.txt", "r") as b:
        balance = b.read()
    with open("money.txt", "r") as bank:
        bankr = bank.read()
    if float(bankr) < 200:
        print("ERROR - YOU DO NOT HAVE ENOUGH MONEY TO MINE")
        time.sleep(1)
        home()
    else:
        with open("money.txt", "w") as take:
            equ = float(balance) - 200
            take.write(str(equ))
            print("TRANSACTION COMPLETED - STARTING MINER...")
    while guess != nonce:
        guess = random.randint(1, 1000000)
        print("MINING - CURRENT GUESS: " + str(guess))
        if time.time() - starting > 120:
            print("FAILED TO SOLVE A BLOCK - EXITING...")
            break
    with open("btc.txt", "r") as balance:
        bbb = balance.read()
        if not bbb:
            with open("btc.txt", "w") as add:
                add.write("3.125")
            print("YOU JUST WON 3.125 BTC - ADDING TO YOUR WALLET...")
            time.sleep(1)
            home()
        elif float(str(bbb)) > 0:
            with open("btc.txt", "w") as addb:
                eq = float(bbb) + 3.125
                addb.write(str(eq))
                print("YOU JUST WON 3.125 BTC - ADDING TO YOUR WALLET...")
                time.sleep(1)
                home()

def buy():
    currentprice = price()
    print("CURRENT PRICE: $" + str(currentprice))
    time.sleep(1)
    buyin = input("HOW MUCH DO YOU WANT TO BUY? (L to Leave): ")
    if buyin.upper() == "L":
        home()
    with open("money.txt", "r") as balance:
        rb = balance.read()
    with open("btc.txt", "r") as btcb:
        btcba = btcb.read().strip()
    if float(rb) < float(buyin):
        print("ERROR - YOU DO NOT HAVE ENOUGH MONEY")
        time.sleep(1)
        buy()
    if not btcba:
        btcba = 0
        with open("btc.txt", "w") as add:
            equation11 = float(rb) / int(currentprice)
            add.write(str(equation11))
        print("YOU JUST BOUGHT " + str(equation11) + " BTC")
        time.sleep(1)
        home()
    else:
        with open("btc.txt", "w") as add:
            equation = float(buyin) / int(currentprice)
            equation2 = float(btcba) + float(equation)
            add.write(str(equation2))
        with open("money.txt", "w") as take:
            eqq = float(buyin) * float(currentprice)
            eq1 = float(rb) - float(eqq)
        print("YOU JUST BOUGHT " + str(eq1) + " BTC")
        time.sleep(1)
        home()

def sell():
    currentprice = price()
    print("CURRENT PRICE: $" + str(currentprice))
    time.sleep(1)
    sellin = input("HOW MUCH DO YOU WANT TO SELL? (L to Leave): ")
    if sellin.upper() == "L":
        home()
    with open("money.txt", "r") as balance:
        rb = balance.read()
    with open("btc.txt", "r") as btcb:
        btcba = btcb.read()
    if float(sellin) > float(btcba):
        print("ERROR - YOU DO NOT HAVE ENOUGH BTC")
        time.sleep(1)
        buy()
    if not float(btcba):
        btcba = 0
        with open("money.txt", "w") as add:
            equation = float(sellin) * float(currentprice)
            add.write(str(equation))
        with open("btc.txt", "w") as sell:
            equation = float(btcba) - float(sellin)
            sell.write(str(equation))
        print("YOU JUST SOLD " + str(sellin) + " BTC FOR $" + str(equation))
        time.sleep(1)
        home()
    else:
        with open("money.txt", "w") as add:
            equation = float(sellin) * float(currentprice)
            equation2 = float(rb) + float(equation)
            add.write(str(equation2))
        with open("btc.txt", "w") as sell:
            equation = float(btcba) - float(sellin)
            sell.write(str(equation))
        print("YOU JUST SOLD " + str(sellin) + " BTC FOR $" + str(equation2))
        time.sleep(1)
        home()


