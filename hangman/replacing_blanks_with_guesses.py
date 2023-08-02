"""
TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

"""
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "cat", "dog", "elephant", "giraffe", "lion", "mouse", "tiger", "wolf"]


def choose_word():
    chosen_word = random.choice(word_list)
    return chosen_word


def check_guess(chosen_word, guess, dashes):
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if dashes[position] == guess:
                print("You already guessed this letter.")
                return True
            if guess == chosen_word[position]:
                dashes[position] = guess
        return True
    else:
        print("Wrong guess.")
        return False


def display(chosen_word):
    display_inner = []
    for letter in chosen_word:
        display_inner.append("_")
    return display_inner


def display_hangman(lives):
    print(stages[lives])
    return 0


def game_loop(dashes, chosen_word):
    i = 0
    lives = 6
    display_hangman(lives)
    while i < 6:
        print(dashes)
        guess = input("Guess a letter: ").lower()
        if check_guess(chosen_word, guess, dashes) is True:
            if "_" not in dashes:
                print("Congratulations, you won!")
                break
            print("Correct guess.")
            print(f"You have {lives} guesses left.")
        else:
            lives -= 1
            i += 1
            if i == len(dashes):
                print("You lost.")
                break
            display_hangman(lives)
            print(f"You have {lives} guesses left.")
    return 0


def main():
    print("Welcome to Hangman!")
    chosen_word = choose_word()
    dashes = display(chosen_word)
    game_loop(dashes, chosen_word)
    return 0


if __name__ == "__main__":
    main()