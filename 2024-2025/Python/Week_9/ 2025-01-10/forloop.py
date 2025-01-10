#Abdullahi
#1/10/25

first_name = str(input("Please enter your first name:"))
last_name = str(input("Please enter your last name:"))

age = int(input("Please enter your age:"))
print()
print("Hello",first_name,last_name)
print("You are",age,"years old,","so you should be about this tall")
for x in range(age):
    print("*")