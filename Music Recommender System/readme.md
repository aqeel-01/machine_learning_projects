
#  Music Recommender System

This is a content-based Music Recommender System that suggests similar songs based on their **lyrics** using **TF-IDF vectorization** and **cosine similarity**.

Built with **Pandas**, **NLTK**, **Scikit-learn**, and deployed using **Streamlit**. It also uses the **Spotify Web API** to display album cover images.

---

##  Screenshot

![App Screenshot](screenshots/song%20pic%20upadted.PNG)

---

##  Features

-  Recommends songs with similar lyrics.
-  NLP-based lyric processing (lowercase, stemming, TF-IDF).
-  Cosine similarity for song similarity.
-  Spotify album covers via Spotipy API.
-  User interface built with Streamlit.
-  Handles missing data or images gracefully.

---

##  How It Works

1. **Lyrics Preprocessing**: Lowercased, cleaned, and stemmed using NLTK.
2. **TF-IDF Matrix**: Lyrics converted into a matrix using `TfidfVectorizer`.
3. **Cosine Similarity**: Similarities computed between all song lyrics.
4. **Recommendation**: When a song is selected, the top 5 most similar songs are shown with their album covers.

---

##  Tech Stack

- Python (Pandas, NLTK, Scikit-learn)
- Spotify API (`spotipy`)
- Streamlit
- Pickle (for saving the model)
- dotenv (for environment variable management)

---

##  Project Structure

details> <summary>📁 Click to expand project structure</summary>
plaintext

machine_learning_projects/
└── Music Recommender System/
    ├── recomendation_system_music.ipynb       # Jupyter notebook for preprocessing & modeling
    ├── df.pkl                                 # Pickled DataFrame of sampled songs
    ├── similer.pkl                            # Pickled cosine similarity matrix
    ├── webapp.py                              # Streamlit frontend application
    ├── .env                                   # Contains SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET (not committed)
    ├── screenshots/
    │   └── song pic upadted.PNG               # UI screenshot used in README
    └── README.md                              # Project documentation
</details>     

## Run It Locally

### 1 Clone the repository

git clone https://github.com/aqeel-01/machine_learning_projects.git

cd machine_learning_projects/Music\ Recommender\ System
### 2 Install dependencies

pip install -r requirements.txt

### 3 Set up Spotify API credentials
Create a .env file in the Music Recommender System/ directory with the following content:

SPOTIPY_CLIENT_ID=your_spotify_client_id

SPOTIPY_CLIENT_SECRET=your_spotify_client_secret

 You can get your credentials by registering an app at Spotify Developer Dashboard

### 4 Launch the app

streamlit run webapp.py


