"""
1. Create a greeting for your program.

2. Ask the user for the city that they grew up in.

3. Ask the user for the name of a pet.

4. Combine the name of their city and pet and show them their band name.

5. Make sure the input cursor shows on a new line:
"""


if __name__ == "__main__":
    print("Welcome to the Band Name Generator.")
    city = input("What's name of the city you grew up in?\n")
    pet = input("What's the name of a pet you know?\n")
    print(f"Your band name could be {city} {pet}")
