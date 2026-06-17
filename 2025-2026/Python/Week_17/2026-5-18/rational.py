class Rational:
    def __init__(self,numerator:int,denominator:int):
        self.numerator:int = numerator
        self.denominator:int = denominator

    def __str__(self):
        return f"{self.numerator:}/{self.denominator}"

    def __add__(self,other):
        total = self.numerator * other.denominator + self.denominator  * other.numerator
        true_denominator = self.denominator * other.denominator
        return Rational(total, true_denominator)





def main():
    fraction = Rational(numerator=1,denominator=7)
    fraction2 = Rational(numerator=5,denominator=8)
    fraction3 = Rational(numerator=6,denominator=7)
    print(fraction.numerator)
    print(fraction.denominator)
    print(fraction2.numerator)
    print(fraction2.denominator)
    print(fraction3)
    print(fraction2 + fraction)

if __name__ == '__main__':
    main()