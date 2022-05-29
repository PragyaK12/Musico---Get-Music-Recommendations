import streamlit as st
st.set_page_config(page_title="Song Recommendation", layout="wide")

import pandas as pd
from sklearn.neighbors import NearestNeighbors
import streamlit.components.v1 as components

from display_rec import *

  

genres = ['Movie', 'R&B', 'A Capella', 'Alternative', 'Country', 'Dance',
       'Electronic', 'Anime', 'Folk', 'Blues', 'Opera', 'Hip-Hop',
       "Children's Music",'Rap', 'Indie',
       'Classical', 'Pop', 'Reggae', 'Reggaeton', 'Jazz', 'Rock', 'Ska',
       'Comedy', 'Soul', 'Soundtrack', 'World']

audio_features = ["acousticness", "danceability", "energy", "instrumentalness", "valence", "tempo"]

df = df = pd.read_csv("SpotifyFeatures.csv")

def getNearestNeighbours(genre,test_feat,num_recommendations):

    same_genre_data = df[(df["genre"]==genre)]
    same_genre_data = same_genre_data.sort_values(by='popularity', ascending=False)[:500]

    model = NearestNeighbors()
    model.fit(same_genre_data[audio_features].to_numpy())

    k_nearest = model.kneighbors([test_feat], n_neighbors=num_recommendations, return_distance=False)[0]

    track_ids = same_genre_data.iloc[k_nearest]["track_id"].tolist()
    return track_ids


def display(tracks,col1,col3):
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


def genre_based():

    st.title("Tune the features as you Like :D")

    with st.container():
        col1, col2,col3,col4 = st.columns((2,0.5,0.5,0.5))
        with col3:
            st.markdown("***Choose your genre:***")
            genre = st.radio(
                "",
                genres, index=genres.index("Pop"))
        with col1:
            st.markdown("***Choose features to customize:***")
           
            acousticness = st.slider(
                'Acousticness',
                0.0, 1.0, 0.5)
            danceability = st.slider(
                'Danceability',
                0.0, 1.0, 0.5)
            energy = st.slider(
                'Energy',
                0.0, 1.0, 0.5)
            instrumentalness = st.slider(
                'Instrumentalness',
                0.0, 1.0, 0.0)
            valence = st.slider(
                'Valence',
                0.0, 1.0, 0.45)
            tempo = st.slider(
                'Tempo',
                0.0, 244.0, 118.0)

    #tracks_per_page = 6
    test_feat = [acousticness, danceability, energy, instrumentalness, valence, tempo]
    track_ids = getNearestNeighbours(genre, test_feat,10)

    tracks = []
    for id in track_ids:
        track = """<iframe src="https://open.spotify.com/embed/track/{}" width="260" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>""".format(id)
        tracks.append(track)

   
    display(tracks,col1,col3)

    

    

    

