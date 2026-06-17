import random
from random import *
class Dice:
    def __init__(self,sides):
        self.sides =sides


    def roll(self):
        random_number = random.randint(1,6)
        return random_number