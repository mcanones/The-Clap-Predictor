import requests 
import simplejson
import pandas as pd


def callBertServer(string, id_):
    payload={"id": id_, "texts":[string], "is_tokenized":False} 
    r = requests.post("http://whiteboxml.com:8915/encode", json=payload).json()
    return r

def bert():

    articles = pd.read_parquet("../../data/processed/model_NoTextFeat.parquet").reset_index(drop=True)

    #Titles
    articles['Title_Embeddings']=""
    for i in range(len(articles['Title'])):
        print('With title...', i)
        r = callBertServer(string=articles['Title'][i],id_=i).json()
        articles['Title_Embeddings'][i] = r['result'][0]

    articles.to_parquet("../../data/processed/model_TextFeat.parquet", compression='gzip')

if __name__ == '__main__':
    bert()