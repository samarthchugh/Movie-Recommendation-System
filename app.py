import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies_dict = pickle.load(open('model/movie.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Function to fetch poster
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f'https://image.tmdb.org/t/p/w500/{poster_path}'
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

# Recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie_names, recommended_movie_posters

# --- Streamlit Page Config ---
st.set_page_config(page_title="Movie Recommender", layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
        .main {
            background-color: #0f2027;
            background-image: linear-gradient(to right, #2c5364, #203a43, #0f2027);
            color: white;
        }
        .stSelectbox label, .stButton button {
            font-weight: bold;
            color: #00ffd9;
        }
        .movie-title {
            font-size: 20px;
            font-weight: bold;
            color: #00ffd9;
            text-align: center;
            margin-bottom: 10px;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center; color: white;'>🎬 Movie Recommender System 🍿</h1>", unsafe_allow_html=True)

# --- Select Movie ---
selected_movie_name = st.selectbox("🎥 Select a movie to get recommendations:", movies['title'].values)

# --- Recommend Button ---
if st.button("✨ Show Recommendations"):
    names, posters = recommend(selected_movie_name)
    st.markdown("<hr>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)
            st.image(posters[i])

# --- Footer ---
st.markdown("""
    <hr>
    <div style='text-align: center; color: white; font-size: 14px;'>
        Built with ❤️ by <a href='https://github.com/samarthchugh' style='color: #00ffd9;'>Samarth Chugh</a><br>
        Data from <a href='https://www.themoviedb.org/' style='color: #00ffd9;'>TMDB</a>
    </div>
""", unsafe_allow_html=True)
