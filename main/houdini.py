import argparse
from ascii_magician import ASCII_Magician
from lumberjack import Logger
# import datetime
# import json
# import shutil
# import sys


def main():
    """
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--voila",
                        action="store",
                        nargs=1,
                        help="Usage: ./houdini.py --voila [butt_key]",
                        dest="voila_args")

    args = parser.parse_args()

    if args.voila_args:
        butt_key = int(args.voila_args[0])
        magician = ASCII_Magician()
        lumberjack = Logger()
        magician.voila(butt_key, lumberjack.get_logger())


if __name__ == "__main__":
    """
    """

    main()
