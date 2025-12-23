import streamlit as st  #the library to create web interface 
import pickle as pk #used to load pre-trained ML model
import spotipy  #python library that talks to spotify. It allow us to search for song  cover
from spotipy.oauth2 import SpotifyClientCredentials #handle the login process 

CLIENT_ID = "84565bd9a24b4189b06476fd0d38d8fd"
CLIENT_SECRET = "5ecb87cb7348461f83a2556c89481741"
Client_Credential_Manager =  SpotifyClientCredentials(client_id = CLIENT_ID, client_secret = CLIENT_SECRET)

sp = spotipy.Spotify(client_credentials_manager = Client_Credential_Manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query =f"track:{song_name}, artist:{artist_name}"
    result= sp.search(q=search_query, type="track")

    if result and result["tracks"]["items"]:
        tracks = result["tracks"]["items"][0]
        album_cover_url = tracks["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
    
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similar_data[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)
    return recommended_music_names, recommended_music_posters
    
st.header('Music Recommender System')
music = pk.load(open('music_file.pkl','rb'))
similar_data = pk.load(open('similar_data.pkl','rb'))
movie_list = music['song'].values
selected_movie = st.selectbox("type or select a song from the dropdown", movie_list)

if st.button('show recommendation'):
    recommend_music_names, recommend_music_posters = recommend(selected_movie)
    col1, col2,col3,col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_music_names[0])
        st.image(recommend_music_posters[0], width=150)
    with col2:
        st.text(recommend_music_names[1])
        st.image(recommend_music_posters[1], width=150)
    with col3:
        st.text(recommend_music_names[2])
        st.image(recommend_music_posters[2], width=150)
    with col4:
        st.text(recommend_music_names[3])
        st.image(recommend_music_posters[3], width=150)
    with col5:
        st.text(recommend_music_names[4])
        st.image(recommend_music_posters[4], width=150)


