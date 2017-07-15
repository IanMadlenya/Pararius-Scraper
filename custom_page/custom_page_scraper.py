from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time
from random import randint




browser = webdriver.Chrome('/Users/Mike/Downloads/chromedriver')

browser.implicitly_wait(10)
wait = WebDriverWait(browser, 30)

urls = [
        'https://www.pararius.nl/huurwoningen/amsterdam/page-',
    ]

data = []

pagerange = range (41,51)

for url in urls:
    for page in pagerange:
        browser.get(url + str(page))
        # wait for the page to load
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.type")))

        for item in browser.find_elements_by_css_selector("li.property-list-item-container"):
            type, street = item.find_element_by_css_selector("h2>a").text.split(" ", 1)

            surface = item.find_element_by_css_selector("li.surface").text.replace(" m²","")
            bedrooms = item.find_element_by_css_selector("li.bedrooms").text[:1]
            furniture = item.find_element_by_css_selector("li.furniture").text

            totalprice = item.find_element_by_css_selector("p.price").text.lstrip('€ ')
            price, rest = totalprice.split(" ", 1)
            price = price.rstrip(',-').replace(".","")

            frequency, inclusive = rest.split(" ", 1)
            frequency = frequency.lstrip('/')
            inclusive = inclusive.lstrip('(').rstrip('.)')

            zipcode1, zipcode2, city = item.find_element_by_css_selector("ul.breadcrumbs").text.split(" ", 2)
            zipcode = zipcode1 + " " + zipcode2

            link = item.find_element_by_css_selector("h2>a").get_attribute('href')

            data.append({
                "type": type,
                "street": street,
                "zipcode": zipcode,
                "city": city,
                "surface": surface,
                "bedrooms": bedrooms,
                "furniture": furniture,
                "price": price,
                "frequency": frequency,
                "inclusive": inclusive,
                "link": link,
            })

        time.sleep(randint(25, 45))

browser.close()
df = pd.DataFrame(data)
df.to_csv("AmsterdamPage"+str(min(pagerange))+"to"+str(max(pagerange))+".csv", sep=';', encoding='utf-8')
print(df.head(n=6))
