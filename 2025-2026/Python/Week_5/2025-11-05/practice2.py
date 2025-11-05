def main():
    age = int(input("What is your age?"))
    if age < 18:
        print("Sorry you can not vote")
    elif age == 18:
        print("You can vote and you can be drafted")
    elif age >= 21:
        print("You can legally drink")
    elif age == 19 or 20:
        print("You are not allowed to drink yet")


if __name__ == '__main__':
    main()