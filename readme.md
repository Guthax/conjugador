![logo](/docs/img/logo.png)

`Conjugador` is a simple verb conjugation command-line tool.


# Usage
```usage: Conjugador [-h] [-t TENSES [TENSES ...]] verb

Conjugates verb into given tenses

positional arguments:
  verb                  The verb to be conjugated.

options:
  -h, --help            show this help message and exit
  -t TENSES [TENSES ...], --tenses TENSES [TENSES ...]
                        the specified verb should be conjugated to.When not specified, all tenses are used.`
```

NOTE: Right now, this tool is developed to only support spanish.


# Installation
1. Clone this report
2. Run `pip install -r requirements.txt` (I recommend using a virtual env)
3. Run `./src/main.py *verb* -t [tenses]
4. For tests, add project folder to PYTHONPATH and run `python -m unittest` in tests folder.

# Contribution
Read contributions documentation in docs folder.

Note: Program is in very early development.