"""
Program to take in a number from user and return if prime or not.

"""


def prime_checker(number):
    if number <= 2:
        return str(number) + " is a prime number."

    for i in range(2, int(number/2) + 1):
        if number % i == 0:
            return str(number) + " is not a prime number."

    return str(number) + " is a prime number."


def main():
    n = int(input("Enter the number you want checked: "))
    print(prime_checker(number=n))


if __name__ == "__main__":
    main()