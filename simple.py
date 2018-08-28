from selenium import webdriver
import time
import os
import pandas as pd
import numpy as np
from fake_useragent import UserAgent
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime as dt

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
    prices = [float(p.text[0:-1])/100 for p in price_eles]
    return prices

def record(prices, filepath = None):
    if filepath is None:
        filepath = get_dir() + "/" + "simple.csv"
    today = dt.date.today().strftime("%Y-%m-%d")
    price_df = pd.DataFrame()
    price_df['Average'] = [np.mean(prices)]
    price_df['Min'] = [min(prices)]
    price_df.index = [today]
    if os.path.isfile(filepath) == True:
        prev_df = pd.read_csv(filepath, index_col = 0)
        if prev_df.index[-1] != today:
            price_df = prev_df.append(price_df)
    price_df.to_csv(filepath)

def get_settings(settings = None):
    if settings is None:
        settings = get_dir() + "/" + "settings.cfg"
    try:
        with open(settings, "r") as f:
            settings2 = f.read().split('\n')
    except IOError as e:
        print("You didn't create a settings file!")
        raise(e)
    sid = settings2[1][19:]
    auth_key = settings2[2][18:]
    mobile = settings2[3][19:]
    days = int(settings2[4][31:])
    return sid, auth_key, mobile, days