# 🎬 Movie Recommender System

An intelligent and visually appealing movie recommendation app built with **Streamlit** and powered by **TMDB API**. This tool suggests similar movies based on a selected title and displays their posters using real-time data.

---

## 🖼️ Poster & UI

![Poster](./images/poster.png)
![UI](./images/ui.png)

---

## 📂 Project Structure

<pre lang="markdown"> ``` 
movie-recommender/ 
├── .streamlit/ 
│ └── config.toml # Custom UI Theme 
├── model/ 
│ ├── movie.pkl # Movie data 
│ └── similarity.pkl # Cosine similarity matrix 
├── app.py # Main Streamlit app 
├── requirements.txt # Python dependencies 
└── README.md  # You're reading it! ``` </pre>

---

## 🚀 Features

- 🎥 Select a movie and get 5 similar movie recommendations
- 🖼️ Fetches and displays posters using **TMDB API**
- 🧠 Content-based recommendation using cosine similarity
- 🎨 Custom-themed UI with columns layout

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, Pandas
- **API**: TMDB API
- **ML**: Cosine Similarity
- **Storage**: Pickle (.pkl)

---

## 🔧 Installation

<pre lang='markdown'>```
# 1. Clone the repository
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```</pre>


