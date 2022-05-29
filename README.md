<h1 align="center">Musico-Get-Music-Recommendations
  </h1>

<p align="center">
 <a target="_blank" href="https://musico-recommendations.herokuapp.com/">Link to the App</a>
    ·
 <a target="_blank" href="https://youtu.be/GNhxq2WSZ4o">Video Demo</a>
</p>
    
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#salient-features">Salient Features</a></li>
        <li><a href="#compatible-platforms">Compatible Platforms</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#implementation">Implementation</a>
      <ul>
        <li><a href="#what-is-content-based-filtering">What is Content Based Filtering</a></li>
        <li><a href="#why-i-used-content-based-approach">Why I used Content Based Approach</a></li>
        <li><a href="#algorithms-used">Algorithms Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#run-locally">Run Locally</a>
      <ul>
        <li><a href="#how-to-run">How to Run</a></li>
      </ul>
    </li>
    <li><a href="#navigating-through-the-app">Navigating through the App</a></li><ul>
        <li><a href="#home-page">Home Page</a></li>
        <li><a href="#get-recommendations-for-spotify-playlist">Get Recommendations for Spotify Playlist</a></li>
        <li><a href="#get-genre-based-recommendations">Genre Based</a></li>
        <li><a href="#get-recommendations-for-input-song">Get Recommendations for Input Song</a></li>
      </ul>
    <li><a href="#resources-used">Resources Used</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project
* Music Recommendation Web Application project built during Microsoft Engage 2022 program. 
* It is a web application that gives song recommendations based on user's choice  

### Salient Features
* Music Recommendation based on Spotify Playlist
* Music Recommendations based on genre , user's input song name
* Song Preview 

### Compatible Platforms
Laptops, Desktops and Tablet PCs

### Built With

* Streamlit for Front-End
* Python for Recommendation Algorithms


<!-- Implementation -->
## Implementation

### What is Content Based Filtering

Content-based filtering is one popular technique of recommendation or recommender systems. The content or attributes of the things you like are referred to as "content." 
Here, the system uses your features and likes in order to recommend you with things that you might like. It uses the information provided by you over the internet and the ones they are able to gather and then they curate recommendations according to that.  

### Why I used Content Based Approach

* No data from other users is required to start making recommendations. Unlike collaborative filtering, content-based filtering doesn’t need data from other users to create recommendations. Once a user has searched on and browsed a few items and/or completed some purchases, a content-based filtering system can begin making relevant recommendations.
* Recommendations are highly relevant to the user. Content-based recommenders can be highly tailored to the user’s interests.
* Recommendations are transparent to the user. Highly relevant recommendations project a sense of openness to the user, bolstering their trust level in offered recommendations.
* Avoiding the “cold start” problem. Collaborative filtering creates a potential cold start scenario when a new website or community has few new users and lacks user connections. 


### Algorithms Used 

* For Playlist Based Recommendation 

  In the context of Spotify playlists, we use the features (loudness, tempo, etc.) of each song in a playlist to find the average score of the whole     playlist. Then, we recommend a song that has a score similar to the playlist but is not in the playlist.
  #Playlist vector generation : 
  We add all the feature values of each song in the playlist together as a summarization vector whilst providing weight to the songs that were added recently in the playlist
  
<img src="readme-images/playlist_vector.png" width="700"/>
  
  By using cosine similarity as a similarity metric between our playlist vector and songs not present in our playlist we determine songs that are similar to our playlist .We sort the most similar items on in decreasing order of similarity from most similar to least similar 

* For Genre Based Recommendation

I have used k Nearest Neighbor model to get the top songs that are closest in distance with the set of feature inputs selected by the user. These “feature inputs” include the genre of interest and a set of audio features (acousticness, danceability, energy, instrumentalness, valence, tempo).
Using Sklearn to build the k-NN model the function returns values of the top neighbors in ascending order of their rank (a point closest to the input features is ranked first).


## Run Locally
<!-- INSTALLATIONS -->

To install and run the project on your local system, following are the requirements:  

### Requirements

```
matplotlib==3.4.3
pandas==1.3.4
Pillow==9.1.1
scikit_learn==1.1.1
spotipy==2.19.0
streamlit==1.9.0
streamlit_option_menu==0.3.2
```


### How to Run
To run this locally, navigate to the app.py file and run the following on the terminal:
```
streamlit run musico/app.py
```

<!-- APP TUTORIAL-->
## Navigating Through The App

### Home Page

Home page is the landing page of my application that takes you to the various recommendation options provided by application

<img src="readme-images/home-screen.jpeg" alt="home page" width="700"/>

### Get Recommendations for Spotify Playlist

User can enter url of any spotify playlist and get recommendations based on the songs in the playlist

<img src="readme-images/recommendation-through-Playlist.jpeg" alt="recommendation-through-Playlist" width="700"/>


### Get Genre Based Recommendations

The user can select a genre out of the given choices and can customise the audio features and can get recommendations 

<img src="readme-images/recommendation-through-Genre.jpeg" alt="recommendation-through-Genre" width="700"/>

### Get Recommendations for Input Song

The user can enter any song of their choice and get recommendations based on it

<img src="readme-images/recommendation-through-NameOfTheSong.jpeg" alt="recommendation-through-NameOfTheSong" width="700"/>




<!-- ACKNOWLEDGEMENTS -->

## Resources Used

* [Dataset](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db)
* [Spotify Playlist Based Recommendations](https://www.madhavthaker.com/blog/blog-post-title-two-t7f56-98wws-rk84t)
* [Spotify API Documentation](https://developer.spotify.com/documentation/web-api/)

