import random
print("Three, Two, One, Shoot!")
user_input = input("Choose between: Lizard, Spock, Rock, Paper, Scissor: ")
words = ["Rock","Paper","Scissor","Lizard","Spock"]
random_item = random.choice(words)
print(f"Your opponent has picked: {random_item}")
if user_input == "Rock" and random_item == "Paper":
    print("You lose because paper covers rock")
elif user_input == "Rock" and random_item == "Lizard":
    print("You win because rock crushes lizard")
elif user_input == "Rock" and random_item == "Scissor":
    print("You win because rock crushes scissors")
elif user_input == "Rock" and random_item == "Spock":
    print("You lose because spock vaporizes rock")
elif user_input == "Scissor" and random_item == "Paper":
    print("You win because scissors cut paper")
elif user_input == "Scissor" and random_item == "Spock":
    print("You lose because spock smashes scissors")
elif user_input == "Scissor" and random_item == "Rock":
    print("You lose because rock crushes scissors")
elif user_input == "Scissor" and random_item == "Lizard":
    print("You win because scissor decapitates lizard")
elif user_input == "Paper" and random_item == "Rock":
    print("You win because paper covers rock")
elif user_input == "Paper" and random_item == "Scissor":
    print("You lose because scissor cuts paper")
elif user_input == "Paper" and random_item == "Lizard":
    print("You lose because lizard eats paper")
elif user_input == "Paper" and random_item == "Spock":
    print("You win because paper disproves spock")
elif user_input == "Spock" and random_item == "Paper":
    print("You lose because paper disproves spock")
elif user_input == "Spock" and random_item == "Rock":
    print("You win because spock vaporizes rock")
elif user_input == "Spock" and random_item == "Scissor":
    print("You win because spock smashes scissors")
elif user_input == "Spock" and random_item == "Lizard":
    print("You lose because lizard poisons spock")
elif user_input == "Lizard" and random_item == "Scissor":
    print("You lose because scissors decapitates lizard")
elif user_input == "Lizard" and random_item == "Rock":
    print("You lose because rock crushes lizard")
elif user_input == "Lizard" and random_item == "Paper":
    print("You win because lizard eats paper")
elif user_input == "Lizard" and random_item == "Spock":
    print("You win because lizard poisons spock")
elif user_input == random_item:
    print("You tie")
else:
    print("Please enter a valid input")