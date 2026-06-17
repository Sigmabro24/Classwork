import random

class Dice:
    def __init__(self,sides:int):
        self.sides:int = sides



    def roll(self):
        dice = random.randint(1,self.sides)
        return dice

    # def __str__(self):
    #     return f'{}'








def main():


    dice = Dice(6)
    roll = dice.roll()
    dice2 = Dice(12)
    roll2 = dice2.roll()

    dice3 = Dice(4)
    roll3 = Dice.roll(dice3)
    dice4 = Dice(8)
    roll4 = Dice.roll(dice4)

    dice5 = Dice(20)
    roll5 = Dice.roll(dice5)
    dice6 = Dice(10)
    roll6 = Dice.roll(dice6)


    print(roll)
    print(roll2)
    print(roll3)
    print(roll4)
    print(roll5)
    print(roll6)









if __name__ == '__main__':
    main()