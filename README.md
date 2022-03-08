# MovieRecSys

### Overview
This project uses various recommendation system algorithms to create and distribute websites that recommend movies.

- <a href = "https://github.com/KevinTheRainmaker/Recommendation_Algorithms/blob/main/1.%20Content-Based%20Filtering%20Practice%20-%20TMDB%205000%20Movie%20Dataset.ipynb">Content-Based Filtering</a>


As a baseline for deploy, the following was referred.

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

First, the expression of genres and keywords was recognized by using the list_eval() method in the ast package. 

From this, all values with the 'name' key were taken and stored in the list form. It was preprocessed again through the lower() and replace() methods.

Up to three casts were treated with helper function using list_eval() to show main actors, and similarly crew was also processed to indicate director.
    In both cases, spaces were removed.

Overview was then preprocessed to use nlp. This will be additionally carried out later.

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

<br>

## 5. Frontend/Streamlit

<br>

## 6. Deployment
