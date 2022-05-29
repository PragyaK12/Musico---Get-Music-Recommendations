# importing streamlit 
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# importing web pages 
from playlist_model import *
from genre_audio_feat import *
from fav_song_recommendation import *
from spotify_playlist_based import * 

# importing necessary libraries for spotify linking 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

from PIL import Image


# home page 
def home_page():
    col1,col2 = st.columns([4,2])
    with col1:
        st.title("Welcome to Musico :)")
        st.text("Musico lets you discover new music")
        st.text("Get recommendations based on any spotify playlist")
        st.text("Or")
        st.text("Tell us your favourite genre and tune the audio features")
        st.text("Or just tell us your favourite song ;)")
    with col2:
        image = Image.open('images/musicNote.png')
        st.image(image)
    





    

