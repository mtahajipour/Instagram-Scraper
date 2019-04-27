import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
import pyodbc
import re


ht=''
Max_Post=100

chromedriver = './chromedriver.exe'
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, options=options)


driver.get("https://www.instagram.com/explore/tags/"+ht+"/")
time.sleep(random.randrange(3, 5))

try:
    h2tag=driver.find_element_by_tag_name('h2')
    txt=h2tag.text
    if txt=='''Sorry, this page isn't available.''':
        print('Error. No Result For This Topic')
        driver.quit()
except:
    pass

SCROLL_PAUSE_TIME = random.randrange(3, 5)
last_height = driver.execute_script("return document.body.scrollHeight")
post_url=[]

container_prev=[]
while True and len(post_url)<Max_Post:
    container =driver.find_elements(By.CSS_SELECTOR, '.v1Nh3 a')
    url_container=list(set(container)-set(container_prev))

    if len(url_container)==0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height and len(post_url)>=Max_Post:
            break
        last_height = new_height
        continue
    container_prev=container
    for c in url_container:
        post_url.append(c.get_attribute('href'))
    
    post_url=list(dict.fromkeys(post_url))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height and len(post_url)>=Max_Post:
        break
    last_height = new_height
    

server = 'localhost'
database = 'Sanjeh'
username = 'sa'
password = '1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

hashtags=[]
for l in post_url:
    driver.get(l)
    comment = driver.find_elements_by_class_name('gElp9')
    container = comment[0].find_element_by_class_name('C4VMK')
    content = container.find_element_by_tag_name('span').text
    content = content.replace('\n', ' ').strip().rstrip()
    caption=str(content)
    hashtags=re.findall(r'\#\w+', caption)
    for h in hashtags:
        cursor.execute('INSERT INTO [dbo].[Popular_Hashtags] ([Keyword],[Hashtags]) VALUES(?,?);',ht,h)
        cnxn.commit()
driver.quit()
