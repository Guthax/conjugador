import unittest
try:
    import context
except ModuleNotFoundError:
    import test.context   
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
        Tests the creation of a conjugation dictionary for a single verb.
        """
        verb = "tener"
        tense = "present"

        conjugations = self.engine.mlconjug3_engine.conjugate(verb)
        actual = self.engine._create_conjugation_dictionary_for_single_tense(conjugations, "present")
        expected = {"yo": "tengo",
                         "tú": "tienes", 
                         "él": "tiene", 
                         "nosotros": "tenemos", 
                         "vosotros": "tenéis", 
                         "ellos":"tienen"}
        self.assertEqual(expected, actual)
