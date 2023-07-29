"""
Instructions

You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

    The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89

In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output

The highest score in the class is: 91

"""


def highest_score(scores):
    highest = 0
    for score in scores:
        if score > highest:
            highest = score
    return highest


def main():
    scores = input("Input a list of student scores ").split(', ')
    scores = [int(score) for score in scores]
    highest = highest_score(scores)
    print(f"The highest score in the class is: {highest}")


if __name__ == "__main__":
    main()