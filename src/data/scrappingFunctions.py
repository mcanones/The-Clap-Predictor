import requests
from bs4 import BeautifulSoup
import os
import re
from nltk.tokenize import word_tokenize

def get_links(url):
    try:
        print(url)
      
        data = requests.get(url, params={'p':'protected'})
        soup = BeautifulSoup(data.content, 'html.parser')
        links=[]
        times=[]
        for link in soup.findAll('a', {'class': 'link link--darken'}):
            links.append(link.get('href')[:-33]) 
            times.append(link.time.get('datetime')) 
        return links, times
    except Exception as e:
        print(e)
       
def get_article(url):

    article={}
    print('*******REQUEST*******')
   
    data = requests.get(url, params={'p':'protected'})
    soup = BeautifulSoup(data.content, 'html.parser')
  
    article['Author'] = soup.select_one('span div a').text 
    print('Author...', article['Author'])

    article['Claps'] = convert_string_to_numeric(soup.select_one('div h4 button').text) if soup.select_one('div h4 button') else 0
    print('Claps...',  article['Claps'])

    s =soup.select_one('span > span > div').text
    article['Reading Time'] = int(re.findall("\d{1,2}", s)[-1])  
    print('Reading Time...', article['Reading Time'])

    article['Title'] = soup.select_one('h1').text 
    print('Title...', article['Title'])

    article['Labels'] = ",".join([e.text for e in soup.select('ul')[-1]])
    print('Labels...', article['Labels'])

    article['Text']=''
    for p in soup.findAll('p'): 
        article['Text'] += p.text+'\n'
    if article['Text']: 
        print('Text...OK')

    imgs=[]
    for link in soup.select('div.n.p figure img'):
        if link.get('src') and '?' not in link.get('src'):
            imgs.append(link.get('src'))
    article['Images'] = len(imgs)  
    print('Images...', article['Images'])

    links = [e.get('href') for e in soup.select('p a')]
    article['Links'] = len(links)  
    print('Links...', article['Links'])
    
    ### Format

    article['Code_Chunks'] = len(soup.find_all('pre') ) if soup.find_all('pre') else 0 
    print('Code Chunks...', article['Code_Chunks'])

    article['Numbered_Lists'] = len(soup.find_all('ol')) if soup.find_all('ol') else 0
    print('Numbered Lists...', article['Numbered_Lists']) 

    article['Bullet_Lists'] = len(soup.find_all('ul')) if soup.select_one('div h4 button') else 0
    print('Bullet Lists...', article['Bullet_Lists']) 

    bolded=""
    for x in soup.find_all('strong'):
        bolded += x.text 
    if bolded:  
        tokens = word_tokenize(bolded)
        bold_clean = [word for word in tokens if word.isalpha()]
        article['Bolded'] = len(bold_clean)
        print('Bolded...', 'OK')
    else:
        article['Bolded'] = 0

    italics=""
    for x in soup.find_all('em'):
        italics += x.text
    if italics:  
        tokens = word_tokenize(italics)
        italics_clean = [word for word in tokens if word.isalpha()]
        article['Italics'] = len(italics_clean)
        print('Italics...', 'OK') 
    else:
        article['Italics'] = 0

    return article

def convert_string_to_numeric(s):
    if 'K' in s:
        return int(float(s.split('K')[0])*10**3)
    return int(s)
      







