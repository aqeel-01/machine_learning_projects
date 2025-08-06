import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os
import requests
import warnings

# Optional: suppress warnings
warnings.filterwarnings("ignore")

# Load environment variables
load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Spotify API setup
client_credentials_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Fallback Spotify logo
FALLBACK_IMAGE_URL = "https://storage.googleapis.com/pr-newsroom-wp/1/2023/05/Spotify_Logo_CMYK_Green.png"

def is_valid_image_url(url):
    """Check if image URL returns a successful response."""
    try:
        response = requests.head(url, timeout=3)
        return response.status_code == 200
    except Exception:
        return False

def get_song_album_cover_url(song_name, artist_name):
    """Get album cover URL or fallback image."""
    try:
        query = f"track:{song_name} artist:{artist_name}"
        result = sp.search(q=query, type="track", limit=1)
        if result and result["tracks"]["items"]:
            url = result["tracks"]["items"][0]["album"]["images"][0]["url"]
            if is_valid_image_url(url):
                return url
    except Exception as e:
        print(f"Error getting cover for {song_name} - {artist_name}: {e}")
    
    return FALLBACK_IMAGE_URL

def recommend(song):
    """Recommend 5 similar songs."""
    try:
        index = music[music['song'] == song].index[0]
        distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
        recommended_songs = []
        recommended_posters = []

        for i in distances[1:6]:
            song_name = music.iloc[i[0]].song
            artist_name = music.iloc[i[0]].artist
            album_cover = get_song_album_cover_url(song_name, artist_name)
            recommended_songs.append(song_name)
            recommended_posters.append(album_cover)

        return recommended_songs, recommended_posters

    except Exception as e:
        st.error(f"Recommendation error: {e}")
        return [], []

# Streamlit UI setup
st.set_page_config(page_title="🎵 Music Recommender", layout="wide")
st.title("🎶 Music Recommender System")


# Load data
try:
    music = pickle.load(open("df.pkl", "rb"))
    similarity = pickle.load(open("similer.pkl", "rb"))
except Exception as e:
    st.error("Error loading model/data files.")
    st.stop()

# Song selection
selected_song = st.selectbox("🎧 Choose a song:", music['song'].values)

# Show recommendations
if st.button("🎵 Show Recommendations"):
    names, posters = recommend(selected_song)
    if names:
        st.subheader("🎼 You might also like:")
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.image(posters[idx], use_container_width=True)
                st.caption(names[idx])
    else:
        st.warning("No recommendations found.")

