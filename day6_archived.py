import random
import time

def rng():
    rand = random.randint(1, 100)
    rand2 = time.time()
    finality = (rand + rand2) * rand
    print("YOUR RANDOM NUMBER IS: " + str(round(finality)))
    
def lottery():
    guess = []
    nums = []
    while len(nums) < 5:
        nums.append(random.randint(1, 50))
    return nums
    
def miner():
    nonce = random.randint(1, 100000)
    mine = 0
    while mine != nonce:
        mine = random.randint(1, 100000)
        print("MINING: " + str(mine)) # Aparrently mine isn't a string
    print("BOOM ,YOU JUST EARNED A DAY OFF")
        
def encoder():
    ugi = input("INPUT A SENTENCE YOU WOULD LIKE TO CONVERT: ")
    encoded = "" # Prevents variable from being used before being defined
    for chars in ugi:
        encoded += str(ord(chars))
    print("RESULT: " + encoded)    
    
def currenttime():
    epoch = time.time()
    local = time.localtime(epoch)
    result = time.strftime("%H:%M:%S", local)
    print(f"THE TIME IS: {result}")
    
class PYDAY:
    def __init__(self, day):
        self.day = day
    
    def sayit(self):
        print(f"THIS IS CURRENTLY DAY {self.day} OF LEARNING PYTHON")
    
print("WELCOME TO MY PYTHON LEARNING PORTAL")
time.sleep(1)
password = input("WHAT IS THE PASSWORD: ")

while password != "mybooty165":
    print("INCORRECT")
    time.sleep(1)
    password = input("WHAT IS THE PASSWORD: ")

secq1 = input("WHAT BREED IS YOUR CAT: ")

while secq1 != "Calico":
    print("INCORRECT")
    time.sleep(1)
    secq1 = input("WHAT BREED IS YOUR CAT: ")
    
secq2 = input("NAME OF YOUR FIRST GIRLFRIEND: ")

while secq2 != "Camila":
    print("INCORRECT")
    time.sleep(1)
    secq2 = input("NAME OF YOUR FIRST GIRLFRIEND: ")
    
print("ACCESS GRANTED")    
time.sleep(1)
print("PASSWORD LENGTH: " + str(len(password)) + "/10")
time.sleep(1)
print("SECURITY QUESTION 1: " + secq1 + " MATCHES " + "\"Calico\"")
time.sleep(1)
print("SECURITY QUESTION 2: " + secq2 + " MATCHES " + "\"Camila\"")
time.sleep(1)
print("WELCOME")
time.sleep(1)
print("[RNG] - RANDOM NUMBER GENERATOR")
print("[LOT] - LOTTERY")
print("[MINE] - PSEUDO-MINE")
print("[EN] - ENCODE ASCII")
print("[TIME] - CURRENT TIME")
print("[DAY] - CURRENT DAY OF LEARNING PYTHON")
time.sleep(1)
choose = input(">> ")

if choose == "RNG":
    rng()
elif choose == "LOT":
    print("WELCOME TO PYBALL!")
    time.sleep(1)
    guess1 = input("GUESS 1: ")
    guess2 = input("GUESS 2: ")
    guess3 = input("GUESS 3: ")
    guess4 = input("GUESS 4: ")
    guess5 = input("GUESS 5: ")
    time.sleep(1)
    guess = [int(guess1), int(guess2), int(guess3), int(guess4), int(guess5)]
    nums = lottery()
    print("WINNING NUMBERS: ", nums)
    time.sleep(1)
    print("YOUR NUMBERS: ", guess)
    if nums == guess:
        print("YOU JUST WON A DAY LONG BREAK FROM LEARNING PYTHON")
    else:
        print("KEEP TRYING BOZO")
elif choose == "MINE":
    miner()
elif choose == "EN":
    encoder()
elif choose == "TIME":
    currenttime()
elif choose == "DAY":
    you = PYDAY(6)
    you.sayit()
else:
    print("THAT DOSEN'T EXIST")
    
# This uses concepts I learned from days 1-5: elif, else, if, for, in, while, print, input, str, time, random, len, def, ord, class, and round
