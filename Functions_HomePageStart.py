# Scraper functions, which in turn are sourced in runfile.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import pandas as pd
import time
from random import randint

# Initialize browser & wait for 15 seconds

def init_browser(file_path):
    browser = webdriver.Chrome(executable_path=file_path)
    browser.implicitly_wait(15)
    return browser

# Open target website

def navigate_to_website(browser):
    browser.get('https://www.pararius.nl')

# Wait until site elements are loaded on the home page and enter search term

def enter_search_term(browser, search_term):

    wait = WebDriverWait(browser, 15)

    try:
        search_bar = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//input[@type='text'])[2]")))
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//input[@type='submit'])[2]")))
        search_bar.click()
        time.sleep(randint(10, 15))
        search_bar.clear()
        time.sleep(randint(10, 15))
        search_bar.send_keys(search_term)
        time.sleep(randint(10, 15))
        button.click()
        print("home page search-button has been clicked")
        time.sleep(randint(15, 20))
        return True
    except (TimeoutException, NoSuchElementException):
        return False

# Scrape the resulting page and move on to the next page until hitting the predefined lastpage. All results are stored in a csv-file

def get_data(browser, lastpage, search_term):

    data = []

    keep_going = True
    wait = WebDriverWait(browser, 15)
    page = 2
    reference = str(page)

    while keep_going and page <= lastpage:

        try:
            for item in browser.find_elements_by_css_selector("li.property-list-item-container"):

                type, street = item.find_element_by_css_selector("h2>a").text.split(" ", 1)

                surface = item.find_element_by_css_selector("li.surface").text.replace(" m²", "")
                bedrooms = item.find_element_by_css_selector("li.bedrooms").text[:1]
                furniture = item.find_element_by_css_selector("li.furniture").text

                totalprice = item.find_element_by_css_selector("p.price").text.lstrip('€ ')
                price, rest = totalprice.split(" ", 1)
                price = price.rstrip(',-').replace(".", "")

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

            print("page extracted")
            time.sleep(randint(25, 35))

            browser.find_element_by_xpath("//a[contains(@href,'huurwoning') and contains(., '" + reference + "')]").click()
            page += 1
            print("link to next page has been clicked")
            time.sleep(randint(5, 15))

        except (TimeoutException, NoSuchElementException):
            keep_going = False

    browser.close()
    df = pd.DataFrame(data)
    df.to_csv(search_term+"uptopage"+str(lastpage)+".csv", sep=';', encoding='utf-8')
    print(df)


