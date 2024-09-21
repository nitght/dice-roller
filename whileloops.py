import random

def rollDice(sides):
    return random.randint(1, sides)

number = 6

while True:
    print(rollDice(number))
    roll_again = input("Would you like to roll again? (Yes/No?): ").lower()
    if roll_again != 'yes':
        break
