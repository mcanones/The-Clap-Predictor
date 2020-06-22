"""

#------- WEB SCRAPING PUBLICATIONS WITH LONG ARCHIVES (MANY ARTICLES IN A MONTH)

pages={
        'Better Programming':'https://medium.com/better-programming/archive',
        'Towards Data Science':'https://towardsdatascience.com/archive',
        'Analytics Vidhya':'https://medium.com/analytics-vidhya/archive',
        'Becoming Human':'https://becominghuman.ai/archive',
        'Good Audience':'https://blog.goodaudience.com/archive',        
        'HeartBeat':'https://heartbeat.fritz.ai/archive',
        }
       
years=['2018','2019','2020']
months=[str(i).zfill(2) for i in range(1,13)]
days=[str(i).zfill(2) for i in range(1,32)]
suffix=['/'+year+'/'+month+'/'+day for year in years for month in months for day in days]

"""

#------- WEB SCRAPING PUBLICATIONS WITH SHORT ARCHIVES (FEW ARTICLES IN A YEAR)

pages={
        'Learn Data Science':'https://blog.exploratory.io/archive',
        'Applied Data Science':'https://medium.com/applied-data-science/archive',
        'TensorFlow':'https://medium.com/tensorflow/archive',
        'Inside Machine Learning':'https://medium.com/inside-machine-learning/archive',
        'metaflow-ai':'https://blog.metaflow.fr/archive',
        'Open Machine Learning Course':'https://medium.com/open-machine-learning-course/archive',
        'ML Review':'https://medium.com/mlreview/archive',
        'Machine Learning for Humans':'https://medium.com/machine-learning-for-humans/archive',
        'Machine Learnings':'https://machinelearnings.co/archive',
        'Learning New Stuff':'https://medium.com/learning-new-stuff/archive',
        'Center For Data Science':'https://medium.com/center-for-data-science/archive',
        'Deep Learning 101':'https://medium.com/deep-learning-101/archive',
        'Fusemachines':'https://medium.com/fusemachines/archive',
        'Datatau':'https://medium.com/datatau/archive',
        'Data Science Library':'https://medium.com/data-science-library/archive',
        'Master’s Program Computing Science at Simon Fraser University':'https://medium.com/sfu-cspmp/archive',
        'BBC DataScience':'https://medium.com/bbc-data-science/archive',
        'vickdata':'https://medium.com/vickdata/archive',
        'The Civis Journal':'https://medium.com/civis-analytics/archive/'
    }

years=['2018','2019','2020']
suffix=['/'+year for year in years]

