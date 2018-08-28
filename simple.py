from selenium import webdriver
import time

def run(zipcode):
    browser = webdriver.PhantomJS()
    browser.get("http://www.powertochoose.com")
    zipfield = browser.find_element_by_id('homezipcode')
    zipfield.click()
    zipfield.send_keys(str(zipcode))
    view_results = browser.find_element_by_id("view_all_results")
    view_results.click()
    time.sleep(1)
    price_eles = browser.find_elements_by_class_name("price")
    prices = [float(p.text[1:-1]) for p in price_eles]
    return prices