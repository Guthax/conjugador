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

## Examples
```
python conjugador.py tener  : Get conjugations in all supported tenses for verb tener
python conjugador.py tener -t present  :  Get conjugations for the present tense for verb tener
python conjugador.py tener -t present future gerund  :  Get conjugations for the present, future and gerund tense for verb tener

python conjugador.py irse : Get conjugations in all supported tenses for reflexive verb irse
python conjugador.py irse -t present : Get conjugations in present tense for reflexive verb irse
python conjugador.py irse -t present future gerund : Get conjugations in present, future and gerund tense for reflexive verb irse

```

# Installation
1. Clone this report
2. `cd` into project dir
2. Run `pip install -r requirements.txt` (I recommend using a virtual env)`
4. Run `python conjugador.py <verb> <tenses>` or `python -m unittest discover` for running tests.

# Contribution
Read contributions documentation in docs folder.

Note: Program is in very early development.
