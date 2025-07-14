import time

def entropy(rng1, rng2):
    rngsub = ""
    for nums in range(100):
        rngsub += str(nums)
    entropy1 = 0
    for characters in rng2:
        entropy1 += ord(characters)
    rngint = int(rngsub)
    finality = (entropy1 + rng1) * rngint
    print(f"RNG: {round(finality)}")   
print("WELCOME TO THE PYTHON LEARNING PORTAL - DAY 5")
time.sleep(1)
mypass = input("PASSWORD: ")
psw = "ILoveCalicos"
while mypass != psw:
    mypass = input("TRY AGAIN: ")

print("ACCESS GRANTED")
time.sleep(1)
print("PASSWORD MATCHES, LENGTH MATCHES: " + str(len(psw)) + "/12")
time.sleep(1)
choice = input("CHOOSE ACTION: [RNG/SPAM]")
if choice == "RNG":
    rng1 = time.time()
    rng2 = psw
    entropy(rng1, rng2)
elif choice == "SPAM":
    while True:
        print("SPAMMING")
else:
    print("ERR - CHOICE NOT FOUND")        
    
# Used known concepts like def, else, if, elif, time, round, for, in, print, ord, input, str, int, and import
# New concepts like range, len, and while loops
    
            
