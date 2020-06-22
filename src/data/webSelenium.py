from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import os

# -------------------------------------------- S E T T I N G S ----------------- #

os.environ['PATH'] = f'{os.environ["PATH"]}:{os.getcwd()}/drivers'  # Append driver to path
options = Options()  # Instance an Options object
options.headless = True  # Change attributes object -> Firefox headless mode

# -------------------------------------------- C L A P S ----------------------- #

def getClaps(link):

    try:

        driver = webdriver.Firefox(options=options)  # Open Firefox Webdriver
        driver.get(link)  # Point to Link
        time.sleep(5)  # Time to charge the page

        element = driver.find_elements_by_tag_name('h4 button')  # Find button
        element[1].click()  # Click button
        time.sleep(2)  # Time to charge the page

        people = driver.find_elements_by_tag_name('h2')  # Find number of claps
        for e in people:
            if 'people' in e.text:
                claps = int(e.text.split('people')[0].split(' ')[-2])
                driver.quit()
                return claps

    except Exception as e:
        print(e)
        driver.quit()
        pass
