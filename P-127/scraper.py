from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("C:/Users/ibrah/OneDrive/Desktop/WhiteHatJr projects/All files/C-127/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(20)

scrape_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
    ## ADD CODE HERE ##
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
        table_cols = row.find_all('td')
        temp_list = []
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
        scrape_data.append(temp_list)


        
# Calling Method    
scrape()

stars_data = []
for i in range(0, len(scrape_data)):
    Star_names = scrape_data[i][1]
    Distance = scrape_data[i][3]
    Mass = scrape_data[i][5]
    Radius = scrape_data[i][6]
    Lum = scrape_data[i][7]
    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)


# Define Header
headers = ["Star_names", "Distance", "Mass", "Radius", "Luminosity"]

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(stars_data, columns = headers)


# Convert to CSV
star_df_1.to_csv("scrapped_data.csv", index = True, index_label = "id")
    


