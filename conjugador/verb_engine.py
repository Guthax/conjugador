from abc import ABC, abstractmethod
from conjugador.config.tense_translations_ml import translations
from conjugador.config.reflexive_verbs import reflexive_verb_ending
from conjugador.config.reflexive_verbs import reflexive_verb_persons
from conjugador.exceptions.ConjugationFailedException import ConjugationFailedException
from conjugador.exceptions.TenseNotFoundException import TenseNotFoundException
from mlconjug3.mlconjug import Conjugator

class VerbEngine(ABC):
    """
    Class handling all verb conjugations.
    """
    def __init__(self, language):
        """
        Initializes mlconjug object to the given language.

        args:
            language (String): Abbreviation of the language(i.e nl, eng, es)
        """
        self.mlconjug3_engine = Conjugator(language)
        self.language = language


    def _check_if_verb_reflexive(self, verb) -> bool:
        """
        Checks if given verb is reflexive in the given language.

        args:
            verb (String): Verb
        
        Returns:
            bool: If the verb is reflexive.
        """
        if self.language in reflexive_verb_ending:
            if verb.endswith(reflexive_verb_ending[self.language]):
                return True
        
        return False

    @abstractmethod
    def _create_conjugation_dictionary_for_single_tense(self, conjugations,reflexive, tense):
        """
        Creates conjugation dictionary for single tense.

        args:
            conjugations (Dict): Full verb conjugation dictionary from mlconjug3,
            containing all conjugations for all.
            reflexive (bool): Is the verb reflexive.
            tense (String): Tense to extract from conjugation dictionary.
        """

    @abstractmethod
    def create_conjugation_dictionary_for_tense_list(self, verb, tenses):
        """
        Conjugates given verb to the provided tense.

        args:
            verb (String): Given verb.
            tenses [String]: Tenses to conjugate verb to.
        """

    @abstractmethod
    def print_conjugation_dictionary(self, conjugation_dictionary):
        """
        Prints a conjugation dictionary.

        args:
            conjugation_dictionary (Dict): Conjugation dictionary to print.
        """

class VerbEngineML(VerbEngine):
    """
    Verb engine extension which using Machine learning.
    """

    def __init__(self, language):
        super().__init__(language)
        self.translations = translations[language]

    def _create_conjugation_dictionary_for_single_tense(self, conjugations,reflexive, tense):
        """
        Creates conjugation dictionary for single tense.

        args:
            conjugations (Dict): Full verb conjugation dictionary from mlconjug3,
            containing all conjugations for all.
            tense (String): Tense to extract from conjugation dictionary.
        """
        verb_dict = conjugations[self.translations[tense][0]][self.translations[tense][1]]
        conjugation_dict = {}
        try:
            for person, conjugation in verb_dict.items():
                if reflexive:
                    conjugation_dict[f"{person} {reflexive_verb_persons[self.language][person]}"] = conjugation
                else:
                    conjugation_dict[person] = conjugation
        except AttributeError:
            # Could be that its a gerund or participant and the conjugation is given as a string.
            conjugation_dict = {"All forms": verb_dict}

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
            raise ConjugationFailedException(f"Conjugation failed on {verb}. \
                  Please make sure the inputted verb is in the spanish dictionary.")

        full_conjugation_dictionary = {}
        reflexive_verb = self._check_if_verb_reflexive(verb)
        if tenses is None:
            for available_tense in self.translations:
                conjugation_dictionary = self._create_conjugation_dictionary_for_single_tense(conjugations,reflexive_verb, available_tense)
                full_conjugation_dictionary[available_tense] = conjugation_dictionary
        else:
            for tense in tenses:
                if tense in self.translations:
                    conjugation_dictionary = self._create_conjugation_dictionary_for_single_tense(conjugations,reflexive_verb, tense)
                    full_conjugation_dictionary[tense] = conjugation_dictionary
                else:
                    raise TenseNotFoundException(f"{tense} is not a valid tense in the language {self.language}.")
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
