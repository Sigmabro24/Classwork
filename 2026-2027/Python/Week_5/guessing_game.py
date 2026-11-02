import random

user_range_a = int(input("Please input the first range value: "))
user_range_b = int(input("Please input the second range value: "))
secret_number = random.randint(user_range_a, user_range_b)
guess_number = int(input("How many guesses do you want? "))
guess = int(input(f"Please guess a number between {user_range_a} and {user_range_b}: "))
guess_checker = 1
print(f"{guess_checker} guesses used")

guess_ora = True
if guess_checker > guess_number:
    guess_ora = False

while guess != secret_number and guess_checker <= guess_number: #for the longest time I used or but then realized that and makes more sense because I am checking if the number isn't right and the guesses have been all used
    if guess > secret_number:
        int(input(f"Please guess a lower number between {user_range_a} and {user_range_b}: "))
    elif guess < secret_number:
        int(input(f"Please guess a higher number between {user_range_a} and {user_range_b}: "))
    guess_checker = guess_checker +1
    print(f"{guess_checker} guesses used")



if guess == secret_number:
    print("You guessed the number!")
if guess_checker > guess_number:
    print(f"You did not guess the number within {guess_number} guesses")
