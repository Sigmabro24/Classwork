def main():
    print(multiply_two(multiply_two(1,3),6))
    print(add_two(4.6,3))
    print(subtract_two(2.5,3))
    print(divide_two(6.0,3))


def multiply_two(first,second):
    return first*second

def add_two(first,second):
    return first+second

def subtract_two(first,second):
    return first-second

def divide_two(first,second):
   return first/second



if __name__ == '__main__':
    main()