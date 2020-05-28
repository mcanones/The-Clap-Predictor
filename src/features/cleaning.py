import pandas as pd
from datetime import datetime
from nltk.stem import WordNetLemmatizer
import nltk
stemmer = WordNetLemmatizer()
#nltk.download('wordnet')
#nltk.download('stopwords')
en_stop = set(nltk.corpus.stopwords.words('english'))
import re

def cleaning(df):

    print('Total amount of articles...', df.shape)

    #Drop unnecesary columns
    df.drop(columns=['id','Author', 'Link'], inplace=True)
    print('Dropping unnecesary columns...', df.shape)

    #Drop Null Values
    df.dropna(inplace=True)
    print('Dropping null values...', df.shape)

    """
    #Only English Articles
    df['English'] = df['Title'].apply(lambda title: is_English(title))
    df = df[df['English']==True]
    df.drop(columns='English', inplace=True)
    print('Dropping non-English articles...', df.shape)
    """

    #Casting Data Types
    df.Claps = df.Claps.astype('int64') 
    df.Reading_Time = df.Reading_Time.astype('int64') 
    df.Images = df.Images.astype('int64') 
    df.Links = df.Links.astype('int64') 
    df.Code_Chunks = df.Code_Chunks.astype('int64') 
    df.Numbered_Lists = df.Numbered_Lists.astype('int64') 
    df.Bullet_Lists = df.Bullet_Lists.astype('int64') 
    df.Bolded = df.Bolded.astype('int64') 
    df.Italics = df.Italics.astype('int64') 
    df.Time = pd.to_datetime(df.Time)
    df.Date_Scrapping = pd.to_datetime(df.Date_Scrapping)
    
    return df

def is_English(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

def remove_outlier(df, col):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3-q1 #Interquartile range
    fence_low  = q1-1.5*iqr
    fence_high = q3+1.5*iqr
    df_clean = df.loc[(df[col] > fence_low) & (df[col] < fence_high)]
    print('Number of outliers dropped: ', df.shape[0]-df_clean.shape[0])
    return df_clean

def notLabels(s):
    if s and len(s)>25:
        return None
    return s

def preprocess_text(doc):

    # Remove all the special characters
    doc = re.sub(r'\W', ' ', str(doc))

    # remove all single characters
    doc = re.sub(r'\s+[a-zA-Z]\s+', ' ', doc)

    # Remove single characters from the start
    doc = re.sub(r'\^[a-zA-Z]\s+', ' ', doc)

    # Substituting multiple spaces with single space
    doc = re.sub(r'\s+', ' ', doc, flags=re.I)

    # Removing prefixed 'b'
    doc = re.sub(r'^b\s+', '', doc)

    # Converting to Lowercase
    doc = doc.lower()

    # Lemmatization
    tokens = doc.split()
    tokens = [stemmer.lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if word not in en_stop]
    tokens = [word for word in tokens if len(word) > 3]

    preprocessed_text = ' '.join(tokens)

    return preprocessed_text


