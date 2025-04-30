import pickle

import streamlit as st

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


ClIENT_ID = " " # use the spotify genearted id here
CLIENT_SECRET = "" # use the spotify genearted sceret key  here

#intialize the spotify client

client_credentials_manger = SpotifyClientCredentials(client_id=ClIENT_ID , client_secret=CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manger)



def get_song_album_cover_url(song_name , artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")


    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return ""
    


def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse= True , key = lambda x: x[1])
    recommend_music_names = []
    recommend_music_posters = []
    for i in distances[1:6]:
        #fetch the song poster
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommend_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song ,artist))
        recommend_music_names.append(music.iloc[i[0]].song)
    
    return recommend_music_names, recommend_music_posters

st.header('Music Recommender System')
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similer.pkl','rb'))


music_list = music['song'].values
selected_song = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)


if st.button('Show Recommendation'):
    recommend_music_names , recommend_music_posters = recommend(selected_song)
    col1, col2 , col3 , col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_music_names[0])
        st.image(recommend_music_posters[0])
    with col2:
        st.text(recommend_music_names[1])
        st.image(recommend_music_posters[1])
    with col3:
        st.text(recommend_music_names[2])
        st.image(recommend_music_posters[2])
    with col4:
        st.text(recommend_music_names[3])
        st.image(recommend_music_posters[3])
    with col5:
        st.text(recommend_music_names[4])
        st.image(recommend_music_posters[4])
        
