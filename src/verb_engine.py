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
        pass

    def conjugate(self, verb, tense):
        """
        Conjugates given verb to the provided tense.

        args:
            verb (String): Given verb.
            tense (String): Given tense.
        """
        res = self.engine.conjugate(verb)

        if res is None:
            print(f"Conjugation failed on {verb}. Please make sure the inputted verb is in the spanish dictionary.")
            return


        if tense not in translations:
            print("Invalid tense, choose one of the following:")
            for k in translations.keys():
                print(k)
        else:
            verb_dict = res[translations[tense][0]][translations[tense][1]]
            
            try:
                for k,v in verb_dict.items():
                    print(k, v)
            except(AttributeError):
                print(verb_dict)