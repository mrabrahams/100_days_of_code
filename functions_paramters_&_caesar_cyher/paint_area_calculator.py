"""
Instructions

You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5

                           = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

IMPORTANT: Notice the name of the function and parameters must match those on line 13 for the code to work.
Example Input

test_h = 3
test_w = 9

Example Output

You'll need 6 cans of paint.

Hint

1. To round up a number:

https://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python

2. Make sure you name your function/parameters the same as when it's called on the last line of code.
Test Your Code

Check your code is doing what it is supposed to. When you're happy with your code, click submit to check your solution.
Solution
"""
import math


def greeting():
    print("Welcome to the Paint Area Calculator!")
    return 0


def collect_height():
    test_h = int(input("What's the height of the wall? "))
    return test_h


def collect_width():
    test_w = int(input("What's the width of the wall? "))
    return test_w


def calculate_cans(test_h, test_w):
    number_of_cans = math.ceil((test_h * test_w) / 5)
    return number_of_cans


def main():
    greeting()
    test_h = collect_height()
    test_w = collect_width()
    number_of_cans = calculate_cans(test_h, test_w)
    print(f"You'll need {number_of_cans} cans of paint.")
    return 0

b []
.MMA
if __name__ == "__main__":
    main()