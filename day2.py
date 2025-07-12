import time

print("WELCOME TO MY PYTHON LEARNING PORTAL")
time.sleep(1)
num = input("WHAT IS YOUR BIRTHDAY?")
bday = int(num)

if bday == 9162010:
    pss = input("WHAT IS YOUR CAT'S BREED?")
    if pss == "Calico":
        print("ACCESS GRANTED")
        time.sleep(1)
        current = time.time()
        local = time.localtime(current)
        stamp = time.strftime("%H:%M:%S", local)
        print("CURRENT TIME: " + f"{stamp}")
        time.sleep(1)
        sound = input("WHAT SOUND DOES YOUR CAT MAKE?")
        if sound == "Meow":
            class Cat:
                def __init__(self, cat):
                    self.cat = cat
                def meow(self):
                    print(f"{self.cat} is the sound a cat makes.")
            catsfx = Cat(sound)        
            catsfx.meow()
        else:
            print("WRONG, ALWAYS WRONG")
    else:
        print("NOT A CALICO = NOT MY CAT")

  # This utilizes class, if, else, print, variables, time, import, input, and int
