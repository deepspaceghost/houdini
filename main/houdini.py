import argparse
# import datetime
# import json
import logging
import os
# import shutil
# import sys

print("Setting up logging...")
log_path = os.path.join(os.getcwd(), "logs/prometheus.log")
if not os.path.isdir("logs"):
    print("Logging directory not found.")
    print("Creating logging directory...")
    log_dir_path = os.path.join(os.getcwd(), "logs")
    os.mkdir(log_dir_path)
    f = open(log_path, "x")
    f.close()

elif not os.path.exists(log_path):
    f = open(log_path, "x")
    f.close()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=log_path)

logger = logging.getLogger()


def ascii(butt_key):
    """
    """

    print("Checking number...")
    logger.info("Checking number...")
    if butt_key > 1114111 or butt_key < 0:
        print("What does Solaris want from us?")
        logger.info("What does Solaris want from us?")
        print("{0} is either not within range, or is not an integer.".format(butt_key))
        logger.info("{0} is either not within range, or is not an integer.".format(butt_key))
        print("To continue, try a number between 0 and 1,114,111.")
        logger.info("To continue, try a number between 0 and 1,114,111.")

    else:
        print("Converting integer...")
        logger.info("Converting integer...")
        print(chr(butt_key))
        logger.info(chr(butt_key))


def main():
    """
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--ascii",
                        action="store",
                        nargs=1,
                        help="Usage: ./prometheus.py --ascii [butt_key]",
                        dest="ascii_args")

    args = parser.parse_args()

    if args.ascii_args:
        butt_key = int(args.ascii_args[0])
        ascii(butt_key)


# def create_record(input1, output1):
#     """
#     """

#     print("Creating record...")
#     logger.info("Creating record...")
#     dt = datetime.datetime.now()
#     record = {"timestamp": dt, "input": {"input1": input1}, "output": {"output1": output1}}
#     with open("record.json", "w") as write_file:
#         json.dump(record, write_file)


if __name__ == "__main__":
    """
    """

    main()
