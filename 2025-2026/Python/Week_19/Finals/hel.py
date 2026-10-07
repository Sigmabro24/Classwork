import random

guess = int(input("Please input a number between 1 and 100: "))
secret_number = random.randint(1, 100)
guess_number = 1

loop = True
if guess == secret_number:
    loop = False
    print("You guessed the number!")
while loop:

    if 100 >= guess > secret_number :
        guess_lower = guess - 1
        guess = int(input(f"Please input a lower number between 1 and {guess_lower}: "))
        guess_number += 1
        guess_lower = guess - 1
    elif 0 < guess < secret_number:
        guess_higher = guess + 1
        guess = int(input(f"Please input a higher number between {guess_higher} and 100: "))
        guess_number += 1
    elif 0 > guess:
        guess = int(input("Please guess a number between 1 and 100"))
        guess_number += 1
    elif guess > 100:
        guess = int(input("Please guess a number between 1 and 100"))
    elif guess == secret_number:
        loop = False
        print("You guessed the number!")
        print(f"You guessed {guess_number} times")



# For the continuous guessing idea I feel like you could do it with a loop that will continuously ask you to guess again until you guess it correctly by watching if the value matches