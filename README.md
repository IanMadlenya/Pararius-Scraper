## Basic tool for (gently) scraping rental home / appartment listings from Dutch housing site [Pararius.nl](http://www.pararius.nl), written in Python using Selenium.

Please note:

- scraping this website is only allowed for personal use (as per Pararius' Terms and Conditions).
- pararius.nl uses the anti-scraping services of Distil Networks so when running this scraper you will have to manually pass a Captcha every now and then
- this tool is structured in a such a way that it gently / ethically scrapes the pages it encounters (in other words, scraping data will take a while given the numerous "sleep" intervals embedded in the code)
- you will have to point the init_browser function to the local path of your webdriver (through the file_path variable)

The code takes as input search terms that would normally be entered on the Pararius home page. It extracts 11 variables from each home listing, which in turn is appended to a dataframed and saved to a CSV file.
It further takes the number of pages you would like to extract as an input (nb - each pararius results page contains 20 listings).

This tool was written by means of [Python 3.5.1](https://www.python.org/downloads/release/python-351/), [Selenium 3.4.3](https://pypi.python.org/pypi/selenium) and [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).

NB - inside the custom_page folder you will find a scraper that allows to scrape custom page ranges (instead of the base scraper that as a standard starts at page 1)

Example of the resulting dataframe:

```
  bedrooms                         city frequency     furniture inclusive  \
0        2  Amsterdam Stadsdeel Centrum       mnd  gemeubileerd      excl
1        1     Amsterdam Stadsdeel Oost       mnd  gemeubileerd      excl
2        2     Amsterdam Stadsdeel Oost       mnd   gestoffeerd      excl
3        3     Amsterdam Stadsdeel Oost       mnd   gestoffeerd      excl
4        2  Amsterdam Stadsdeel Centrum       mnd   gestoffeerd      excl
5        3     Amsterdam Stadsdeel Zuid       mnd   gestoffeerd      excl

                                                link price            street  \
0  https://www.pararius.nl/appartement-te-huur/am...  2450         Oude Waal
1  https://www.pararius.nl/appartement-te-huur/am...  2000     Blasiusstraat
2  https://www.pararius.nl/appartement-te-huur/am...  1330  Joris Ivensplein
3  https://www.pararius.nl/appartement-te-huur/am...  2300   Pretoriusstraat
4  https://www.pararius.nl/appartement-te-huur/am...  2950     Keizersgracht
5  https://www.pararius.nl/appartement-te-huur/am...  1975     Rooseveltlaan

  surface         type  zipcode
0      85  Appartement  1011 BZ
1      68  Appartement  1091 CS
2     103  Appartement  1087 BP
3      96  Appartement  1092 GB
4     120  Appartement  1016 EJ
5     100  Appartement  1078 NZ
```
