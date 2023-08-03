import os
from email.message import EmailMessage
import ssl, smtplib
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

from_email = os.getenv("EMAIL")
to_email = os.getenv("TO_EMAIL")
app_pass = os.getenv("APP_PASS")

os.environ['PATH'] += r'/Users/jacobyoo/Downloads/chromedriver_mac_arm64/chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
df_dict = pd.read_csv('all_prices.csv').to_dict("list")
original_df = pd.read_csv('all_prices.csv')

for index, row in original_df.iterrows():
    driver.get(row['url'])
    
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')

    price = float(soup.find('dd').text.strip("$"))
    product = soup.find('h1').text

    if product not in df_dict['product']:
        index_of_url = df_dict['url'].index(row['url'])
        df_dict['product'][index_of_url] = product
        df_dict['price'][index_of_url] = price
    elif price < float(row['price']):
        em = EmailMessage()
        em["From"] = from_email
        em["To"] = to_email
        em["Subject"] = f"DEAL FOR {product} ON PLUGIN BOUTIQUE WAS ${row['price']} AND NOW IS ${price}!"
        em.set_content(f"Dear Me,\n\nThe current price of {product} used to be ${row['price']} and is now ${price}!\n\nFrom,\n\n Me")

        context = ssl.create_default_context() # secures the message!
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(from_email, app_pass)
            smtp.sendmail(from_email, to_email, em.as_string())
        df_dict['price'][df_dict['product'].index(product)] = price
    else:
        df_dict['price'][df_dict['product'].index(product)] = price

df = pd.DataFrame.from_dict(df_dict)
df.to_csv('all_prices.csv', index=False)
    