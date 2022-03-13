from urllib import response
import streamlit as st
import pickle
import pandas as pd
import numpy as np

import requests

movies_pickle = pickle.load(open('pickle/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_pickle)
movies_list = movies['title']
genre_sim = pickle.load(open('pickle/genre_sim.pkl', 'rb'))

def fetch_poster(movie_index):
    movie_id = movies['id'][movie_index]
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=189e2f0ac7606d631dd67d62ef7f8811')
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']
    
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index.values
    distances = genre_sim[movie_index]
    recommend_list = distances.argsort()[:, ::-1][0][1:7]

    recommended_movies = []
    recommended_movies_posters = []
    
    for i in recommend_list:
        recommended_movies.append(movies.iloc[i].title)
        recommended_movies_posters.append(fetch_poster(i))
    return recommended_movies, recommended_movies_posters

st.title('MovieRecSys Demo')

selected_movie_name = st.selectbox(
    'Search the movie you likes.',
    movies_list
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    st.write(f"Recommendation based on genres of '{selected_movie_name}'")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.text(names[0])
        st.image(posters[0])
        st.text(names[3])
        st.image(posters[3])
        
    with col2:
        st.text(names[1])
        st.image(posters[1])
        st.text(names[4])
        st.image(posters[4])
        
    with col3:
        st.text(names[2])
        st.image(posters[2])
        st.text(names[5])
        st.image(posters[5])