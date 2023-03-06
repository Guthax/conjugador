from mlconjug3.mlconjug import Conjugator
from src.translation_dict import translations

class VerbEngine:
    """
    Class handling all verb conjugations.
    """
    def __init__(self, language):
        """
        Initializes mlconjug object to the given language.

        args:
            language (String): Abbreviation of the language(i.e nl, eng, esp)
        """
        self.mlconjug3_engine = Conjugator(language)
        self.language = language
        pass

    def conjugate(self, verb, tenses):
        """
        Conjugates verb into a list of tenses.

        args:
            verb (String): verb to conjugate.
            tenses [String]: tenses to conjugate verb into.
        """


class VerbEngineML(VerbEngine):
    """
    Verb engine extension which using Machine learning.
    """

    def __init__(self, language):
        super().__init__(language)

    def _create_conjugation_dictionary_for_single_tense(self, conjugations, tense):
        """
        Creates conjugation dictionary for single tense.

        args:
            conjugations (Dict): Full verb conjugation dictionary from mlconjug3,
            containing all conjugations for all.
            tense (String): Tense to extract from conjugation dictionary.
        """
        verb_dict = conjugations[translations[tense][0]][translations[tense][1]]

        conjugation_dict = {}
        try:
            for key, value in verb_dict.items():
                conjugation_dict[key] = value
        except AttributeError:
            # Could be that its a gerund or participant and the conjugation is given as a string.
            conjugation_dict = {"Todo": verb_dict}

        return conjugation_dict


    def create_conjugation_dictionary_for_tense_list(self, verb, tenses):
        """
        Conjugates given verb to the provided tense.

        args:
            verb (String): Given verb.
            tenses [String]: Tenses to conjugate verb to.
        """

        conjugations = self.mlconjug3_engine.conjugate(verb)
        if conjugations is None:
            print(f"Conjugation failed on {verb}. \
                  Please make sure the inputted verb is in the spanish dictionary.")
            return

        full_conjugation_dictionary = {}
        if tenses is None:
            for available_tense in translations:
                conjugation_dictionary = self._create_conjugation_dictionary_for_single_tense(conjugations, available_tense)
                full_conjugation_dictionary[available_tense] = conjugation_dictionary
        else:
            for tense in tenses:
                if tense in translations:
                    conjugation_dictionary = self._create_conjugation_dictionary_for_single_tense(conjugations, tense)
                    full_conjugation_dictionary[tense] = conjugation_dictionary
                else:
                    print(f"{tense} is not a valid tense in the language {self.language}.")
        return full_conjugation_dictionary

    def print_conjugation_dictionary(self, conjugation_dictionary):
        """
        Prints a conjugation dictionary.

        args:
            conjugation_dictionary (Dict): Conjugation dictionary to print.
        """
        for tense in conjugation_dictionary:
            print(f"--------[{tense}]--------")
            for key, value in conjugation_dictionary[tense].items():
                print(key, value)
            print("--------------------------")
