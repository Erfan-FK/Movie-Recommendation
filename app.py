from flask import Flask, render_template, request, jsonify, redirect, url_for

import requests
import numpy as np
import pandas as pd

app = Flask(__name__)

TMDB_API_KEY = 'YOUR_API_KEY'

similarity_matrix = np.load('data/similarity_matrix.npy')
movies_df = pd.read_csv('data/movies_data.csv')


def get_movie_index(title):
    result = movies_df[movies_df['originalTitle'].str.contains(title, case=False, na=False)]
    if not result.empty:
        return result.index[0]
    return None


def recommend(movie_index, top_n=10):
    similarity_scores = list(enumerate(similarity_matrix[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:top_n+1]
    movie_indices = [i[0] for i in similarity_scores]

    return movie_indices


def fetch_movie_details(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&append_to_response=credits'
    response = requests.get(url)
    return response.json()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detail')
def detail():
    title = request.args.get('title')
    if not title:
        return redirect(url_for('home'))

    movie_index = get_movie_index(title)
    if movie_index is None:
        return redirect(url_for('home'))

    movie_id = movies_df.iloc[movie_index]['tconst']
    movie = fetch_movie_details(movie_id)

    recommended_indices = recommend(movie_index, 9)
    recommended_movies = []
    for idx in recommended_indices:
        rec_movie_id = movies_df.iloc[idx]['tconst']
        rec_movie = fetch_movie_details(rec_movie_id)
        recommended_movies.append({
            'title': rec_movie['title'],
            'poster_path': rec_movie['poster_path']
        })

    # Get required movie details
    movie_details = {
        'title': movie['title'],
        'poster_path': movie['poster_path'],
        'overview': movie['overview'],
        'release_date': movie['release_date'],
        'runtime': movie['runtime'],
        'rating': movie.get('vote_average'),
        'director': next((crew['name'] for crew in movie['credits']['crew'] if crew['job'] == 'Director'), 'N/A'),
        'cast': [
            {
                'name': cast['name'],
                'character': cast['character'],
                'profile_path': cast['profile_path']
            }
            for cast in movie['credits']['cast'][:18]
        ],
        'recommended_movies': recommended_movies
    }

    return render_template('detail.html', movie=movie_details)


if __name__ == '__main__':
    app.run(debug=True)
