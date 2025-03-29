```markdown
# Movie Recommendation System

A content-based movie recommendation system built using Python, scikit-learn, and Streamlit. This project analyzes movie metadata to provide personalized movie recommendations based on content similarity.

## Project Overview

This system uses TF-IDF vectorization and cosine similarity to recommend movies based on their overview, genres, keywords, cast, and crew information. The frontend is built with Streamlit, providing an interactive web interface for users to get movie recommendations.

## Features

- Content-based filtering using movie metadata
- TF-IDF vectorization for text processing
- Cosine similarity for recommendation generation
- Interactive Streamlit web interface
- Movie poster display using TMDB API
- Customizable number of recommendations
- Responsive UI with modern styling

## Dataset

- **Source**: [TMDB Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files**:
  - `tmdb_5000_movies.csv`: Contains movie details like overview, genres, and keywords
  - `tmdb_5000_credits.csv`: Contains cast and crew information
- **Size**: Approximately 4800 movies
- **License**: Provided by The Movie Database (TMDB)

## Requirements

- Python 3.8+
- Libraries:
  - pandas
  - numpy
  - scikit-learn
  - nltk
  - streamlit
  - requests
  - streamlit-lottie (optional for animations)

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Project Structure

```
movie-recommendation-system/
├── model_creation.py    # Model training and pickle file generation
├── app.py              # Streamlit application
├── movies.pkl          # Processed movie data (generated)
├── similarity.pkl      # Similarity matrix (generated)
├── tfidf.pkl          # TF-IDF vectorizer (generated)
├── movie_animation.json # Optional Lottie animation file
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) and place it in folder or update the path .

4. (Optional) Download a movie-related Lottie animation from [Lottiefiles](https://lottiefiles.com/) and save as `movie_animation.json`.

## Usage

1. Generate the model files:
```bash
python model_creation.py
```
This creates `movies.pkl`, `similarity.pkl`, and `tfidf.pkl`.

2. Run the Streamlit application:
```bash
streamlit run app.py
```

3. Open your browser to `http://localhost:8501` and:
   - Select a movie from the dropdown
   - Adjust the number of recommendations (3-10)
   - Click "Get Recommendations" to see similar movies

## How It Works

1. **Data Processing** (`model_creation.py`):
   - Loads and merges TMDB movies and credits datasets
   - Extracts relevant features (overview, genres, keywords, top 3 cast, director)
   - Processes text data using stemming and space removal
   - Creates TF-IDF vectors and similarity matrix
   - Saves processed data as pickle files

2. **Web Application** (`app.py`):
   - Loads preprocessed data
   - Provides interactive UI for movie selection
   - Fetches movie posters from TMDB API
   - Displays recommendations in a responsive grid

## Future Improvements

- Add collaborative filtering
- Include movie ratings and reviews
- Implement genre filtering
- Add search autocomplete
- Include movie trailers
- Deploy to cloud platform (e.g., Heroku, AWS)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The Movie Database (TMDB) for providing the dataset
- Streamlit team for the awesome web framework
- NLTK and scikit-learn teams for text processing tools

## Contact

For questions or suggestions, please open an issue or contact me .
