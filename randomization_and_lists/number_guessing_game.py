import random


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    number = random.randint(1, 100)
    attempts = set_difficulty(difficulty)
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            return 0
        elif guess > number:
            print("Too high.")
            attempts -= 1
        else:
            print("Too low.")
            attempts -= 1
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return 0
        else:
            print("Guess again.")
    return 0


def set_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    else:
        return 5


if __name__ == "__main__":
    main()