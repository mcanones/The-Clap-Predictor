from src.demo.parser import ParserKey
from src.demo.prepareFeats import prepareFeats
from src.demo.getPrediction import getPrediction
from src.demo.makeReport import makeReport
from src.features.bert import bert, callBertServer
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings("ignore")
from sklearn.metrics.pairwise import cosine_similarity

def main():
    
    print('\n\n')  
    print ( ' ██████╗██╗      █████╗ ██████╗     ██████╗ ██████╗ ███████╗██████╗ ██╗ ██████╗████████╗ ██████╗ ██████╗')
    print ('██╔════╝██║     ██╔══██╗██╔══██╗    ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗')
    print ('██║     ██║     ███████║██████╔╝    ██████╔╝██████╔╝█████╗  ██║  ██║██║██║        ██║   ██║   ██║██████╔╝')
    print ('██║     ██║     ██╔══██║██╔═══╝     ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║██║██║        ██║   ██║   ██║██╔══██╗')
    print ('╚██████╗███████╗██║  ██║██║         ██║     ██║  ██║███████╗██████╔╝██║╚██████╗   ██║   ╚██████╔╝██║  ██║')
    print (' ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝         ╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝')
    print('\n\n')                                                                                                     
    
    ############ PREPARE DATA ################

    pars = ParserKey()

    article_df = prepareFeats(pars)

    df_model = article_df.drop(columns=['Author', 'Labels', 'Claps', 'Title', 'Text'])

    ################# MODEL ################# 

    filename = './models/model_NoText_def.sav'
    
    loaded_model = pickle.load(open(filename, 'rb'))
    
    print('Starting Prediction...\n\n')

    df_res = getPrediction(pars, loaded_model, df_model)

    ################# REPORT ################

    print(df_res)
    print('\n')
    print('Prediction done!\n\n')

    ########### RECOMMENDATION ##############

    df_label = article_df

    print('Calculating recommendation...\n\n')

    db_articles = pd.read_parquet("./data/processed/model_YesTextFeat.parquet").reset_index(drop=True)
    embedding = callBertServer(df_label['Title'][0], id_=0)['result'][0]

    db_articles['Distance'] = 0 
    for i in range(db_articles.shape[0]):
        db_articles['Distance'] = round(cosine_similarity(X=[np.array(db_articles['Title_Embeddings'][i])], Y=[np.array(embedding)])[0,0], 2)

    selected_articles = db_articles.sort_values(by=['Distance','Claps'], ascending=False)[:5]
    table = selected_articles[['Claps', 'Title', 'Publication', 'Reading_Time', 'Links', 'Bolded', 'Images', 'Distance']]

    print('Generating report...')

    makeReport(df_res, pars, article_df, table)

if __name__ == '__main__':
    main()


