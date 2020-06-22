from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Date

Base = declarative_base()

#------------------------------------- T A B L E  ->  A R T I C L E S

class Article(Base):  # Article inherits from Class Base

    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)     # Primary Key
    Link_Article = Column(String(300))         # Link
    Author = Column(String(50))                # Categorical features (CONTENT)
    Publication = Column(String(100))
    Title = Column(String(50))
    Body_Text = Column(String(10000))
    DateTime_Publication = Column(DateTime())  # Numerical features (FORMAT)
    Reading_Time = Column(Integer)
    N_Labels = Column(String(300))
    N_Images = Column(Integer)
    N_Links = Column(Integer)
    N_Code_Chunks =  Column(Integer)
    N_Numbered_Lists =  Column(Integer)
    N_Bullet_Lists =  Column(Integer)
    N_Words_Bolded = Column(Integer)
    N_Words_Italics = Column(Integer)

    def __init__(self, Link_Article, \
                 Author, Publication, Title, Body_Text, \
                 DateTime_Publication, Reading_Time, \
                 N_Labels, N_Images, N_Links, \
                 N_Code_Chunks, N_Numbered_Lists, N_Bullet_Lists, \
                 N_Words_Bolded, N_Words_Italics):

        self.Link_Article = Link_Article # Defining attributes after class construction
        self.Author = Author
        self.Publication = Publication
        self.Title = Title
        self.Body_Text = Body_Text
        self.DateTime_Publication = DateTime_Publication
        self.Reading_Time = Reading_Time
        self.N_Labels = N_Labels
        self.N_Images = N_Images
        self.N_Links = N_Links
        self.N_Code_Chunks = N_Code_Chunks
        self.N_Numbered_Lists = N_Numbered_Lists
        self.N_Bullet_Lists = N_Bullet_Lists
        self.N_Words_Bolded = N_Words_Bolded
        self.N_Words_Italics = N_Words_Italics

#------------------------------------------- T A B L E  ->  C L A P S

class People(Base):

    __tablename__ = 'claps'
    id = Column(Integer, primary_key=True)
    id_articles = Column(Integer)
    Date_Scraping = Column(Date())
    People = Column(Integer)

    def __init__(self, id_articles, Date_Scraping, People):
        self.id_articles = id_articles # Defining attributes after class construction
        self.Date_Scraping = Date_Scraping
        self.People = People





