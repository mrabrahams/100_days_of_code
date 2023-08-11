"""
Instructions

The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.

Welcome to the secret auction program.
What is your name?: Angela

What's your bid?: $123

Are there any other bidders? Type 'yes' or 'no'.
yes

If there are other bidders, the screen should clear, so you can pass your phone to the next person.
If there are no more bidders, then the program should display the name of the winner and their winning bid.

The winner is Elon with a bid of $55000000000

Use your knowledge of Python dictionaries and loops to solve this challenge.
My console doesn't clear!

This will happen if you’re using an IDE other than replit (e.g., VSCode, PyCharm etc). Similar to how we used the
"random" module previously, in this project we will use the "replit" module. The clear() function is available here
via the replit module without any extra configuration.

I’ll cover how to use PyCharm and import modules on Day 15. That said, you can write your own clear() function or
configure your IDE like so:

Solution
"""
import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


bids = {}
highest_bid = {}


def clear():
    os.system("clear")
    return


def highest_bidder():
    current_high = 0
    for bid in bids:
        if bids[bid] > current_high:
            highest_bid.clear()
            current_high = bids[bid]
            highest_bid[bid] = bids[bid]
    return highest_bid


def auction_bids(bidders):
    i = 0
    while i < bidders:
        name = input(f'What is the name of bidder {i + 1}? ')
        bid = int(input(f'What is the {i + 1} bid? '))
        bids[name] = bid
        i += 1
    return bids


def main():
    print("Welcome to the silent auction!")
    num_bidders = int(input("How many bidders are there? "))
    auction_bids(num_bidders)
    winning_bid = (highest_bidder())
    print(f"The highest bidder is {highest_bid}!")
    return


if __name__ == "__main__":
    main()