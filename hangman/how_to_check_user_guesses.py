"""
#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

"""

import random

word_list = ["aardvark", "baboon", "camel", "cat", "dog", "elephant", "giraffe", "lion", "mouse", "tiger", "wolf"]


def choose_word():
    chosen_word = random.choice(word_list)
    return chosen_word


def check_guess(chosen_word, guess):
    if guess in chosen_word:
        return True
    else:
        return False


def main():
    print("Welcome to Hangman!")
    chosen_word = choose_word()
    guess = input("Guess a letter: ").lower()
    print(check_guess(chosen_word, guess))
    return 0


if __name__ == "__main__":
    main()