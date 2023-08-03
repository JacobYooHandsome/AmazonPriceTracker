import os
from selenium import webdriver
import time
from bs4 import BeautifulSoup

os.environ['PATH'] += r'/home/jacobyooguapo/pluginboutique-deal-checker'
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

class DealScraper():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.price = 0
        self.product = ""
    
    def scrape(self, url):
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        self.price = float(soup.find('dd').text.strip("$"))
        self.product = soup.find('h1').text
    
    
    
    
    