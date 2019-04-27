import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
import pyodbc



admin_username=''
admin_password=''
account=''
Min_Followers=10000

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


driver.get("https://www.instagram.com/"+account+"/")
time.sleep(random.randrange(3, 5))

try:
    h2tag=driver.find_element_by_tag_name('h2')
    txt=h2tag.text
    if txt=='''Sorry, this page isn't available.''':
        print('Error. No Result For This Topic')
        driver.quit()
except:
    pass

post_info_list=driver.find_elements(By.CSS_SELECTOR, '.g47SY')
follower_count=post_info_list[1].get_attribute('title')
follower_count=follower_count.replace(',','')

Min_Followers=min(Min_Followers,int(follower_count))

l=driver.find_elements_by_css_selector("ul li a")
l[0].click()
time.sleep(2)

Followers=[]
Ercount=0
followersList_Prev=[]
while True:
    followersList = driver.find_elements_by_css_selector('div[role=\'dialog\'] ul li a')
    New_followersList=list(set(followersList)-set(followersList_Prev))
    followersList_Prev=followersList
    try:
        for f in New_followersList:
            Followers.append(f.get_attribute('title'))
    except:
        Ercount=Ercount+1
        Followers.append('Error')
        pass
    if len(New_followersList)!=0:
        Followers=list(dict.fromkeys(Followers))
    
    if len(Followers)+Ercount >= Min_Followers:
        break
    followersList[0].send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)

driver.quit()

server = 'localhost'
database = 'Sanjeh'
username = 'sa'
password = '1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cur = cnxn.cursor()


for f in Followers:
    cur.execute('INSERT INTO Followers (Account,Follower) values (?,?)',account,f)
    cnxn.commit()

cnxn.close()
