import argparse
import json
# import sys

"""
Project Title: Find the character of an ASCII code

Project Date: 01/17/2021

Project Description: Write a program that receives an ASCII
code (an integer between 0 and 127) and displays
its character. For example, if the user enters 97, the
program displays the character a.

Input: Enter an ASCII code: 69 [enter]

Input constraints: Is the input an integer? Between 0 and 127?

Compute
"""

# Current task(s): as of 1:39am, 1/25/2021, create tests for individual functions

# Output: The character is E

"""
git add *
git commit -m "some message"
git push origin dev
"""


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

    data = {"president": {"name": "Zaphod Beeblebrox", "species": "Betelgeusian"}}
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)

    parser = argparse.ArgumentParser()
    parser.add_argument("--voila",
                        action="store",
                        nargs=1,
                        help="Usage: ./houdini.py --voila [chango]",
                        dest="voila_args")

    args = parser.parse_args()

    chango = int(args.voila_args[0])
    if num_check(chango):
        voila(chango)
    else:
        print("For this trick, I require a number between 0 and 127.")
