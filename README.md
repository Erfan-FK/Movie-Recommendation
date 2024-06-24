# Movie Recommendation System

This project is a content-based movie recommendation system.

<img src="/static/gif/Shrek.gif" alt="Gif">

<img src="/static/gif/spider-man.gif" alt="Gif">

<img src="/static/gif/hobbit.gif" alt="Gif">

## Table of Contents
1. [Introduction](#introduction)
2. [Used Technologies](#used-technologies)
3. [Dataset Preparation](#dataset-preparation)
4. [Algorithm and Similarity Measure](#algorithm-and-similarity-measure)
5. [Usage](#usage)

## Introduction

The **Movie Recommendation System** uses a content-based filtering approach to suggest movies to users based on the features of the movies they have searched. The features used for each movie include genres, overview, cast, director, and title. The recommendation engine utilizes the Cosine Similarity algorithm to find movies similar to the ones the user has shown interest in.

## Used Technologies

This project was developed using the following technologies:

[![My Skills](https://skillicons.dev/icons?i=py,flask,js,html,css&theme=light)](https://skillicons.dev)
![Google Colab](https://img.icons8.com/color/48/000000/google-colab.png)


## Dataset Preparation

The dataset for this project was prepared using Google Colab and APIs from IMDb and TMDB. The dataset includes 6223 movies and around 7000 features extracted from various movie attributes. The preparation steps are documented in the provided Google Colab notebooks.

The data includes the following columns:
- `tconst`
- `originalTitle`
- `startYear`
- `runtimeMinutes`
- `genres`
- `averageRating`
- `numVotes`
- `crew`
- `overview`

The data was collected using the following steps:
1. **Fetching Movie Data:** Using IMDb and TMDB APIs to get details about movies.
2. **Feature Extraction:** Extracting features such as genres, overview, cast, director, and title for each movie.
3. **Preprocessing:** Cleaning and transforming the data into a suitable format for building the recommendation model.

The dataset and the Google Colab notebooks used for data preparation are available in the repository's `dataset` folder.

The dataset and the Google Colab notebooks used for data preparation are available in the repository's `dataset` folder. You can find the specific notebooks here:
- [DataPrep.ipynb](data/DataPrep.ipynb)
- [SimilarityMatrix.ipynb](data/SimilarityMatrix.ipynb)


## Algorithm and Similarity Measure

### Cosine Similarity
The core of our recommendation engine is the **Cosine Similarity** measure. This algorithm is used to compute the similarity between two movie vectors. The Cosine Similarity between two vectors A and B is given by:

$$\[ \text{Cosine Similarity} = \cos(\theta) = \frac{A \cdot B}{\||A\|| \||B\||} = \frac{\sum_{i=1}^{n} A_i B_i}{\sqrt{\sum_{i=1}^{n} A_i^2} \sqrt{\sum_{i=1}^{n} B_i^2}} \]$$

In this formula:
- \( A \) and \( B \) are vectors representing two movies.
- \( $\cdot$ \) denotes the dot product of the vectors.
- \( $\||A\||$ \) and \( $\||B\||$ \) are the magnitudes of vectors A and B respectively.

The vectors are constructed using the features extracted from each movie. Each feature contributes to the vector's dimensions, allowing the Cosine Similarity to capture the multi-dimensional relationships between movies.

### Feature Representation
Each movie is represented as a vector in a high-dimensional space where each dimension corresponds to a specific feature such as genre, cast, director, etc. For instance, a movie vector might look like this:

$$\[ \text{Movie Vector} = [\text{genre1}, \text{genre2}, \text{cast1}, \text{cast2}, \dots, \text{director}, \text{overview}, \text{title}] \]$$

These vectors are then used to compute the similarity scores.

## Usage

To run the movie recommendation system, follow these steps:

1. **Create the Similarity Matrix:**
   - Open the `SimilarityMatrix.ipynb` notebook in Google Colab or your local Jupyter environment.
   - Execute the cells to create the similarity matrix.
   - Save the generated similarity matrix to the `data` folder in your project directory alongside the dataframe.

2. **Install Requirements:**
   - Ensure you have Python installed.
   - Install the necessary dependencies by running:
     ```sh
     pip install -r requirements.txt
     ```

3. **Run the Application:**
   - Once the similarity matrix and dataframe are in place, run the application using:
     ```sh
     python app.py
     ```

This will start the Flask server, and you can interact with the movie recommendation system.
