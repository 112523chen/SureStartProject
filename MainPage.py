import streamlit as st
import pickle

from helper import removeNewLine, removeSpecialCharacters, transformGuess

model = pickle.load(open('deepLearningModel.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(
    page_title="Face News Detection Demo"
)

st.title('Face News Detection Demo')

title = st.text_input('Enter Title Sample', '')
text = st.text_input('Enter Text Sample', '')

if title is not "" and text is not "":

    text = removeNewLine(text)
    text = removeSpecialCharacters(text)
    new_data = title + " " + text
    new_data = vectorizer.transform(new_data)
    guess = model.predict(new_data)

    st.header(f"The article sample is {transformGuess(guess)} news")
