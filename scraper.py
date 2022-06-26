from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"

broswer = webdriver.Chrome("chromedriver.exe")
broswer.get(START_URL)

time.sleep(10)

def scrape():
    headers = ["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[]

    soup = BeautifulSoup(broswer.page_source,"html.parser")

    for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
        li_tags = ul_tag.find_all("li")
        temp_list=[]
        for index,li_tag in enumerate(li_tags):
            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
        planet_data.append(temp_list)
    
    print(planet_data)


scrape()
