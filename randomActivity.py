import random

def rollDice(sides):
    return random.randint(1, sides)

number = int(input("hou meney sides"))

print(rollDice(number))