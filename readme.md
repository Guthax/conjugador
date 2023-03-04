# Conjugador
While learning spanish, I constantly needed to look up verb conjugations on esfacil.eu. This is a great site but required an internet connection and navigation to the site each time was annoying. This is the reason I created conjugador, a *very* simple command line tool to conjugate verbs. 

The application usses the mlconjug3 library, which is an opensource machine learning library for language conjugtaion. Originally, I wanted to use a REST API but this requires both an internet connection and an API key.

To develop:
1. Clone this repo
2. run pip install -r requirements.txt
3. python main.py <verb> <tense>
4. Happy coding