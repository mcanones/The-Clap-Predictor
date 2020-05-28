# The-Clap-Predictor

<p align="center">
<img src="./reports/figures/head_readme.png" width="650" height="350"/>
</p>

## Scope 

Final project of the Data Analytics Bootcamp in Ironhack (March 2020). The project is divided in 3 parts: 

1) Do `Web Scrapping` from Medium and save the articles in a database.

2) `Clean` and `analyse` data for later analysis. 

3) `Train` a model of `Supervised Learning` to predict how good will be a possible article the user publishes in Medium regarding the number of days since publication.
    - 🗂️ **Binary Classification** 
    - ✅ **Top articles**: articles with claps over the quantile 50 
    - ⛔ **Regular articles**: articles with claps below the quantile 50
    - 🤩 The **first approach** is training a model considering features such as Reading Time, Number of Images in an Article, Number of Links, etc.
    - 🧐 The **advanced approach** is to consider the embeddings (NLP Analysis) to see if they boost the power of prediction.

## Tools 

- **Web Scrapping**: Requests
- **Database**: SQL Alchemy + Sqlite
- **Cleaning**: Pandas, Numpy, NLTK, Matplotlib, Seaborn
- **Model ML**: Sklearn, LightGBM
- **Advanced NLP Analysis of Text Features**: Fasttext

## Some highlights

These are the features that most influence the model when training: 

- **Class 0**: Regular articles 
- **Class 1**: Top articles 

<p align="center">
<img src="./reports/figures/highlights2.png" width="400" height="260"/>
</p>



