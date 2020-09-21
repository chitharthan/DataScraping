import selenium
import csv
from selenium import webdriver
from optparse import Option
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument("--disable-notification")
driver = webdriver.Chrome("/Users/ADMIN/Documents/chromedriver.exe", chrome_options=options)
driver.maximize_window()
driver.implicitly_wait(1)
driver.get("https://plugstar.com/electricians")
time.sleep(2)

with open("C:/Users/ADMIN/PycharmProjects/plug/zip.csv") as f1:
    csvrow = csv.reader(f1, delimiter=",")
    csvrow = list(csvrow)

driver.find_element_by_xpath('//*[(@id = "address")]').clear()
time.sleep(2)
driver.find_element_by_xpath('//*[(@id = "address")]').send_keys("10050")
time.sleep(1)
driver.find_element_by_xpath('//*[(@id = "address")]').send_keys(Keys.ENTER)
time.sleep(5)

for row in csvrow:
    location = row
    driver.find_element_by_xpath('//*[(@id = "address")]').clear()
    time.sleep(2)
    driver.find_element_by_xpath('//*[(@id = "address")]').send_keys(location)
    time.sleep(1)
    driver.find_element_by_xpath('//*[(@id = "address")]').send_keys(Keys.ENTER)
    time.sleep(5)
    title = driver.find_elements_by_css_selector('div.col-sm-6>a')
    address = driver.find_elements_by_css_selector('div>address')
    website = driver.find_elements_by_css_selector('div.col-sm-6>a')

    numpage = len(title)
    i = 0
    while i < numpage:
        i += 1
    for i in range(numpage):
        title_data = title[i].text
        website_data = website[i].get_attribute('href')
        address_data = address[i].text
        plug_result = [{'Company': title_data, 'Address': address_data, 'Area': location, 'Website': website_data}]
        data = pd.DataFrame(plug_result)
        data.to_csv("PlResultC.csv", index=False, header=False, mode='a')
