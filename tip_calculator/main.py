"""
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

Write your code below this line 👇
"""


def calculate_bill(bill, patrons, tip):
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / patrons
    final_amount = round(bill_per_person, 2)
    print(f"Each person should pay: ${final_amount}, and the tip is ${total_tip_amount}")


if __name__ == "__main__":
    print("Welcome to the tip calculator.")
    bill = float(input("What was the total bill? $"))
    patrons = int(input("How many people to split the bill? "))
    tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    calculate_bill(bill, patrons, tip)