#--------------------------------------------------- A L C H E M Y ------------------#

from sqlalchemy import create_engine
from webRequests import getArticle
from webSelenium import getClaps

#---------------------------------- M U L T I P R O C E S S I N G  ------------------#

from multiprocessing import Pool

#------------------------------ A R T I C L E S  ------------------------------------#

def func(article):

    try:

        engine = create_engine('sqlite:///' + '../../data/raw/new_db.db')  # Point to db

        if not article.Title:

            data = getArticle(article.Link_Article)  # Collect data

            print(data['Author'])
            print(article.Author)
            #article.Author = data['Author']
            #article.Title = data['Title']
            #article.Body_Text = data['Text']
            #article.Reading_Time = data['Reading Time']
            #article.N_Labels = data['Labels']
            #article.N_Images = data['Images']
            #article.N_Links = data['Links']
            #article.N_Code_Chunks = data['Code_Chunks']
            #article.N_Numbered_Lists = data['Numbered_Lists']
            #article.N_Bullet_Lists = data['Bullet_Lists']
            #article.N_Words_Bolded = data['Bolded']
            #article.N_Words_Italics = data['Italics']

        with engine.connect() as connection:

            connection.execute(claps.insert(), {"People": getClaps(article.Link_Article),\
                                                "Date_Scraping ": date.today(),\
                                                "id_articles": article.id
                                                })

    except KeyboardInterrupt:
        print('Exiting')
        os._exit(status = 0)

    except Exception as e:
        print(e)
        pass

#------------------------------ P O O L ---------------------------------------------#

def multiprocessingPool():

    pool = Pool()

    try:

        engine = create_engine('sqlite:///' + '../../data/raw/new_db.db')   # Point to db

        with engine.connect() as connection:

            articles = connection.execute('SELECT * FROM articles')
            pool.map(func, articles)
            #pool.terminate()
            #pool.join()

    except KeyboardInterrupt:
        print('Exiting')
        os._exit(status=0)

if __name__ == '__main__':
    multiprocessingPool()



