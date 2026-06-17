def main():
    salary = float(input("Please tell me a reasonable yearly salary you expect to make after high school:"))
    tax = salary * 0.23
    total = (salary - tax) / 26

    print(f"Based on your {salary} yearly salary minus a tax of 23%, you would take home {total} every two weeks.")
    print(f"The total tax you paid for the year would be {tax}")


if __name__ == '__main__':
    main()

