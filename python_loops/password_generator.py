"""
Instructions

The program will ask:

How many letters would you like in your password?

How many symbols would you like?

How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password.
Use your knowledge about Python lists and loops to complete the challenge.
Easy Version (Step 1)

Generate the password in sequence. If the user wants

    4 letters
    2 symbols and
    3 numbers

then the password might look like this:

fgdx$*924

You can see that all the letters are together.
All the symbols are together and all the numbers follow each other as well.
Try to solve this problem first.

Hard Version (Step 2)

When you've completed the easy version, you're ready to tackle the hard version.
In the advanced version of this project the final password does not follow a pattern.
So the example above might look like this:

x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different.
Solution to the Password Generator Project
"""

import random


def generate_letters(nr_letters):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chosen_letters = []
    for i in range(nr_letters):
        chosen_letters.append(random.choice(letters))
    return chosen_letters


def generate_symbols(nr_symbols):
    symbols = "!@#$%^&*()_+"
    chosen_symbols = []
    for i in range(nr_symbols):
        chosen_symbols.append(random.choice(symbols))
    return chosen_symbols


def generate_numbers(nr_numbers):
    numbers = "1234567890"
    chosen_numbers = []
    for i in range(nr_numbers):
        chosen_numbers.append(random.choice(numbers))
    return chosen_numbers


def generate_password(nr_numbers, nr_symbols, nr_letters):
    password = [generate_numbers(nr_numbers), generate_symbols(nr_symbols), generate_letters(nr_letters)]
    random.shuffle(password)
    password = "".join(password[0] + password[1] + password[2])
    password = "".join(random.sample(password, len(password)))
    print(f"Your password is: {password}")
    return 0


def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    generate_password(nr_numbers, nr_symbols, nr_letters)
    return 0


if __name__ == "__main__":
    main()
