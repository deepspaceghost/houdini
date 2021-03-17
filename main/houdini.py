import argparse
import datetime

from ascii_magician import ASCII_Magician
from lumberjack import Logger
from storage_worker_factory import Historian_Factory


class EXECUTION_History():
    """
    """

    def get_timestamp():
        """
        """

        ct = datetime.datetime.now()
        return ct.strftime("%Y/%m/%d-%H:%M:%S")

    def get_execution_input(butt_key):
        """
        """

        input1 = {}
        input1["input"] = {}
        input1["input"]["butt_key"] = butt_key
        return input1


    def get_execution_output(chango):
        """
        """

        output1 = {}
        output1["output"] = {}
        output1["output"]["chango"] = chango
        return output1


    def store_execution(timestamp, input1, output1):
        """
        """

        historian_factory = Historian_Factory()
        json_historian = historian_factory.build_historian("json")
        json_historian.create_execution_record(timestamp, input1, output1)
        json_historian.print_execution_record()
        json_historian.write_execution_history()
        json_historian.print_execution_history()


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
        chango = magician.voila(butt_key, lumberjack.get_logger())
        execution_history = EXECUTION_History()
        timestamp = execution_history.get_timestamp()
        input1 = execution_history.get_execution_input(butt_key)
        output1 = execution_history.get_execution_output(chango)
        execution_history.store_execution(timestamp, input1, output1)


if __name__ == "__main__":
    """
    """

    main()
