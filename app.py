import streamlit as st
import pickle
import requests
import pandas as pd
from streamlit_lottie import st_lottie
import json

# Load Lottie animation
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# API configuration
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"
BASE_URL = "https://api.themoviedb.org/3/movie/"

@st.cache_data
def fetch_poster(movie_id):
    """Fetch movie poster from TMDB"""
    try:
        url = f"{BASE_URL}{movie_id}?api_key={API_KEY}&language=en-US"
        data = requests.get(url).json()
        poster_path = data['poster_path']
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except:
        return "https://via.placeholder.com/500x750?text=Poster+Not+Available"

@st.cache_data
def load_data():
    """Load pickled data"""
    movies = pickle.load(open('movies.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity

def recommend(movie, movies_df, similarity, n_recommendations=5):
    """Generate movie recommendations"""
    try:
        index = movies_df[movies_df['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), 
                         reverse=True, key=lambda x: x[1])
        recommended_movies = []
        movie_posters = []
        for i in distances[1:n_recommendations+1]:
            movie_id = movies_df.iloc[i[0]].movie_id
            recommended_movies.append(movies_df.iloc[i[0]].title)
            movie_posters.append(fetch_poster(movie_id))
        return recommended_movies, movie_posters
    except:
        return ["Movie not found"], ["https://via.placeholder.com/500x750?text=Not+Found"]

# Set up page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Load data
movies_df, similarity = load_data()

# Custom CSS
st.markdown("""
    <style>
    .movie-card {
        padding: 10px;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 10px;
    }
    .movie-title {
        font-size: 16px;
        font-weight: bold;
        margin: 5px 0;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([1, 3])
with col1:
    # Add Lottie animation (download from https://lottiefiles.com/)
    try:
        lottie_movie = load_lottiefile("movie_animation.json")
        st_lottie(lottie_movie, height=200)
    except:
        st.image("https://via.placeholder.com/200x200?text=Movie+Icon")

with col2:
    st.title("🎬 Movie Recommendation System")
    st.subheader("Find your next favorite movie!")

# Movie selection
movie_list = movies_df['title'].values
selected_movie = st.selectbox(
    "Type or select a movie",
    movie_list,
    help="Start typing to search for a movie"
)

# Recommendation settings
n_recommendations = st.slider("Number of recommendations", 3, 10, 5)

# Show recommendations
if st.button("Get Recommendations", type="primary"):
    with st.spinner("Finding recommendations..."):
        recommended_movies, posters = recommend(selected_movie, movies_df, 
                                              similarity, n_recommendations)
        
        st.success(f"Movies similar to {selected_movie}")
        
        # Display recommendations in a grid
        cols = st.columns(min(n_recommendations, 5))
        for idx, (movie, poster) in enumerate(zip(recommended_movies, posters)):
            with cols[idx % 5]:
                st.markdown(f"""
                    <div class="movie-card">
                        <img src="{poster}" width="100%">
                        <div class="movie-title">{movie}</div>
                    </div>
                """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Data from TMDB")