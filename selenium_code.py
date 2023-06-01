from selenium import webdriver
import time

DRIVER_PATH = './chromedriver.exe'
driver = webdriver.Chrome(executable_path = DRIVER_PATH)
# opens Google
driver.get("https://www.google.com")

time.sleep(5)

# open python official website
driver.get("https://www.python.org")

time.sleep(5)

# will go to Google
driver.back()

time.sleep(5)

# will go to python official website
driver.forward()

time.sleep(5)

# driver quit
driver.quit()
