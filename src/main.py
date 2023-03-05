import sys
import argparse

from verb_engine import VerbEngine


def __configure__arg_parser():
    """
    Configures the parser object for the command line arguments.
    """
    parser = argparse.ArgumentParser(
                    prog = 'Conjugador',
                    description = 'Conjugates verb into given tenses',
                    epilog = 'Text at the bottom of help')

    parser.add_argument('verb', type=str, help="The verb to be conjugated.")
    parser.add_argument('-t', '--tenses', nargs='+',
                        help="the specified verb should be conjugated to." \
                         "When not specified, all tenses are used.")
    return parser

if __name__ == "__main__":
    parser = __configure__arg_parser()
    args = parser.parse_args()
    engine = VerbEngine("es")
    engine.conjugate(args.verb, args.tenses)
