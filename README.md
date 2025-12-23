# Music Recommendation System

A content-based music recommendation web application built with Python and Streamlit. It suggests songs based on lyric similarity using Machine Learning (Cosine Similarity) and fetches real-time album covers using the Spotify API.

## Features

- Content-Based Filtering: Recommeds Songs similar to your selection based on lyrics
- Spotify Integration: Automatically fetches high-quality album art for every recommended songs
- Interative UI: clean and simple web interface powered by Streamlit
- Top 5 Recommendation: Instantly display the top 5 most similar songs

## Tech Stack

- Frontend: Streamlit
- Backend: Python
- Machine Learning: scikit-Learn
- Data Handling: Pandas, Pickle
- API: Spotipy(Spotify web API)

## Getting Started



### Installation

## Download & Extract
-  Download the project zip file from ** **.
-    **Unzip/Extract** the folder to a location on your computer (e.g., Desktop or Downloads).
3.  Open your terminal (Command Prompt or PowerShell) and navigate to the extracted folder:
    ```bash
    cd path/to/extracted-folder/music-recommender
    ```

### 2. Install Dependencies
Ensure you have **Python 3.7+** installed. Run the following command to install the required libraries:

```bash
pip install streamlit spotipy pandas scikit-learn

```

#Run the Application
``` bash
streamlit run app.py
```

## Project Structure

```text
music-recommender/
│
├── app.py                   # The main Streamlit web application
├── main-copy.ipynb          # Jupyter Notebook used for data cleaning & model training
├── music_file.pkl           # Processed music data (Pickle file)
├── similar_data.pkl         # Similarity matrix (Pickle file)
├── spotify_data.csv         # Raw dataset containing songs and lyrics
├── requirements.txt         # List of Python dependencies
└── README.md                # Project documentation
```

## API

The app uses the spotify API to fetch song and album cover, if album cover not available, spotify logo will be displayed.

## My Coding Approach
- Cleaning:
    The raw dataset (spotify_data.csv) is cleaned to remove duplicates and null values.
- Stemming:
    applied PorterStemmer (from NLTK) to reduce words to their root form (e.g.,                      "dancing", "danced", "dancer" $\rightarrow$ "danc"). This ensures that variations of the         same word are treated as identical features.
- Feature Extraction (Vectorization):
    Computers cannot understand text directly, so we convert the "tags" into numbers using Bag       of Words (BoW) logic: CountVectorizer from Scikit-Learn.
- Similarity Calculation:
   To find similar songs, we calculate the geometric distance between the vectors (rows) created    in the previous step.
   **Metric: Cosine Similarity**.
- Recommendation Logic:
  - When a user selects a song (e.g., "Song A"), the system performs the following steps:
  -Index Lookup: Finds the index of "Song A" in the dataframe.
  - Fetch Scores: Retrieves the row of similarity scores for "Song A" against all other songs.
  - Sort: Sorts the scores in descending order (highest similarity first).
  -Slice: Picks the top 5 songs (excluding the first one, which is "Song A" itself).
  - Output: Returns the names of these 5 songs to the frontend.

## Note
 If you encounter a **FileNotFoundError**, please ensure that **music_file.pkl** and **similar_data.pkl** are located in the same directory where you are running the streamlit run command.

