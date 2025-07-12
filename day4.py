import time

firstpass = input("WHAT IS YOUR PASSWORD: ")
time.sleep(1)
gettime = time.time()
entropyone = input("TYPE IN ANY AMOUNT OF NUMBERS: ")
onemum = int(entropyone)
time.sleep(1)
finalentropy = input("TYPE IN A PHRASE: ")

def doentropy():
    entropyfirst = 0 # Somehow ensures that the for loop uses all characters, without this, it would only use the very last character
    for words in firstpass: # Loops though firstpass, for means selecting something and in means where it's selected
        entropyfirst = ord(words) # It converts the characters to ASCII code
    entropysec = 0
    for characters in finalentropy:
        entropysec = ord(characters)
    finality = (entropyfirst + entropysec) * gettime
    output = print(round(finality)) # Using round, I don't get an endless decimal

doentropy()

# This utilizes known concepts (def, print, time, import, input, and int), and uses new concepts like (for, in, ord, and round)
