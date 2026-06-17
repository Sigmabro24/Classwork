import random
import statistics



class Dice:
    def __init__(self, sides: int):
        if 4 >= sides >= 100:
            raise ValueError("Value should be between 4 and 100")

        self.sides = sides
        self.history = []

    def roll(self):
        me= random.randint(1, self.sides)
        self.history.append(me)

    def roll_many(self, times):
        for times in times:
            self.roll()
        return self.history.append(times)

    def average(self):
        return print(statistics.mean(self.history))


def main():
    print(Dice(4))


if __name__ == '__main__':
    main()
