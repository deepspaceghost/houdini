# import argparse
import click
import datetime

from ascii_magician import ASCII_Magician
from lumberjack import Logger
from historian_factory import Historian_Factory


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
    # json_historian.write_execution_history()
    json_historian.print_execution_history()


@click.group()
def cli():
    """
    Houdini takes an ASCII code and returns an the corresponding ASCII character.
    """
    pass


@cli.command()
@click.option("--butt-key", default=100, help="ASCII code to convert to ASCII character.")
def voila(butt_key):
    """
    Voila takes an ASCII code and returns an the corresponding ASCII character.
    """
    # click.echo("The value of butt_key is: {}".format(butt_key))

    # parser = argparse.ArgumentParser()
    # parser.add_argument("--voila",
    #                     action="store",
    #                     nargs=1,
    #                     help="Usage: ./houdini.py --voila [butt_key]",
    #                     dest="voila_args")

    # args = parser.parse_args()

    # if args.voila_args:
    # butt_key = int(args.voila_args[0])
    magician = ASCII_Magician()
    lumberjack = Logger()
    chango = magician.voila(butt_key, lumberjack.get_logger())
    click.echo(chango)
    timestamp = get_timestamp()
    input1 = get_execution_input(butt_key)
    output1 = get_execution_output(chango)
    store_execution(timestamp, input1, output1)


# if __name__ == "__main__":
#     """
#     """

#     main()
