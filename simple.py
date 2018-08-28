from selenium import webdriver
import time
import os
import pandas as pd
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_dir():
    #http://www.karoltomala.com/blog/?p=622
    return os.path.dirname(os.path.abspath(__file__))

def run(zipcode):
    ua = UserAgent()
    caps = DesiredCapabilities.PHANTOMJS
    caps["phantomjs.page.settings.userAgent"] = ua.random
    browser = webdriver.PhantomJS(desired_capabilities=caps)
    browser.get("http://www.powertochoose.com")
    zipfield = browser.find_element_by_id('homezipcode')
    zipfield.click()
    zipfield.send_keys(str(zipcode))
    view_results = browser.find_element_by_id("view_all_results")
    view_results.click()
    time.sleep(1)
    price_eles = browser.find_elements_by_class_name("price")
    prices = [float(p.text[0:-1]) for p in price_eles]
    return prices, price_eles