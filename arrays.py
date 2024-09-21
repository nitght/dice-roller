import random

def rollDice(sides):
    return random.randint(1, sides)

acceptable = ["yes","se","ok","yea","of course"]
number = 100

while True:
    result = rollDice(number)
    print(result)
    if result == 100:
        print("your a winner")
    roll_again = input("Would you like to roll again? (Yes/No?): ").lower()
    if roll_again not in acceptable:
        break