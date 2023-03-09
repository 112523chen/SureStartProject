import streamlit as st
import pickle
import tensorflow as tf
from PIL import Image
import sklearn

from helper import getPrediction


model = tf.keras.models.load_model('./model')
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
logo = Image.open('rumorradar-logo.png')

st.set_page_config(
    page_title="RumorRadar",
    page_icon=logo,
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("<h1 style='text-align: center; color:mediumslateblue;font-family:Monospace'>Fake News Detection</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(logo, width=250)

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color:mediumslateblue; font-family:Monospace; font-size:25px'>Did you know that fake news causes 67% of the American population confusion? There is no need to be confused with RumorRadar "
            "because it can detect fake news.</h6>", unsafe_allow_html=True)


st.markdown("<h1 style='text-align: center; color:mediumslateblue; font-family:Monospace; font-size:25px'>Try it out here: 👇 </h6>", unsafe_allow_html=True)


title = st.text_input('Enter News Title:', '')
text = st.text_input('Enter News Content:', '')
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write('')

with col2:
    st.write('')

with col3:
    button = st.button("Fake or Real?")

with col4:
    st.write('')

with col5:
    st.write('')

if title != "" and text != "" and button:

    guess = getPrediction(title, text, vectorizer, model)
    st.header(f"The text is {guess} news")

with st.sidebar:
    with st.expander("About our goal"):
        st.markdown(
            "<h1 style='text-align: center; color:mediumslateblue; font-family:Monospace; font-size:15px'> Our goal is to reduce the spread of misinformation in social media platforms. </h6>",
            unsafe_allow_html=True)
