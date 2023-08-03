import os
from email.message import EmailMessage
import ssl, smtplib
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

from_email = os.getenv("EMAIL")
to_email = os.getenv("TO_EMAIL")
app_pass = os.getenv("APP_PASS")


os.environ['PATH'] += r'/Users/jacobyoo/Downloads/chromedriver_mac_arm64/chromedriver'
website = 'https://www.pluginboutique.com/product/2-Effects/44-Saturation/3016-RC-20-Retro-Color'
driver = webdriver.Chrome()
driver.get(website)

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'lxml')

price = float(soup.find('dd').text.strip("$"))
product = soup.find('h1').text

if price < 99.95:
    em = EmailMessage()
    em["From"] = from_email
    em["To"] = to_email
    em["Subject"] = f"DEAL FOR {product} ON PLUGIN BOUTIQUE WAS $99.95 and now is ${price}!"
    em.set_content(f"Dear Me,\n\nThe current price of {product} used to be $99.95 and is now ${price}!\n\nFrom,\n\n Me")

    context = ssl.create_default_context() # secures the message!
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(from_email, app_pass)
        smtp.sendmail(from_email, to_email, em.as_string())
    