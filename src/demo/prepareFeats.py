import pandas as pd
import sys
sys.path.append("..")
from src.demo.modelParams import labels, publications
from src.data.scrappingFunctions import get_article
from src.features.features import featuresFromTitleCol

def prepareFeats(pars):

    print('Obtaining article info...\n\n')

    article = get_article(pars.args.url)
    article['Days_since_publication'] = pars.args.days
    article_df = pd.DataFrame([article])
    
    print('\n')
    print('Adding Features...\n\n')

    #Publication
    if pars.args.publication in publications:
        article_df['Publication'] = pars.args.publication
    else:
        article_df['Publication'] = 'others'
    article_df['Publication'] = article_df['Publication'].astype('category')

    #Title
    article_df = featuresFromTitleCol(article_df) 

    #Labels
    article_df['Total_Labels'] = article_df['Labels'].apply(lambda labels: len(str(labels).split(",")))
    for label in article_df['Labels'][0].split(","):
        if f'Label_{label}' in labels:
            labels[f'Label_{label}']=1
    article_df = pd.concat([article_df, pd.DataFrame([labels])], axis=1)
    
    return article_df
