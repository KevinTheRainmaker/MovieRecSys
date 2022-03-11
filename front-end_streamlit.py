import streamlit as st
import pickle
import pandas as pd

movies_pickle = pickle.load(open('movies_dict.pkl', 'rb'))
movies_list = pd.DataFrame(movies_pickle)['title'].values

st.title('MovieRecSys Demo')

option = st.selectbox(
    'Search the movie you likes.',
    movies_list
)