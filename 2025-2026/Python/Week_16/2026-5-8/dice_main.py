import random


def main():

    from dice import Dice
    from random import randint
    roll_dice = Dice(6)

    print(roll_dice)
    print(random.randint(1, 6))


if __name__ == '__main__':
    main()







