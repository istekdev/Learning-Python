import random
import time

def rng():
    nums = []
    guess = []
    while len(nums) < 5: # Aparrently, this checks whether there are 5 numbers in the list
        nums.append(random.randint(1, 50))
    return nums # Forgot to learn this, returns value back for later use.

print("WELCOME TO THE PYTHONBALL!")
time.sleep(1)
print("INPUT 5 NUMBERS, ALL FROM 1-50")
time.sleep(1)
guess1 = input("GUESS 1: ")
guess2 = input("GUESS 2: ")
guess3 = input("GUESS 3: ")
guess4 = input("GUESS 4: ")
guess5 = input("GUESS 5: ")
guess = [guess1, guess2, guess3, guess4, guess5] # These are strings, int() aparrently can't be used
nums = rng()
time.sleep(1)
print("WINNING NUMBERS: ", nums) # Fun fact, adding strings to messages means you have to use commas instead of +
time.sleep(1)
print("YOUR NUMBERS: ", guess)

if nums == guess:
    print("YOU JUST WON A DAY OFF OF LEARNING PYTHON!")
else:
    print("WRONG, YOU HAVE A LONG WAY TO GO")

# Could not use for, range, in, str, int, ord, round, elif, and class
# Used known concepts like if, else, print, time, import, def, len, and while
# Used new concepts like append, return, and random
