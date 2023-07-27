import random


def split_names(names):
    names_list = names.split(", ")
    return names_list


def choose_random_name(names):
    random_name = random.randint(0, len(names) - 1)
    return names[random_name]


def main():
    print("Welcome to the Banker's Roulette!")
    names_string = input("Give me everybody's names, separated by a comma. \n")
    names_list = split_names(names_string)
    print(f"{choose_random_name(names_list)} is going to pay for the meal today!")
    return 0


if __name__ == "__main__":
    main()