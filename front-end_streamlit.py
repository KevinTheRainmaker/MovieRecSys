import streamlit as st
import pickle
import pandas as pd

movies_pickle = pickle.load(open('pickle/movies_dict.pkl', 'rb'))
movies_list = pd.DataFrame(movies_pickle)['title'].values
genre_sim_sorted_ind = pickle.load(open('pickle/genre_sim_sorted_ind.pkl', 'rb'))
st.title('MovieRecSys Demo')

selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies_list['title'].values
)

# if st.button('Recommend'):
#     df = recommend(selected_movie_name)
#     st.write(f"Recommendation based on genres of '{selected_movie_name}'")
#     for i in df['title'].values:
#         st.write(i)
    
option = st.selectbox(
    'Search the movie you likes.',
    movies_list
)