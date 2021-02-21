import sys

"""
Project Title: Find the character of an ASCII code

Project Date: 01/17/2021

Project Description: Write a program that receives an ASCII
code (an integer between 0 and 127) and displays
its character. For example, if the user enters 97, the
program displays the character a.
"""

# Input: Enter an ASCII code: 69 [enter]

# Input constraints: Is the input an integer? Between 0 and 127?

# Compute

"""
"""

# Current task(s): as of 1:39am, 1/25/2021, create tests for individual functions

# Output: The character is E


def num_check(chango):
    """
    """

    if chango > 127 or chango < 0:
        return False

    return True


def voila(chango):
    """
    """

    print("Voila!")
    print(chr(chango))


if __name__ == "__main__":
    """
    """

    print("And now, for my next trick, give me a number, between 0 and 127.")
    print("In exchange, I will make a letter appear in its place.")

    print(sys.argv)
    presto = sys.argv[2]

    try:
        chango = int(presto)

    except ValueError as err:
        print("INFO: Could not convert data into a integer.")
        print("DEBUG: {0}".format(err))

        exit()

    if num_check(chango):
        print("This number is within range!")
        voila(chango)
    else:
        print("This number is not within range!")
