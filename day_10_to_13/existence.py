import os
import time
import bitcoin
import gambling

def verifyfiles():
    moneytxt = ""
    bitcointxt = ""
    print("LOADING FILES")
    time.sleep(1)
    if not os.path.exists("money.txt"):
        moneytxt = "fail"
        print("ERROR - money.txt EITHER DOSEN'T EXIST OR FAILED TO LOAD")
    elif not os.path.exists("btc.txt"):
        bitcointxt = "fail"
        print("ERROR - btc.txt EITHER DOSEN'T EXIST OR FAILED TO LOAD")
    else:
        moneytxt = "exists"
        bitcointxt = "exists"
        print("IMPORTING TXT FILES SUCCESSFUL")
    bp = bitcoin.ping()
    gp = gambling.ping()
    if bp and gp and moneytxt == "exists" and bitcointxt == "exists":
        print("5/5 FILES SUCCESSFULLY IMPORTED")
    else:
        print("ERROR - FILES FAILED TO LOAD")

def verifybalance():
    with open("money.txt", "r") as balance:
        money = balance.read()
    if not money:
        with open("money.txt", "w") as add:
            add.write("1000")
        print("NEW USERS GET $1,000 AS A GAMBLING HEAD START. USE IT WISELY.")
    else:
        print("WELCOME BACK, FRIEND.")

