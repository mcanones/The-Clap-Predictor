import requests
from bs4 import BeautifulSoup
import re
from nltk.tokenize import word_tokenize

#--------------------------------------------------- L I N K S

def getLinks(url):
    try:

        # ------- Monitor Web Scraping in Terminal ---------- #
        print(url)

        # --------------------- Soup ------------------------ #
        data = requests.get(url, params={'p':'protected'}) # Access in private mode
        soup = BeautifulSoup(data.content, 'html.parser')  # Save HTML content

        # ------ Obtain Link + Publication DateTime --------- #
        links, times = [], []
        for link in soup.findAll('a', {'class': 'link link--darken'}):
            links.append(link.get('href')[:-33]) 
            times.append(link.time.get('datetime'))

        return links, times

    except Exception as e:
        print(e)

#--------------------------------------------------- A R T I C L E S
       
def getArticle(url):

    # --------------------- Soup ------------------------ #
    data = requests.get(url, params={'p':'protected'}) # Access in private mode
    soup = BeautifulSoup(data.content, 'html.parser')  # Save HTML content

    article = {}
    article['Author'] = soup.select_one('span div a').text                                         # Author (string)
    article['Title'] = soup.select_one('h1').text                                                  # Title  (string)
    article['Labels'] = ",".join([e.text for e in soup.select('ul')[-1]])                          # Labels (string)
    article['Code_Chunks'] = len(soup.find_all('pre')) if soup.find_all('pre') else 0              # Number of Code Chunks (int)
    article['Numbered_Lists'] = len(soup.find_all('ol')) if soup.find_all('ol') else 0             # Number of Numbered Lists (int)
    article['Bullet_Lists'] = len(soup.find_all('ul')) if soup.select_one('div h4 button') else 0  # Number of Bullet Lists (int)
    article['Links'] = len([e.get('href') for e in soup.select('p a')])                            # Number of Links (int)

    # ------------------ Reading Time ------------------ #
    s = soup.select_one('span > span > div').text
    article['Reading Time'] = int(re.findall("\d{1,2}", s)[-1])

    # -------------------- Body Text ------------------- #
    article['Text']=""
    for p in soup.findAll('p'): 
        article['Text'] += p.text+'\n'

    # --------------- Number of Images ----------------- #
    imgs=[]
    for link in soup.select('div.n.p figure img'):
        if link.get('src') and '?' not in link.get('src'):
            imgs.append(link.get('src'))
    article['Images'] = len(imgs)

    # ------------ Number of Words Bolded -------------- #
    bolded=""
    for x in soup.find_all('strong'):
        bolded += x.text 
    if bolded:  
        tokens = word_tokenize(bolded)
        bold_clean = [word for word in tokens if word.isalpha()]
        article['Bolded'] = len(bold_clean)
    else:
        article['Bolded'] = 0

    # ------------ Number of Words Italics -------------- #
    italics=""
    for x in soup.find_all('em'):
        italics += x.text
    if italics:  
        tokens = word_tokenize(italics)
        italics_clean = [word for word in tokens if word.isalpha()]
        article['Italics'] = len(italics_clean)
    else:
        article['Italics'] = 0

    # ------- Monitor Web Scraping in Terminal ---------- #
    print('*******REQUEST*******')
    print('Author...', article['Author'])
    print('Reading Time...', article['Reading Time'])
    print('Title...', article['Title'])
    print('Labels...', article['Labels'])
    print('Images...', article['Images'])
    print('Links...', article['Links'])
    print('Code Chunks...', article['Code_Chunks'])
    print('Numbered Lists...', article['Numbered_Lists'])
    print('Bullet Lists...', article['Bullet_Lists'])
    if article['Text']:
        print('Text...OK')
    if italics:
        print('Italics...', 'OK')
    if bolded:
        print('Bolded...', 'OK')

    return article


      







