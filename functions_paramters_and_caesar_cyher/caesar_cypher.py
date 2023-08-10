import math


alphabet = "abcdefghijklmnopqrstuvwxyz"


def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(text, key):
    return encrypt(text, -key)


def main():
    print("Welcome to the Caesar Cypher!")
    print("What do you want to do?")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input("Enter your choice: "))
    message = input("Enter your text: ").lower()
    key = int(input("Enter your key: "))
    if choice == 1:
        print(encrypt(message, key))
    elif choice == 2:
        print(decrypt(message, key))
    else:
        print("Invalid choice.")
        main()


if __name__ == "__main__":
    main()