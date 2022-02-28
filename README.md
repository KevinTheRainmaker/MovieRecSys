# MovieRecSys

### Overview
This project uses various recommendation system algorithms to create and distribute websites that recommend movies.

As a baseline for this, the following video was referred.

<a href="https://youtu.be/1xtrIEwY_zY">[YouTube: 'Movie Recommender System Project | Content Based Recommender System with Heroku Deployment']</a>

---
### Contents

<a href ="">1. Project Flow</a>

<a href ="">2. Dataset & Jupyter notebook setup</a>

<a href ="">3. Data Preprocessing</a>

<a href ="">4. Vectorization</a>

<a href ="">5. Main function</a>

<a href ="">6. Frontend/Streamlit</a>

<a href ="">7. Deployment</a>

---

## 1. Project Flow

- **Dataset: TMDB 5000 Dataset from Kaggle
<a href ="https://www.kaggle.com/tmdb/tmdb-movie-metadata">[Link]</a>**

    Both datasets were downloaded, combined appropriately, and simple processing was performed. 

    As a result, a dataset without empty or duplicate values was completed.
    
    The size of the dataset is (4800, 7).

<br >

- **Preprocessing**

    First, the expression of genres and keywords was recognized by using the list_eval() method in the ast package. 
    From this, all values with the 'name' key were taken and stored in the list form. It was preprocessed again through the lower() and replace() methods.

    Up to three casts were treated with helper function using list_eval() to show main actors, and similarly crew was also processed to indicate director.
    In both cases, spaces were removed.

    Overview was then preprocessed to use nlp. This will be additionally carried out later.

    Finally, the columns previously processed (except overview) are combined into the column 'tags' that were newly created.