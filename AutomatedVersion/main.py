import pandas as pd
from messager import Messager
from deal_scraper import DealScraper

df = pd.read_csv('all_prices.csv')

messager = Messager()
dealScraper = DealScraper()

for index, row in df.iterrows():
    
    dealScraper.scrape(row['url'])
    new_price = dealScraper.price
    product = dealScraper.product

    if product not in df['product']:
        df.loc[index, 'product'] = product
        df.loc[index, 'price'] = new_price
    elif new_price < float(row['price']):
        messager.send_email(product, row['price'], new_price)
    
    df.loc[index, 'price'] = new_price

df.to_csv("all_prices.csv", index=False)
    