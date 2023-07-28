row_1 = ["⬜️", "⬜️", "⬜️"]
row_2 = ["⬜️", "⬜️", "⬜️"]
row_3 = ["⬜️", "⬜️", "⬜️"]
map = [row_1, row_2, row_3]
print(f"{row_1}\n{row_2}\n{row_3}")


def set_position(position):
    position = position.split(" ")
    position = "".join(position)
    if position == "11":
        row_1[0] = "X"
    elif position == "12":
        row_1[1] = "X"
    elif position == "13":
        row_1[2] = "X"
    elif position == "21":
        row_2[0] = "X"
    elif position == "22":
        row_2[1] = "X"
    elif position == "23":
        row_2[2] = "X"
    elif position == "31":
        row_3[0] = "X"
    elif position == "32":
        row_3[1] = "X"
    elif position == "33":
        row_3[2] = "X"
    else:
        print("Invalid position.")
    return 0


def main():
    print("Welcome to Treasure Map!")
    position = input("Where do you want to put the treasure? ")
    set_position(position)
    print(f"{row_1}\n{row_2}\n{row_3}")
    return 0


if __name__ == "__main__":
    main()
