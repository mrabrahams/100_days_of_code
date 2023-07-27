import random


def main():
    random_int = random.randint(0, 1)

    if random_int == 0:
        print("Tails")
    else:
        print("Heads")

    return 0


if __name__ == "__main__":
    main()
