from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbModel import Base, Article
from scrappingFunctions import get_article
import os 

def articles():

    engine = create_engine('sqlite:///' + '../../data/raw/project.db')    
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)  
    session = Session()

    articles = session.query(Article).all()

    for article in articles[3163:]: #CHANGE THIS
        try:
            data = get_article(article.Link)

            published = session.query(Article).filter_by(Title = data['Title']).scalar()
            if published: #CHANGE THIS
                session.begin_nested()
                print('...SAVING IN DB...')
                article.Author = data['Author']
                article.Claps = data['Claps']
                article.Reading_Time = data['Reading Time']
                article.Title = data['Title']
                article.Text = data['Text']
                article.Labels = data['Labels']
                article.Images = data['Images']
                article.Links = data['Links']
                article.Code_Chunks = data['Code_Chunks']
                article.Numbered_Lists = data['Numbered_Lists']
                article.Bullet_Lists = data['Bullet_Lists']
                article.Bolded = data['Bolded']
                article.Italics = data['Italics']
            session.commit()

        except KeyboardInterrupt: 
            print('Exiting')
            os._exit(status = 0)

        except:  # exceptions format page
            pass

    session.close()

if __name__ == '__main__':
    articles()