import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initializing webdriver...
service = Service()
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options, service = service)

# Creating list variables to contain returns
NAME = []
PHONE = []
EMAIL = []
ADDRESS = []
OFFICES = []

# Driving URL...
driver.get("https://www.cbre.com/")

# Maximizing window
driver.maximize_window()

# Waiting for webpage to load elements
time.sleep(5)

# Accepting cookies
driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

# Allow to program to sleep before progressing...
time.sleep(3)

# Getting names of offices (in desperate manner... lol)
california = driver.find_element(By.ID, "section-3")

OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[1]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[2]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[3]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[4]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[6]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[7]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[8]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[9]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[10]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[11]/div/a").text)
OFFICES.append(california.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[12]/div/a").text)

# Clicking on Los Angeles
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[2]/div/a").click()

# Scrolling to desired location
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div/h2"))

# Clicking on 'Contacts'
driver.find_element(By.ID, "tab-contacts").click()

# Waiting for program to load
time.sleep(5)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to obtain result from items on webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = brokers.find_element(By.XPATH, f"//*[@id= '{broker_id[i]}']")
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    if i not in [1,2,5]:     
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(2) > a").get_attribute('href').replace('mailto:', ' ').strip()
    else:
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    
    NAME.append(temp_name)
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    ADDRESS.append(OFFICES[1])

    # Loop control
    i+=1

# Scrolling up
driver.execute_script('window.scrollTo(0, 0);')

# _____________________________________FOR CENTRAL VALLEY ______________________________________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

# Clicking on Central Valley
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[1]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()
    
    ADDRESS.append(OFFICES[0])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

# ________________________________________________________For Oakland______________________________________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(5)

# Clicking on Oakland
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[3]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    if i == 1:
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(2) > a").get_attribute('href').replace('mailto:', ' ').strip()
    else:
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[2])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

# ________________________________________________________For Orange County______________________________________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(5)

# Clicking on Orange County
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[4]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[3])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

#______________________________________________FOR PALTO ALTO _________________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on Pato Alto
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[4])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

#______________________________________________________________FOR ROSEVILLE______________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on Roseville
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[6]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[5])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

#______________________________________________FOR SACRAMENTO____________________________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on Sacramento
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[7]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[6])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

#____________________________________________FOR SAN DIEGO ___________________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on San Diego
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[8]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    if i == 3:
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()
    else:
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(2) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[7])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

#________________________________ FOR SAN FRANSICO _________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on San Franciscoe
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[9]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[8])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

#______________________________________________________________FOR SAN FRANCISCO PENINSULA_____________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on San Francisco Peninsula
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[10]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[9])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

#___________________________________________FOR SAN JOSE ________________________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on San Jose
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[11]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[10])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

# ____________________________________________________FOR WALNUT CREEK _________________________

# Clicking on Office...
driver.find_element(By.LINK_TEXT, "Offices").click()

# Scrolling to position to enable visibility of required web element.
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "//*[@id='ph_LargeModuleZoneSet']/div/section[2]/div/div/div/div/h2"))

# Clicking on Americas
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/h3[1]/button").click()

# Waiting for web-element (United States) to become clickable
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/section[2]/div/div/div/div/div/div[1]/ul/li[10]/a/span[2]"))).click()

# Getting page height
page_height = driver.execute_script('return document.body.scrollHeight')
to_height = page_height/5

# Scrolling down...
driver.execute_script(f"window.scrollTo(0, {to_height});")

# Clicking on California
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/h3[4]/button").click()

time.sleep(3)

# Scrolling down to Web-element
driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[5]/div/a"))

# Clicking on Walnut Creek
driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[2]/div/div[1]/div/div/div[1]/div/div/div[4]/div[12]/div/a").click()

time.sleep(2)

# Scrolling to desired location
driver.execute_script('arguments[0].scrollIntoView(true);', driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/section[3]/div/div[1]/div/div/h2"))

time.sleep(3)

# Obtaining IDs of web element.
brokers = driver.find_element(By.ID, "xUp__grid-3")
broker_id = []
ids = brokers.find_elements(By.CLASS_NAME, "cbre-c-xUp__grid-item")
for id in ids:
    broker_id.append(id.get_attribute('id'))

# Iteration to collect requested data from webpage
i = 0
# Loop control
while i < len(broker_id):
    # Loop action
    temp = driver.find_element(By.XPATH, f"//*[@id='{broker_id[i]}']/div/div/div/div")
    temp_name = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__header > h3 > a").text.strip()
    temp_phone = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(1) > a").get_attribute('href').replace('tel:', ' ').strip()
    if i == 1:
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(2) > a").get_attribute('href').replace('mailto:', ' ').strip()
    else:
        temp_mail = temp.find_element(By.CSS_SELECTOR, f"#{broker_id[i]} > div > div > div > div > div.cbre-c-gridCard__description > div.cbre-c-gridCard__person-info > ul > li:nth-child(3) > a").get_attribute('href').replace('mailto:', ' ').strip()

    ADDRESS.append(OFFICES[11])
    PHONE.append(temp_phone)
    EMAIL.append(temp_mail)
    NAME.append(temp_name)
    
    # Loop control
    i+=1

# Scroll up
driver.execute_script('window.scrollTo(0, 0);')

# Allow to program to sleep before progressing...
time.sleep(3)

# TRANSFORMING DATA TO DATAFRAME
data = {'NAME':NAME,
        'EMAIL': EMAIL,
        'PHONE NUMBER': PHONE,
        'OFFICE':ADDRESS}

df = pd.DataFrame(data)

df.to_csv("cbre.csv")

# Wait for three seconds...
time.sleep(3)

driver.quit()