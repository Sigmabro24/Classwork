import random
print("Three, Two, One, Shoot!")
user_input = input("Choose between: lizard, spock, rock, paper, scissor: ")
words = ["rock","paper","scissor","lizard","spock"]
random_item = random.choice(words)
print(random_item)
rules = {"rock":("lizard","scissor"),"scissor":("paper","lizard"),"paper":("spock","rock"),"lizard":("spock","paper"),"spock":("scissor","rock")}
if random_item in rules[user_input]:
    print("You win!")
elif random_item == user_input:
    print("You tied")
else:
    print("You lose")