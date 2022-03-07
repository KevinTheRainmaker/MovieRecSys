# MovieRecSys

### Overview
This project uses various recommendation system algorithms to create and distribute websites that recommend movies.

- <a href = "https://github.com/KevinTheRainmaker/Recommendation_Algorithms/blob/main/1.%20Content-Based%20Filtering%20Practice%20-%20TMDB%205000%20Movie%20Dataset.ipynb">Content-Based Filtering</a>


As a baseline for deploy, the following was referred.

<a href="https://youtu.be/1xtrIEwY_zY">[YouTube: 'Movie Recommender System Project | Content Based Recommender System with Heroku Deployment']</a>

---
### Contents

<a href ="">1. Project Flow</a>

<a href ="">2. Data Preprocessing</a>

<a href ="">3. Measure content similarity</a>

<a href ="">4. Frontend/Streamlit</a>

<a href ="">5. Deployment</a>

---

## 1. Project Flow

- **Dataset: TMDB 5000 Dataset from Kaggle
<a href ="https://www.kaggle.com/tmdb/tmdb-movie-metadata">[Link]</a>**

Both datasets were downloaded, combined appropriately, and simple processing was performed. 

As a result, a dataset without empty or duplicate values was completed.
    
The size of the dataset is (4800, 7).


```
movies = pd.read_csv(os.path.join(root_path, 'tmdb_5000_movies.csv'))
credits = pd.read_csv(os.path.join(root_path, 'tmdb_5000_credits.csv'))

credits.rename(columns = {'movie_id' : 'id'}, inplace = True)

df = movies.merge(credits, on=['title', 'id'])

extract = df[['id','title','overview','genres','keywords','cast','crew']].copy()
extract.dropna(inplace=True)
```

<br >

## 2. Data Preprocessing

First, the expression of genres and keywords was recognized by using the list_eval() method in the ast package. 

From this, all values with the 'name' key were taken and stored in the list form. It was preprocessed again through the lower() and replace() methods.

Up to three casts were treated with helper function using list_eval() to show main actors, and similarly crew was also processed to indicate director.
    In both cases, spaces were removed.

Overview was then preprocessed to use nlp. This will be additionally carried out later.

Finally, the columns previously processed (except overview) are combined into the column 'tags' that were newly created.

```
# genres, keywords
from ast import literal_eval
extract['genres'] = extract['genres'].apply(literal_eval)
extract['keywords'] = extract['keywords'].apply(literal_eval)
extract['genres'] = extract['genres'].apply(lambda x : [y['name'] for y in x])
extract['keywords'] = extract['keywords'].apply(lambda x : [y['name'] for y in x])

extract['genres'] = extract['genres'].apply(lambda x:[i.lower().replace(" ", "_") for i in x])
extract['keywords'] = extract['keywords'].apply(lambda x:[i.replace(" ", "_") for i in x]) 

extract['cast'] = extract['cast'].apply(convert_cast)
extract['cast'] = extract['cast'].apply(lambda x:[i.replace(" ", "") for i in x])

# crew to director
extract['director'] = extract['crew'].apply(fetch_director)
extract = extract.drop(columns=['crew'])
extract['director'] = extract['director'].apply(lambda x:[i.replace(" ", "") for i in x])

extract['tags'] = extract['genres'] + extract['keywords'] + extract['cast'] + extract['director']
movies_df = extract[['id','title','overview','tags']]
```
    
<br>

## 3. Measure content similarity
