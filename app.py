import numpy as np
import streamlit as st
import pickle
import requests

st.title("Movie Recommendations")
movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8c5e7dcb825266dc90ff2ca4100e7c0f&language=en-US'.format(movie_id))
    data = response.json()
    print(data)
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


def recommend(movie):
    idx =  movies_list[movies_list['title'] == movie].index[0]
    array_m = similarity[idx]
    array_m = sorted(list(enumerate(array_m)),reverse=True, key= lambda x: x[1])[1:6]
    recs = []
    recs_posters = []
    for i in array_m:
        movie_id =movies_list.loc[i[0]].movie_id
        ## fetch poster from api

        recs.append(movies_list.loc[i[0]].title)
        recs_posters.append(fetch_poster(movie_id))

    return recs,recs_posters
    
     


movies_list1 = movies_list['title'].values
movie_name= st.selectbox('Movie names',movies_list1)


if st.button('Find Recommendations'):
    recommendations,posters = recommend(movie_name)
    col1, col2,col3,col4, col5 = st.columns(5)
    with col1:
        st.text(recommendations[0])
        st.image(posters[0])
    with col2:
        st.text(recommendations[1])
        st.image(posters[1])
    with col3:
        st.text(recommendations[2])
        st.image(posters[2])
    with col4:
        st.text(recommendations[3])
        st.image(posters[3])
    with col5:
        st.text(recommendations[4])
        st.image(posters[4])

