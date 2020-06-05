##################################################### S E L E N I U M

from selenium import webdriver
from multiprocessing import Pool, cpu_count
import time
from dbModel import Article

import os
os.environ['PATH'] = f'{os.environ["PATH"]}:{os.getcwd()}/drivers'
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True

####################################################### A L C H E M Y 

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///' + '../../data/raw/people.db')
Session = sessionmaker(bind=engine)

######################################################################

def getPeople(link):

    try:

        driver = webdriver.Firefox(options=options)
        driver.get(link)
        time.sleep(5)

        element = driver.find_elements_by_tag_name('h4 button')
        element[1].click()
        time.sleep(2)
        people = driver.find_elements_by_tag_name('h2')

        for e in people:

            if 'people' in e.text:

                #Open session
                session = Session()

                #Find article
                article = session.query(Article).filter_by(Link=link).scalar()
                
                article.People = int(e.text.split('people')[0].split(' ')[-2])
                #article.People = int(e.text.split(' ')[3])
                print(f"Added in article...{article.id} | People: {article.People} | Link: {article.Link}")

                session.commit()
                session.close()
            
        driver.quit()

    except Exception as e:
        print(e)
        driver.quit()
        pass

def run_parallel_selenium_processes(datalist, selenium_func):
    
    #datalist = datalist[6000:]

    pool = Pool()

    ITERATION_COUNT = cpu_count()-1 

    count_per_iteration = len(datalist) / float(ITERATION_COUNT)

    for i in range(0, ITERATION_COUNT):                   
        list_start = int(count_per_iteration * i)         
        list_end = int(count_per_iteration * (i+1))      

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


