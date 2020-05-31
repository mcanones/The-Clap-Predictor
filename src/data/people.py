##################################################### S E L E N I U M

from selenium import webdriver
from multiprocessing import Pool, cpu_count
import time
import os

####################################################### A L C H E M Y

from dbModel import Base, Article
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///' + '../../data/raw/prueba.db')
Session = sessionmaker(bind=engine)

######################################################################

def getPeople(link):

    try:

        driver = webdriver.Chrome('./chromedriver')
        driver.get(link)
        time.sleep(3)

        element = driver.find_elements_by_tag_name('button')
        element[2].click()
        time.sleep(2)
        people = driver.find_elements_by_tag_name('h2')

        for e in people:

            if 'people' in e.text:

                #Open session
                session = Session()

                #Find article
                article = session.query(Article).filter_by(Link=link).scalar()

                article.People = int(e.text.split(' ')[3])
                print(f"Added in article...{article.id} | People: {article.People}")

                session.commit()
                session.close()

                """ Doesn't work - why?
                with engine.connect() as connection:
                    article = connection.execute(f" SELECT * FROM articles WHERE Link = '{link}' ")
                    #article.People = int(e.text.split(' ')[3])
                    #print(f"Added in article...{article.id} | People: {article.People}")
                """

        driver.quit()

    except Exception as e:
        print(e)
        pass

def run_parallel_selenium_processes(datalist, selenium_func):

    pool = Pool()

    ITERATION_COUNT = cpu_count()-1 # 4 - 1

    count_per_iteration = len(datalist) / float(ITERATION_COUNT)

    for i in range(0, ITERATION_COUNT):                   #     0  to 12405 -> CPU 1
        list_start = int(count_per_iteration * i)         #  12405 to 24811 -> CPU 2
        list_end = int(count_per_iteration * (i+1))       #  12405 to 24811 -> CPU 2

        # pool.map(f, args) --> Multi-args NO / Concurrence  YES / Blocking YES / Ordered-results YES
        pool.map(selenium_func, datalist[list_start:list_end])

def people():

    print('Connecting to db...')

    with engine.connect() as connection:
        articles = connection.execute('SELECT * FROM articles')
        links = [article.Link for article in articles if not article.People]

    try:
        run_parallel_selenium_processes(datalist=links, selenium_func=getPeople)

    except KeyboardInterrupt:
        print('Exiting')
        os._exit(status=0)

if __name__ == '__main__':
    people()



