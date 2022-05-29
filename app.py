# importing streamlit 
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

# importing web pages 
from playlist_model import *
from genre_audio_feat import *
from fav_song_recommendation import *
from spotify_playlist_based import * 
from home import *

# importing necessary libraries for spotify linking 
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

from PIL import Image


st.set_page_config(
     page_title="Musico",
     page_icon="🎵",
     layout="wide",
     menu_items={}
    )


with st.sidebar:
    # navigation bar
    curr_page = option_menu(
        menu_title=None, 
        options=["Home", "Link My Spotify Playlists", "I'll tell my favourite genre","I'll Tell My Fvourite Song"], 
        icons=[ "house"], 
        default_index=0, 
        )

if "curr_page" not in st.session_state: # setting the default page as home page 
    st.session_state.curr_page="Home"

# checking the current page 

if (curr_page=="Home"): 
    st.session_state.curr_page="Home"
    home_page()


if (curr_page=="Link My Spotify Playlists"):
    st.session_state.curr_page="Spotify_Playlist"
    spotify_playlist_page()

if (curr_page=="I'll tell my favourite genre"):
    st.session_state.curr_page="Genre_Based"
    genre_based()
    

if (curr_page=="I'll Tell My Fvourite Song"):
    fav_song_page()
