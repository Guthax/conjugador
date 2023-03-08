import argparse
from conjugador.config.supported_languages import supported_languages
from conjugador.verb_engine import VerbEngineML

def __configure__arg_parser():
    """
    Configures the parser object for the command line arguments.
    """
    arg_parser = argparse.ArgumentParser(
                    prog = 'Conjugador',
                    description = 'Conjugates verb into given tenses',
                    epilog = 'Text at the bottom of help')

    arg_parser.add_argument('verb', type=str, help="The verb to be conjugated.")
    arg_parser.add_argument('-t', '--tenses', nargs='+',
                        help="the specified verb should be conjugated to." \
                         "When not specified, all tenses are used.")
    return arg_parser

if __name__ == "__main__":
    parser = __configure__arg_parser()
    args = parser.parse_args()

    language = "es"
    if language not in supported_languages:
        print("Not a valid language")
    else:
        engine = VerbEngineML(language)
        conjugations = engine.create_conjugation_dictionary_for_tense_list(args.verb, args.tenses)
        engine.print_conjugation_dictionary(conjugations)
