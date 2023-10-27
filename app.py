import streamlit as st
import numpy as np
import pandas as pd
import pickle

def recommend(movie):
    movie_index = movies_list_df[movies_list_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_movies = []
    for i in movies_list:#movies_list is enumerated list
        recommended_movies.append(movies_list_df.iloc[i[0]].title)
    
    return recommended_movies


movies_list_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list_df['title'].values
print(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'How would you like to be contacted?',
movies_list)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



# api key - 05fd93503b9db40bdfe8e12b99a0cde0
# API Read Access Token - eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNWZkOTM1MDNiOWRiNDBiZGZlOGUxMmI5OWEwY2RlMCIsInN1YiI6IjY0OGE0NjNjNTMyYWNiMDBjODRhZWQ5NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hyhkJPtlv8QJfTMQdXmwGZB1v2osQ5zqXOeSVBblSds
