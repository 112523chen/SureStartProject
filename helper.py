import re


def removeNewLine(text):
    return re.sub(r'\n', '', text)


def removeSpecialCharacters(text):
    return re.sub(r'[^\w\s]', '', text)


def transformGuess(x):
    if x == 0:
        return "Real"
    return "Fake"


def getPrediction(title, text, vectorizer, model):
    text = removeNewLine(text)
    text = removeSpecialCharacters(text)
    new_data = title + " " + text
    new_data = vectorizer.transform([new_data]).toarray()
    guess = transformGuess(model.predict([new_data]).round())
    return guess
