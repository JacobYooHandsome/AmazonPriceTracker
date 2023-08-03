import requests
import os
from selenium import webdriver
import time
from bs4 import BeautifulSoup

os.environ['PATH'] += r'/Users/jacobyoo/Downloads/chromedriver_mac_arm64/chromedriver'
website = 'https://www.pluginboutique.com/product/2-Effects/44-Saturation/3016-RC-20-Retro-Color'
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(website)

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')

price = soup.find('dd').text

# r = requests.get("https://www.pluginboutique.com/product/2-Effects/44-Saturation/3016-RC-20-Retro-Color").text
# soup = BeautifulSoup(r, "lxml")
# price = soup.find('dd')
# print(price)


