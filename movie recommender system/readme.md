

# Movie Recommender System

A **content-based movie recommendation system** built with **Python**, **pandas**, **NLTK**, **scikit-learn**, and **Streamlit**. It recommends movies based on similarity in genres, keywords, cast, crew, and overview.

---

##  Demo Screenshot

![Movie Recommender Demo](screenshots/movie%20pic/demo.png)

---

##  Features

- Content-based filtering using **cosine similarity**
- Clean UI using **Streamlit**
- Movie posters fetched from **TMDB API**
- Fast recommendations from a precomputed similarity matrix
- Local caching of movie metadata using `pickle`

---

##  How it Works

1. Data loaded from TMDB dataset (`tmdb_5000_movies.csv`, `tmdb_5000_credits.csv`)
2. Extract key features: **overview**, **genres**, **keywords**, **cast**, **crew**
3. Combine and clean into a `tags` column
4. Apply **NLTK stemming** and remove stopwords
5. Create vector representation using `CountVectorizer`
6. Calculate similarity matrix using **cosine similarity**
7. Streamlit UI provides top 5 similar movie recommendations

---

##  Installation

### 1. Clone the repo

```
cd movie-recommender-streamlit


### 2. Install dependencies

pip install -r requirements.txt

Or manually install:

pip install streamlit pandas scikit-learn nltk requests python-dotenv

### 3. Add your .env file

Create a .env file in the root directory:


TMDB_API_KEY=your_tmdb_api_key_here

## Run the App

streamlit run app.py

##  Project Structure

```
.
├── app.py
├── movie_dict.pkl
├── movies.pkl
├── similarity.pkl
├── .env
├── screenshots/
│   └── movie_pic/
│       ├── demo.png
│       └── avatar_results.png
└── README.md

```
