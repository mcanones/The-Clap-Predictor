import pandas as pd
from scrappingFunctions import get_links
from scrappingVariables import pages, suffix
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbModel import Base, Article
from datetime import datetime, date

def links():

    print('Connecting to db...')
    engine = create_engine('sqlite:///' + '../../data/raw/project.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    #Loop each publisher
    for publisher,URL in pages.items():

        #Loop all the calendar for one publisher
        for url in [URL+s for s in suffix]:

            #Obtain articles links for a date
            links, times = get_links(url)
            
            #Connect db
            session=Session()

            #Loop through links
            for i,l in enumerate(links):
                
                #If link is not in db --> add 
                published = session.query(Article).filter_by(Link=l).scalar()
                if not published:
                    print('Saving in db...')
                    session.add(Article(Author=None, Claps=None, Reading_time=None, Title=None, Text=None, Labels=None, Publication = publisher, Time = datetime.strptime(times[i], "%Y-%m-%dT%H:%M:%S.%fZ"), Link = l, Date_Scrapping=date.today(), Images=None, Links=None, Code_Chunks=None, Numbered_Lists=None, Bullet_Lists=None, Bolded=None, Italics=None))
                    session.commit()
            
            #Close session
            session.close()  

if __name__ == '__main__':
    links()

