import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
import pyodbc
from datetime import datetime as dtime


post_url=''

try:
    server = 'localhost'
    database = 'Sanjeh'
    username = 'sa'
    password = '1'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
except:
    print('Error. SQL Connection Failed.')

chromedriver = './chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1200x600')
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, options=options)

curs = cnxn.cursor()
try:
    driver.get(post_url)
    elem = driver.find_element(By.CSS_SELECTOR, '._1o9PC')
    post_date=elem.get_attribute('datetime')
except:
    pass
curs.execute('INSERT INTO [dbo].[Posts] (Post_URL,Post_Date) VALUES (?,?);',post_url,post_date)
cnxn.commit()

like_count=-1
view_count=-1
try:
        try:
                container = driver.find_element_by_class_name('zV_Nj')
                like_count = container.find_element_by_tag_name('span').text
                like_count=int(like_count.replace(',',''))

                
        except:
                container = driver.find_element_by_class_name('vcOH2')
                view_count = container.find_element_by_tag_name('span').text
                view_count=int(view_count.replace(',',''))
except:
        pass

curs = cnxn.cursor()
curs.execute('UPDATE [dbo].[Posts] SET Like_Count=? , View_Count=? WHERE Post_URL=?;',like_count,view_count,post_url)
cnxn.commit()

cnxn.close()
driver.quit()


