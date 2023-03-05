import re


def removeNewLine(text):
    return re.sub(r'\n', '', text)


def removeSpecialCharacters(text):
    return re.sub(r'[^\w\s]', '', text)


def transformGuess(x):
    if x == 0:
        return "Real"
    return "Fake"
