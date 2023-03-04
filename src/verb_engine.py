from mlconjug3.mlconjug import Conjugator
from translation_dict import translations
class VerbEngine:
    def __init__(self, language):
        self.engine = Conjugator(language)
        pass

    def conjugate(self, verb, tense):
        res = self.engine.conjugate(verb)

        for k,v in res[translations[tense][0]][translations[tense][1]].items():
            print(k, v)


    def print_value(self):
        print("test")