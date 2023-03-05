from mlconjug3.mlconjug import Conjugator
from translation_dict import translations

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
        self.engine = Conjugator(language)
        self.language = language
        pass

    def _print_verb_in_tense(self, conjugations, tense):
        verb_dict = conjugations[translations[tense][0]][translations[tense][1]]

        print(f"----------[{tense}]----------")
        try:
            for key, value in verb_dict.items():
                print(key, value)
        except AttributeError:
            # Could be that its a gerund or participant and the conjugation is given as a string.
            print(verb_dict)
        print("-------------------------------")

    def conjugate(self, verb, tenses):
        """
        Conjugates given verb to the provided tense.

        args:
            verb (String): Given verb.
            tense (String): Given tense.
        """

        conjugations = self.engine.conjugate(verb)
        if conjugations is None:
            print(f"Conjugation failed on {verb}. \
                  Please make sure the inputted verb is in the spanish dictionary.")
            return

        if tenses is None:
            for available_tense in translations:
                self._print_verb_in_tense(conjugations, available_tense)
        else:
            for tense in tenses:
                if tense in translations:
                    self._print_verb_in_tense(conjugations, tense)
                else:
                    print(f"{tense} is not a valid tense in the language {self.language}.")
