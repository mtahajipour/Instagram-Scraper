import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.common.by import By
import pyodbc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


post_url=input('Enter Post URL: ')
user_name=input('Enter User Name: ')

server = 'localhost'
database = 'Sanjeh'
username = 'sa'
password = '1'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)



chromedriver = './chromedriver.exe'
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=chromedriver, options=options)

cursor = cnxn.cursor()
start = time. time()
driver.get(post_url)
time.sleep(random.randrange(0, 3))


while True:
    sl=driver.find_elements_by_link_text(user_name)
    sl[1].get_attribute('title')
    sl[1].send_keys(Keys.END)
    time.sleep(0.5)

    try:
            wait = WebDriverWait(driver, 30)
            #loadmore_button=wait.until(ec.element_to_be_clickable((By.XPATH,'//button[text()="Load more comments"]')))
            loadmore_button=wait.until(ec.element_to_be_clickable((By.XPATH,'//span[@aria-label="Load more comments"]')))
            time.sleep(0.5)
            loadmore_button.click()
    except:
            try:
                    loadmore_button = driver.find_element_by_xpath("//button[contains(text(), 'View all ')]")
                    loadmore_button.click()
                    sl[1].send_keys(Keys.HOME)
                    break

            except:
                    break

end = time. time()
print('The Process Terminates In',end - start, 'Seconds.')

start = time. time()
comment = driver.find_elements_by_class_name('gElp9')
for c in comment:
    try:
        container = c.find_element_by_class_name('C4VMK')
        name = container.find_element_by_class_name('_6lAjh').text
        content = container.find_element_by_tag_name('span').text
        content = content.replace('\n', ' ').strip().rstrip()
        cursor.execute('INSERT INTO Comments (Post_URL,Comment,Person) values (?,?,?);',post_url,content,name)
        cnxn.commit()
    except:
        pass
driver.quit()

end = time. time()
print('The Process Terminates In',end - start, 'Seconds.')
