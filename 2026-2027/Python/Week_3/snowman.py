import random

words = ["sponge","bong","ping","smile","rival","bathroom","wisdom","doom"]
secret_word = random.choice(words)
length = len(secret_word)
processing = []
for i in range(length):
    processing += "_"

print(processing)

wrong_guess = 0
while wrong_guess < 8 and str(processing) != secret_word:
    guess = input("Please guess a letter: ")
    if guess in secret_word:
        for j in range(length):
            if guess == secret_word[j]:
                processing[j] = guess
                print(processing)
            if processing==secret_word:
                print("You guessed the word")
    else:
        wrong_guess +=1