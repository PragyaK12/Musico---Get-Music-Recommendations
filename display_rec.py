import streamlit as st
import streamlit.components.v1 as components


# function to display recommendations 

def display_recommendations(recommendations):
    tracks = []
    for id in recommendations['track_id']:
        track = """<iframe src="https://open.spotify.com/embed/track/{}" width="260" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>""".format(id)
        tracks.append(track)

    with st.container():
        col1, col2, col3 = st.columns([2,0.5,2])
        i=0
        for track,recommendation in zip(tracks,recommendations['track_id']):
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

