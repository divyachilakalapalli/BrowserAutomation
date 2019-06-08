import time
from selenium import webdriver

browser=webdriver.Chrome("/home/divya/Desktop/Python/webdriver/chromedriver")
browser.maximize_window()
browser.get("https://www.google.com/gmail/")

email_field=browser.find_element_by_id('identifierId')
email_field.clear()
email_field.send_keys('divyachilakalapalli.1999@gmail.com')

email_next_button=browser.find_element_by_id('identifierNext')
email_next_button.click()
time.sleep(2)

password_field=browser.find_element_by_name('password')
password_field.clear()
password_field.send_keys('netblockurll')

password_next_button=browser.find_element_by_id('passwordNext')
password_next_button.click()
time.sleep(4)

compose=browser.find_element_by_css_selector('.aic .z0 div')
compose.click()

toadd=browser.find_element_by_css_selector('.oj div textarea')
toadd.send_keys('divyachilakalapalli.1999@gmail.com')

subject=browser.find_element_by_css_selector('.aoD.az6 input')
subject.send_keys('message sent using python')

msg=browser.find_element_by_css_selector('.Ar.Au div')
msg.send_keys('Hey there,How are you??')
time.sleep(1)

send=browser.find_element_by_css_selector('.T-I.J-J5-Ji.aoO.v7.T-I-atl.L3')
send.click()

time.sleep(10)
browser.quit()
