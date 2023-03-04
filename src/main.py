from verb_engine import VerbEngine
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please use the program as: conjugador <verb> <time>")
        print("time can be: present, imperfect, preterite or future")
    else:
        engine = VerbEngine("es")
        engine.conjugate(sys.argv[1], sys.argv[2])