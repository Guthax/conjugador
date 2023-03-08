import unittest

from conjugador.verb_engine import VerbEngineML


class TestConjugations(unittest.TestCase):
    """
    Tests creation of conjugation dictionaries.
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
