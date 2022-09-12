from multiprocessing.sharedctypes import Value
import random

sideAmount = int(input("Please input how many sides your dice has: "))
# sideAmount = 5

class Die:
    
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def roll(self):
        return random.randrange(1, self.sides) 



# sixSided = Die("Die 1", random.randint())
# print(sixSided.roll())


die = Die("Die 1: ", sideAmount)

def rollAll(die):
    count = 0
    yahtzee = 0
    value = 0
    newRoll = value

    while (count < 5):
        count = count + 1
        value = die.roll()

        if value == newRoll:
            yahtzee = yahtzee + 1
            if yahtzee == 5:
                print("Yahtzee!")
        
        else: print(value)

rollAll(die)
