from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

driver = webdriver.Chrome()
data_dict = {}
try:
    driver.get(url="https://store.steampowered.com/search/?supportedlang=russian&tags=19&os=win&hidef2p=1&filter=topsellers&ndl=1")
    time.sleep(3)
    for i in range(1, 101):
        game_name = driver.find_element(By.CSS_SELECTOR, f"#search_resultsRows > a:nth-child({i}) > div.responsive_search_name_combined > div.col.search_name.ellipsis > span")                                             
        print(game_name.text)  
        game_price =  driver.find_element(By.CSS_SELECTOR, f"#search_resultsRows > a:nth-child({i}) > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div > div > div > div")
        print(game_price.text) 
        game_price = game_price.text
        game_price = game_price.split('\n')[0]
        data_dict[game_name.text] = game_price
        df = pd.DataFrame(data=data_dict, columns=['Game_Name, Game_Price'])
        df.to_csv("data.csv")                                      
except Exception as ex:
    print(ex.__class__.__name__)
finally:
    driver.close()
    driver.quit()

