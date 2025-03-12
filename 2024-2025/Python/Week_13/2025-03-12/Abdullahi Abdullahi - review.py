# Please leave 2 comments below, one with your name, and the other with
# today's date
#Abdullahi Yahye
#3/12/25




# Create a variable called random_input and use it to get some text from the
# user.
random_input = input("Enter some text:")



# If you want to find out what type a variable is in Python, what method do
# you use?

type(random_input)



# Use the appropriate method to display the type of the random_input
# variable. Put a comment below the code with the output you get from
# running the code.

print(type(random_input))
#<class 'str'>


# Please create a variable called name and get the name from the user and
# store it in the variable.  The variable should be a string.

name = input("Enter your name:")



# Use Python to output proof that your variable name is a string

print(type(name))
#<class 'str'>

# Please create a variable called age and get the name from the user and
# store it in the variable.  The variable should be an integer.

age = int(input("Enter your age:"))


# Use Python to output proof that your variable age is an integer

print(type(age))
#<class 'int'>

# Please create a variable called gpa and get the gpa from the user and
# store it in the variable.  The variable should be a float.

gpa = float(input("Enter your GPA:"))

# Use Python to output proof that your variable gpa is a float

print(type(gpa))
#<class 'float'>

# Use Python to output a one line complete sentence with your name, age and
# GPA.

print("Your name is",name,"your age is",age,"and your gpa is",gpa)