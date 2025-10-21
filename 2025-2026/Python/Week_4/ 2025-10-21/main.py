def main():
    pass

name = input("Enter your name: ")
print(name)
print(len(name))
print(type(name))
age = (input("Enter your age: "))
print(age)
print(len(age))
age = int(age)
print(type(age))
float_age = float(age)
print(type(float_age))
int_age = int(float_age)
print(type(int_age))
planning_on_graduating_on_time = True
print(type(planning_on_graduating_on_time))
#cant len a bool
bool_to_age = int(planning_on_graduating_on_time)
print(bool_to_age)


if __name__ == '__main__':
    main()