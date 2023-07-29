import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇


# create a list of the game images called game_images
game_images = [rock, paper, scissors]


def compare(user_choice, computer_chosen_name):
    if user_choice == computer_chosen_name:
        print("It's a draw.")
    elif user_choice == 0 and computer_chosen_name == 2:
        print("You win!")
    elif user_choice == 2 and computer_chosen_name == 1:
        print("You win!")
    elif user_choice == 1 and computer_chosen_name == 0:
        print("You win!")
    else:
        print("You lose.")
    return 0


def computer_choice(user_choice):
    computer_chosen_sign = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_chosen_sign])
    compare(user_choice, computer_chosen_sign)


def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number!")
        main()
    else:
        print(game_images[user_choice])
        computer_choice(user_choice)
    return 0


if __name__ == "__main__":
    main()