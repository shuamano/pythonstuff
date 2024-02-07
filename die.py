import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))
        
my_die = Die(20)
my_die.roll_die()