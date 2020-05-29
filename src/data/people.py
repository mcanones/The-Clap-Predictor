from selenium import webdriver
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbModel import Base, Article
import os

from multiprocessing.pool import ThreadPool
import threading
from multiprocessing import Pool, cpu_count

"""
def people():

    print('Connecting to db...')
    engine = create_engine('sqlite:///' + '../../data/raw/prueba.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    articles = session.query(Article).all()

    for i,article in enumerate(articles):

        if not article.People:

           try:
                #driver = webdriver.Chrome('./chromedriver')
                link = article.Link
                driver.get(link)
                time.sleep(10)

                element = driver.find_elements_by_tag_name('h4.aq.cl.as.ds')
                element[0].click()
                time.sleep(3)
                people = driver.find_elements_by_tag_name('h2.aq.ds')

                for e in people:
                    if 'people' in e.text:
                        article.People=int(e.text.split(' ')[3])
                        session.commit()
                        print(f"Added People in article...{i} | Result: {e.text.split(' ')[3]}")

                #driver.quit()

           except KeyboardInterrupt:
                print('Exiting')
                os._exit(status=0)

           except:
               pass

    session.close()

if __name__ == '__main__':
    people()
    
"""

def getPeople(datalist):

    for article in datalist:

        try:
            driver = webdriver.Chrome('./chromedriver')
            driver.get(article.Link)
            time.sleep(10)

            element = driver.find_elements_by_tag_name('h4.aq.cl.as.ds')
            element[0].click()
            time.sleep(3)
            people = driver.find_elements_by_tag_name('h2.aq.ds')

            for e in people:
                if 'people' in e.text:
                    session.begin_nested()
                    article.People = int(e.text.split(' ')[3])
                    print(f"Added in article...{article.id} | People: {article.People}")

            driver.quit()

        except Exception as e:
            print(e)
            pass


def run_parallel_selenium_processes(datalist, selenium_func):

    pool = Pool()

    ITERATION_COUNT = cpu_count()-1

    count_per_iteration = len(datalist) / float(ITERATION_COUNT)

    for i in range(0, ITERATION_COUNT):
        list_start = int(count_per_iteration * i)
        list_end = int(count_per_iteration * (i+1))

        #     0  to 12405 -> CPU 1
        #  12405 to 24811 -> CPU 2
        #  24811 to 37217 -> CPU 3

        # pool.apply_async(f, args) --> Multi-args YES / Concurrence  YES / Blocking NO / Ordered-results NO
        pool.apply_async(selenium_func, datalist[list_start:list_end])


def people():

    print('Connecting to db...')

    #Create engine
    engine = create_engine('sqlite:///' + '../../data/raw/prueba.db')

    #Create a configured session class
    Session = sessionmaker(bind=engine)

    #Create an instance
    session = Session()

    #Query to obtain articles
    articles = session.query(Article).all()

    #Multiprocessing
    try:
        run_parallel_selenium_processes(datalist=articles, selenium_func=getPeople)
        session.commit()
        session.close()

    except KeyboardInterrupt:
        print('Exiting')
        os._exit(status=0)

if __name__ == '__main__':
    people()



