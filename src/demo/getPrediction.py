  
import pandas as pd 

def getPrediction(pars, loaded_model, df_model):

    #Start of prediction
    if pars.args.days-int(pars.args.temp/2) > 0:
        start = pars.args.days-int(pars.args.temp/2) 
    else:
        start = 0

    #Get results 
    res={}      
    for day in range(start,pars.args.days+int(pars.args.temp/2)):
        df_model['Days_since_publication'] = day
        result = loaded_model.predict_proba(df_model)[0][1]
        #print(loaded_model.predict_proba(df_model)[0])
        res[day]=result
        
    df_res = pd.DataFrame(res.values(), index=res.keys()).reset_index(drop=False)
    df_res.rename(columns = {0:'Probability_Top_Article','index':'Days_since_publication'}, inplace = True)
    df_res['Actual_day'] = 0
    df_res['Actual_day'].iloc[df_res[df_res['Days_since_publication']==pars.args.days].index] = 1
    
    return df_res