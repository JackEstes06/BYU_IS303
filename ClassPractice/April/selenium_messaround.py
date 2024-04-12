import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from myLoginInfo import USERNAME, PASSWORD

browser = webdriver.Firefox()
browser.implicitly_wait(10)

browser.get("https://marriott.byu.edu/scheduler")

# LOGIN STUFF
browser.find_element(By.ID, "username").send_keys(USERNAME)
browser.find_element(By.ID, "password").send_keys(PASSWORD)
browser.find_element(By.ID, "byuSignInButton").click()
browser.find_element(By.ID, "dont-trust-browser-button").click()

# Navigate to a day 1 days in advance
browser.find_element(By.ID, "nextDate").click()
browser.find_element(By.ID, "nextDate").click()

# Schedule Room
# browser.find_element(By.CLASS_NAME, "timeUnitFree").click()
browser.find_elements(By.CLASS_NAME, "timeUnitFree")[0].click()
selectObj = Select(browser.find_element(By.ID, "end"))
# These next 2 lines do the same thing: grab the last element in the list
selectObj.options[-1].click()
# selectObj[len(selectObj.options)-1].click()
browser.find_element(By.ID, "terms").click()
# avoid this shortcut to finding things if possible
browser.find_element(By.XPATH, "/html/body/main/div/section/div/div/div[2]/div/div/div[3]/button[3]").click()


browser.close()
