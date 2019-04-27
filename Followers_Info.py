import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
import pyodbc
from datetime import datetime as dtime
import random



admin_username=''
admin_password=''

chromedriver = './chromedriver.exe'
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, options=options)

    
try:
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    emailInput = driver.find_elements_by_css_selector('form input')[0]
    passwordInput = driver.find_elements_by_css_selector('form input')[1]
    emailInput.send_keys(admin_username)
    time.sleep(random.randrange(0, 2))
    passwordInput.send_keys(admin_password)
    time.sleep(random.randrange(0, 2))
    passwordInput.send_keys(Keys.ENTER)
    time.sleep(random.randrange(5, 7))
except:
    print('Error. Instagram Connection Failed.')
    driver.quit()

notify_button = driver.find_element_by_xpath('//button[text()="Not Now"]')
notify_button.click()
time.sleep(random.randrange(1, 2))


try:
    server = 'localhost'
    database = 'Sanjeh'
    username = 'sa'
    password = '1'
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cur = cnxn.cursor()
    res=cur.execute("SELECT Follower,Account FROM [dbo].[Followers] WHERE LEN(Follower)>0")
    Follower_List=res.fetchall()
except:
    print('Error. SQL Server Connection Failed.')
    driver.quit()


for l in Follower_List:
    driver.get("https://www.instagram.com/"+l[0]+"/")
    post_info_list=driver.find_elements(By.CSS_SELECTOR, '.g47SY')
    post_count=post_info_list[0].text
    post_count=int(post_count.replace(',',''))
    follower_count=post_info_list[1].get_attribute('title')
    follower_count=int(follower_count.replace(',',''))
    following_count=post_info_list[2].text
    following_count=int(following_count.replace(',',''))
    cur.execute('UPDATE Followers SET Post_Count=?,Follower_Count=?,Following_Count=? WHERE Follower=? ;',post_count,follower_count,following_count,l[0])
    cnxn.commit()

    
driver.quit()
cnxn.close()

