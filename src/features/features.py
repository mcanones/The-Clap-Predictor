import textstat
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from .cleaning import notLabels
import sys
sys.path.append("..") 

def featuresFromPublicationCol(df):
    #Small Publications --> Others
    renam={'Machine Learnings':'others','Learn Data Science':'others','Inside Machine Learning':'others',
       'Center For Data Science':'others','Data Science Library':'others','Applied Data Science':'others',
       'BBC DataScience':'others','The Civis Journal':'others','vickdata':'others','Datatau':'others',
       'ML Review':'others','metaflow-ai':'others','Master’s Program Computing Science at Simon Fraser University':'others',
       'Fusemachines':'others','Learning New Stuff':'others', 'TensorFlow':'others', 'Open Machine Learning Course':'others',
       'Machine Learning for Humans':'others', 'Deep Learning 101':'others'}
       
    df['Publication'] = df['Publication'].replace(renam)
    return df

def featuresFromTitleCol(df):
    #Number of words 
    df['Length_Title'] = df['Title'].apply(lambda title: len(str(title).split(" ")))
    #Readability level
    df['Title_read_lvl'] = df['Title'].map(textstat.flesch_kincaid_grade)
    #Sentiment analysis 
    sia=SIA()
    df['Sentiment_Title'] = df['Title'].apply(lambda row: sia.polarity_scores(row)['compound'])  #preprocess_text()
    return df 

def featuresFromTimeCol(df):
    #df['Year'] = df.Time.dt.year
    #df['Day_of_week'] = df.Time.dt.dayofweek
    #df['Hour'] = df.Time.dt.hour
    #df['Month'] = df.Time.dt.month
    df['Days_since_publication'] = (df['Date_Scrapping'].dt.date - df['Time'].dt.date).dt.days
    df.drop(columns=['Time', 'Date_Scrapping'], inplace=True) 
    return df  

def featuresFromLabelsCol(df):
    #Col with total number of labels
    df['Total_Labels'] = df['Labels'].apply(lambda labels: len(str(labels).split(",")))

    #################### SELECT MOST REPRESENTATIVE LABELS #################### 
    ###########################################################################

    #Expand labels as columns for each article 
    df_labels = df.Labels.str.split(",",expand=True)
    #We take 1st and 2nd label 
    df_labels = df_labels[[0,1]]
    #Clean long strings which are not labels 
    for i in range(2):
        df_labels[i] = df_labels[i].apply(notLabels)
    #Obtain set of important labels 
    set_label1=set(df_labels[0].value_counts()[:20].index.tolist())
    set_label2=set(df_labels[1].value_counts()[:20].index.tolist())
    final_set_labels = set_label1.union(set_label2.difference(set_label1))
    print('Total Labels: ', len(final_set_labels))
    #Create columns for each label
    for label in final_set_labels:
        df['Label_'+label]=df['Labels'].str.contains(label, regex=True).astype(int)

    ########################################################################### 
    ########################################################################### 

    df.drop(columns='Labels', inplace=True)
    return df








