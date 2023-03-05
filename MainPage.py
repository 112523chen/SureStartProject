import streamlit as st
import pickle

from helper import getPrediction

model = pickle.load(open('deepLearningModel.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(
    page_title="Face News Detection Demo"
)

st.title('Face News Detection Demo')

title = st.text_input('Enter Title Sample', '')
text = st.text_input('Enter Text Sample', '')

if title is not "" and text is not "":

    guess = getPrediction(title, text, vectorizer, model)

    st.header(f"The article sample is {guess} news")
