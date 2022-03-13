import streamlit as st
import pickle
import pandas as pd
import numpy as np

movies_pickle = pickle.load(open('pickle/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_pickle)
movies_list = movies['title']
genre_sim = pickle.load(open('pickle/genre_sim.pkl', 'rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index.values
    distances = genre_sim[movie_index]
    recommend_list = distances.argsort()[:, ::-1][0][1:11]
    recommended_movies = []

    for i in recommend_list:
        recommended_movies.append(movies_list.iloc[i])
    return recommended_movies

st.title('MovieRecSys Demo')

selected_movie_name = st.selectbox(
    'Search the movie you likes.',
    movies_list
)

if st.button('Recommend'):
    df = recommend(selected_movie_name)
    st.write(f"Recommendation based on genres of '{selected_movie_name}'")
    for i in df:
        st.write(i)