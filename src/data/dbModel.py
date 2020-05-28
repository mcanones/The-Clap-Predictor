from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Date

Base = declarative_base()

class Article(Base): 
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    Author = Column(String(50))
    Claps = Column(Integer)
    Reading_Time = Column(Integer)
    Time = Column(DateTime())
    Publication = Column(String(100))
    Title = Column(String(50))
    Text = Column(String(10000))
    Link = Column(String(300))
    Labels = Column(String(300))
    Date_Scrapping = Column(Date())
    Images = Column(Integer)
    Links = Column(Integer)
    Code_Chunks =  Column(Integer)
    Numbered_Lists =  Column(Integer)
    Bullet_Lists =  Column(Integer)
    Bolded = Column(Integer)
    Italics = Column(Integer)
    
    def __init__(self, Author, Claps, Reading_time, Title, Text, Labels, Time, Publication, Link, Date_Scrapping, Images, Links, Code_Chunks, Numbered_Lists, Bullet_Lists, Bolded, Italics):
        self.Author = Author
        self.Claps = Claps
        self.Reading_Time = Reading_time
        self.Time = Time
        self.Publication = Publication
        self.Title = Title
        self.Text = Text
        self.Link = Link
        self.Labels = Labels
        self.Date_Scrapping = Date_Scrapping
        self.Images = Images
        self.Links = Links
        self.Code_Chunks = Code_Chunks
        self.Numbered_Lists = Numbered_Lists
        self.Bullet_Lists = Bullet_Lists
        self.Bolded = Bolded
        self.Italics = Italics

