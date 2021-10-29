import requests
from selenium import webdriver
import time
driver=webdriver.Chrome("/home/divya/Desktop/Python/webdriver/chromedriver")
driver.get('http://www.irctc.com/')

links = driver.find_elements_by_css_selector("a")

print("Broken links in the website http://www.irctc.com/ are:")
for link in links:
    r = requests.head(link.get_attribute('href'))
    if(r.status_code>=400):
        print(link.get_attribute('href'), r.status_code)
time.sleep(10)
driver.quit()
