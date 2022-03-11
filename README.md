# MovieRecSys

### Overview
This project uses various recommendation system algorithms to create and distribute websites that recommend movies.

- <a href = "https://github.com/KevinTheRainmaker/Recommendation_Algorithms/blob/main/1.%20Content-Based%20Filtering%20Practice%20-%20TMDB%205000%20Movie%20Dataset.ipynb">Content-Based Filtering</a>


As a baseline for front-end & deploy, the following was referred.

<a href="https://youtu.be/1xtrIEwY_zY">[YouTube: 'Movie Recommender System Project | Content Based Recommender System with Heroku Deployment']</a>

---
### Contents

<a href ="https://github.com/KevinTheRainmaker/MovieRecSys/blob/main/README.md#1-project-flow">1. Project Flow</a>

<a href ="https://github.com/KevinTheRainmaker/MovieRecSys/blob/main/README.md#2-data-preprocessing">2. Data Preprocessing</a>

<a href ="https://github.com/KevinTheRainmaker/MovieRecSys/blob/main/README.md#3-measure-content-similarity">3. Measure content similarity</a>

<a href ="https://github.com/KevinTheRainmaker/MovieRecSys/blob/main/README.md#4-recommendation-using-contents-filtering">4. Recommendation using Contents Filtering</a>

<a href ="https://github.com/KevinTheRainmaker/MovieRecSys/blob/main/README.md#5-frontendstreamlit">5. Frontend/Streamlit</a>

<a href ="https://github.com/KevinTheRainmaker/MovieRecSys/blob/main/README.md#6-deployment">6. Deployment</a>

---

## 1. Project Flow

- **Dataset: TMDB 5000 Dataset from Kaggle
<a href ="https://www.kaggle.com/tmdb/tmdb-movie-metadata">[Link]</a>**

Both datasets were downloaded, combined appropriately, and simple processing was performed. 

As a result, a dataset without empty or duplicate values was completed.
    
The size of the dataset is (4800, 10).

<br >

## 2. Data Preprocessing

- genres, keywords

    First, the expression of genres and keywords was recognized by using the list_eval() method in the ast package. 

    From this, all values with the 'name' key were extracted as the list form. It was preprocessed again through the lower() and replace() methods.

- cast, crew

    Up to three casts were treated to be main actors, and similarly, crew was also processed to indicate director. In both cases, space between names was removed.

- overview

    Overview should be preprocessed to use nlp. This will be additionally carried out later.

- tags

    Finally, part of the columns previously processed are combined into the column 'tags' that were newly created.

<br>

## 3. Measure content similarity

There are several ways to measure content similarity between movies, but the simplest of them is to find cosine similarity. It is implemented in the following steps.

1. The data converted into str form will be feature vectorized based on Count.

2. Compare the vectorized data through cosine similarity.

3. Recommend movies in order of high ratings among movies with high genre similarity.

```
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```

<br>

## 4. Recommendation using Contents Filtering

Only the genres are used in recommendation.

I use 'Weighted Rating' to recommend more properly by considering vote_count and vote_average. Many vote_counts may represent that the movie is popular so I only take 60% from top.

Recommendation is processed by recommend() function that using find_sim_movie() function in it.

find_sim_movie() has two steps.

**1. Retrieval (candidate generation):**     
Get 20(top_n * 2) movies from entire movie using genre similarity. The movie itself is removed from candidates list.

**2. Ranking:**
Choose 10(top_n) from the list in the order of the weighted_vote value. Result is shown as dataframe referred from movies_df.

\* Strictly speaking, the 'Ranking' commonly referred to in the recommendation system is different meaning from this, but the process of creating weighted_vote was above, so it was expressed as this.

```
def find_sim_movie(df, sorted_ind, title_name, top_n = 10):
    title_movie = df[df['title'] == title_name]
    title_index = title_movie.index.values
    
    # Retrieval
    similar_indexes = sorted_ind[title_index, :(top_n * 2)]
    similar_indexes = similar_indexes.reshape(-1)
    
    # Remove the movie itself
    similar_indexes = similar_indexes[similar_indexes != title_index]
    
    #Ranking
    return df.iloc[similar_indexes].sort_values('weighted_vote', ascending=False)[:top_n]
```

<br>

## 5. Frontend/Streamlit

<br>

## 6. Deployment
