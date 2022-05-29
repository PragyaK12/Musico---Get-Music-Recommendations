# importing necessary libraries 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
from playlist_model import *
from display_rec import *
import streamlit as st
from PIL import Image



# function to link user's spotify playlists and get a dictionary with playlist names 
def get_playlists():
    client_id = '69af2951bd214eb79c214240c17aabc9' 
    client_secret= 'b5c29e0a0925498388191b7a4eaa1401'
    scope = 'user-library-read'
    token = util.prompt_for_user_token(scope, client_id= client_id, client_secret=client_secret, redirect_uri='http://localhost:8881/callback')
    sp = spotipy.Spotify(auth=token)
    playlist_dic = {}

    for i in sp.current_user_playlists()['items']:
        playlist_dic[i['name']] = i['uri'].split(':')[2]

    return playlist_dic , sp


# function to get the playlist id from user input url 
def get_playlist_id_from_url(playlist_url):
    playlist_id = playlist_url.split('/')[-1].split('?')[0]
    return playlist_id
   


# web page 
def spotify_playlist_page():
    song_dataset = pd.read_csv('data/SpotifyFeatures.csv')
    #st.title('Get Recommendations for Your Spotify Playlist')
    st.title('Get Recommendations for any Spotify Playlist')
    playlist_url = st.text_input("Enter Playlist Url")
    with st.expander("Here's how to find any Playlist url in Spotify"):
        st.text("Right click on the playlist you like")
        st.text("Go to : Share -> Copy Link to Playlist")
        image=Image.open("images/how_to_get_url.png")
        st.image(image)

    if "get_recommendation" not in st.session_state:
        st.session_state.get_recommendation = False

    if "playlist_link_input" not in st.session_state:
        st.session_state.playlist_link_input = False

    if (st.button("Get Recommendations") or st.session_state.get_recommendation):
        with st.spinner("Fetching Recommendations..."):
            st.session_state.get_recommendation = True
            #if playlist_url is not None:
            st.session_state.playlist_link_input=True
            playlist_id=get_playlist_id_from_url(playlist_url)
            playlist_df,sp = generate_playlist_df(song_dataset,playlist_id)
            playlist_vector , nonplaylist_df = generate_playlist_vector(spotify_features_df, playlist_df, 1.2)
            recommendations = generate_recommendation(song_dataset, playlist_vector, nonplaylist_df, 10,sp)
            display_recommendations(recommendations)
        



    


    
    #initialize session state 
    #if "link_playlist" not in st.session_state:
     #   st.session_state.link_playlist = False 

    # linking user playlist
    #user_playlist_dic={}
    #if (st.button('Link My Playlists') or st.session_state.link_playlist):
     #   st.session_state.link_playlist = True
      #  user_playlist_dic , sp=get_playlists()
       # if (not user_playlist_dic): #checking if user playlist is empty
        #    st.write('Oops! You do not have any playlists in your account')
        #else:
         #   playlist_name = st.selectbox("Select One Playlist: ", user_playlist_dic.keys())
          #  #generate dataframe of selected playlist 
           # playlist_df=generate_playlist_df(playlist_name, user_playlist_dic, song_dataset,sp)
            # converting playlist to vector 
            #playlist_vector , nonplaylist_df = generate_playlist_vector(spotify_features_df, playlist_df, 1.2)
            #if (st.button('Get Recommendations')):
                #generate recommendations 
             #   recommendations = generate_recommendation(song_dataset, playlist_vector, nonplaylist_df, 10,sp)
                #display recommendations
              #  display_recommendations(recommendations)