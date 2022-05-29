# importing necessary libraries for spotify api 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import streamlit.components.v1 as components


#importing streamlit 
import streamlit as st 


#function to get recommendations using sppotify api function
def get_recommendations_spotify(song_name=None):

    #Authorising
    client_id = '69af2951bd214eb79c214240c17aabc9' 
    client_secret= 'b5c29e0a0925498388191b7a4eaa1401'
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # Searching for the input song name 
    search_result = sp.search(q = song_name, type = 'track', limit = 1)

    # fetching the id of the search result
    song_id = [search_result['tracks']['items'][0]['id']]

    # getting recommendations based on input song 
    return sp.recommendations(seed_tracks = song_id, limit = 10)


# function to get track id of the recommended songs 
def get_ids(recommendations):

    # getting the list of track_id from the recommendations 
    id_list = [track['id'] for track in recommendations['tracks']]

    return id_list


#function to display the recommendations
def display_recommendations(recommendation_ids):
    tracks = []
    for id in recommendation_ids:
        track = """<iframe src="https://open.spotify.com/embed/track/{}" width="260" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>""".format(id)
        tracks.append(track)

    with st.container():
        col1, col2, col3 = st.columns([2,1,2])
        i=0
        for track in tracks:
            if i%2==0:
                with col1:
                    components.html(
                        track,
                        height=400,
                    )
                i+=1

            else:
                with col3:
                    components.html(
                        track,
                        height=400,
                    )
                i+=1



# streamlit webpage 
def fav_song_page():
    st.title("Get More of that One Song You Like")
    song_name=st.text_input('Enter Song Name')
    if (song_name):
        recommendations=get_recommendations_spotify(song_name)
        recommendation_ids=get_ids(recommendations)
        display_recommendations(recommendation_ids)






