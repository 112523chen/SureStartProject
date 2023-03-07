import streamlit as st
import pickle
import tensorflow as tf
import sklearn

from helper import getPrediction

model = tf.keras.models.load_model('./model')
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(
    page_title="Face News Detection Demo"
)

st.title('Face News Detection Demo')

title = st.text_input('Enter Title Sample', '')
text = st.text_input('Enter Text Sample', '')

if title != "" and text != "":

    guess = getPrediction(title, text, vectorizer, model)

    st.header(f"The article sample is {guess} news")
