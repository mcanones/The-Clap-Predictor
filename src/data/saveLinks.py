from webRequests import getLinks
from publications import pages, suffix
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, Article
from datetime import datetime

def links():

    engine = create_engine('sqlite:///' + '../../data/raw/new_db.db') # Point to db
    Base.metadata.create_all(engine)     # Create table if it doesn't exist
    Session = sessionmaker(bind=engine)  # Create session instance

    for publisher,URL in pages.items():      # Loop each publisher
        for url in [URL+s for s in suffix]:  # Loop all the calendar for one publisher

            links, times = getLinks(url)     # Obtain list of links for a date (Ex: 1/1/2020)
            session=Session()                # Open session

            for i,l in enumerate(links):     # Loop in the list of links
                published = session.query(Article).filter_by(Link_Article=l).scalar()
                if not published:

                    session.add(Article(Link_Article = l, \
                                        DateTime_Publication = datetime.strptime(times[i], "%Y-%m-%dT%H:%M:%S.%fZ"), \
                                        Publication = publisher, \
                                        Author = None, \
                                        Title = None,  \
                                        Body_Text = None,  \
                                        Reading_Time = None, \
                                        N_Labels = None, \
                                        N_Images= None, \
                                        N_Links= None, \
                                        N_Code_Chunks= None, \
                                        N_Numbered_Lists= None, \
                                        N_Bullet_Lists= None, \
                                        N_Words_Bolded= None, \
                                        N_Words_Italics= None  ) )

                    session.commit()

            session.close()

if __name__ == '__main__':
    links()

