
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guess = input("Guess A Letter: ").lower()
#
# for x in range(0, len(chosen_word)):
#     chosen_word[x] = list(chosen_word)


# hangman = [''' '0', '|', '/', '\', '/', '\' ''']

for letter in chosen_word:
    if letter == guess:
        print(letter)

    else:
        print(chosen_word)
