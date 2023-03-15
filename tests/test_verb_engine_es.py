import unittest
from conjugador.exceptions.ConjugationFailedException import ConjugationFailedException
from conjugador.exceptions.TenseNotFoundException import TenseNotFoundException

from conjugador.verb_engine import VerbEngineML


class TestConjugations(unittest.TestCase):
    """
    Tests creation of conjugation dictionaries for Spanish.

    Dont test mlconjugs inner workings. Assume they are correct.
    """
    def setUp(self):
        self.engine = VerbEngineML("es")
        pass

    def test_create_conjugation_dictionary_for_single_tense(self):
        """
        Tests the creation of a conjugation dictionary for a single verb in a single tense.
        """
        verb = "tener"
        tense = "present"

        conjugations = self.engine.mlconjug3_engine.conjugate(verb)

        reflexive = self.engine._check_if_verb_reflexive(verb)
        self.assertFalse(reflexive)

        actual = self.engine._create_conjugation_dictionary_for_single_tense(conjugations, False, "present")
        expected = {"yo": "tengo",
                         "tú": "tienes", 
                         "él": "tiene", 
                         "nosotros": "tenemos", 
                         "vosotros": "tenéis", 
                         "ellos":"tienen"}
        self.assertEqual(expected, actual)

    def test_create_conjugation_dictionary_for_single_tense_reflexive(self):
        """
        Tests the creation of a conjugation dictionary for a single reflexive verb in a single tense.
        """
        verb = "irse"
        tense = "present"
        conjugations = self.engine.mlconjug3_engine.conjugate(verb)
        reflexive = self.engine._check_if_verb_reflexive(verb)

        self.assertTrue(reflexive)

        actual = self.engine._create_conjugation_dictionary_for_single_tense(conjugations,reflexive, "present")
        expected = {"yo me": "voy",
                         "tú te": "vas", 
                         "él se": "va", 
                         "nosotros nos": "vamos", 
                         "vosotros os": "vais", 
                         "ellos se":"van"}
        self.assertEqual(expected, actual)

    def test_create_conjugation_dictionary_for_multiple_tenses(self):
        verb = "tener"
        tenses = ["present", "imperfect", "preterite", "participant"]

        conjugations = self.engine.mlconjug3_engine.conjugate(verb)
        actual = self.engine.create_conjugation_dictionary_for_tense_list(verb, tenses)
        expected = {"present": {"yo": "tengo",
                                "tú": "tienes", 
                                "él": "tiene", 
                                "nosotros": "tenemos", 
                                "vosotros": "tenéis", 
                                "ellos":"tienen"},
                    "imperfect": {"yo": "tenía",
                                "tú": "tenías", 
                                "él": "tenía", 
                                "nosotros": "teníamos", 
                                "vosotros": "teníais", 
                                "ellos":"tenían"},
                    "preterite": {"yo": "tuve",
                                "tú": "tuviste", 
                                "él": "tuvo", 
                                "nosotros": "tuvimos", 
                                "vosotros": "tuvisteis", 
                                "ellos":"tuvieron"},
                    "participant": {"All forms": "tenido"}}
        self.assertEqual(expected, actual)

    def test_create_conjugation_dictionary_for_all_tenses(self):
        """
        This tests needs to be updated everytime a new verb is added to the spanish conjugation functionality.
        """
        verb = "tener"

        conjugations = self.engine.mlconjug3_engine.conjugate(verb)
        actual = self.engine.create_conjugation_dictionary_for_tense_list(verb, None)
        expected = {"present": {"yo": "tengo",
                                "tú": "tienes", 
                                "él": "tiene", 
                                "nosotros": "tenemos", 
                                "vosotros": "tenéis", 
                                "ellos":"tienen"},
                    "imperfect": {"yo": "tenía",
                                "tú": "tenías", 
                                "él": "tenía", 
                                "nosotros": "teníamos", 
                                "vosotros": "teníais", 
                                "ellos":"tenían"},
                    "preterite": {"yo": "tuve",
                                "tú": "tuviste", 
                                "él": "tuvo", 
                                "nosotros": "tuvimos", 
                                "vosotros": "tuvisteis", 
                                "ellos":"tuvieron"},
                    "future": {"yo": "tendré",
                                "tú": "tendrás", 
                                "él": "tendrá", 
                                "nosotros": "tendremos", 
                                "vosotros": "tendréis", 
                                "ellos":"tendrán"},
                    "conditional": {"yo": "tendría",
                                "tú": "tendrías", 
                                "él": "tendría", 
                                "nosotros": "tendríamos", 
                                "vosotros": "tendríais", 
                                "ellos":"tendrían"},
                    "gerund": {"": "teniendo"},
                    "participant": {"All forms": "tenido"}}
        self.assertEqual(expected, actual)

    def test_create_conjugation_dictionary_conjugation_failed(self):
        """
        This tests needs to be updated everytime a new verb is added to the spanish conjugation functionality.
        """
        verb = "tener123"
        with self.assertRaises(ConjugationFailedException):
            self.engine.create_conjugation_dictionary_for_tense_list(verb, None)

    def test_create_conjugation_dictionary_invalid_tense(self):
        """
        This tests needs to be updated everytime a new verb is added to the spanish conjugation functionality.
        """
        verb = "tener"
        tenses = ["faultytense"]
        with self.assertRaises(TenseNotFoundException):
            self.engine.create_conjugation_dictionary_for_tense_list(verb, tenses)