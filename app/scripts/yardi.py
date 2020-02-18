# Author: Nik Burmeister
import time
import os
import bs4
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="app/scripts/chromedriver.exe", chrome_options=chrome_options)
yardi_login_url = "https://www.yardiasp13.com/47310settlement/pages/LoginAdvanced.aspx"
yardi_financial_analytics_url = "https://www.yardiasp13.com/47310settlement/pages/GlrepFinancial.aspx"
username = "nburmeister"
password = "Winter19!"


def yardi_login():
    try:
        driver.get(yardi_login_url)
        username_field = driver.find_element_by_id("Username")
        username_field.clear()
        username_field.send_keys(username)
        driver.find_element_by_id("Password_Text").click()
        driver.find_element_by_id("Password").send_keys(password)
        driver.find_element_by_id("cmdLogin1").click()
        time.sleep(1)
        return 1
    except:
        return 0


def T12_Month_Statement(property, book, account_tree, period_start, period_end):
    # TODO: CHECK IF LOGGED IN
    #driver.switch_to(yardi_financial_analytics_url)
    driver.get(yardi_financial_analytics_url)
    driver.find_element_by_id("PropertyID_LookupCode").clear()
    driver.find_element_by_id("PropertyID_LookupCode").send_keys(property)
    driver.find_element_by_id("BookID_LookupCode").clear()
    driver.find_element_by_id("BookID_LookupCode").send_keys(book)
    driver.find_element_by_id("TreeID_LookupCode").clear()
    driver.find_element_by_id("TreeID_LookupCode").send_keys(account_tree)
    driver.find_element_by_id("FromMMYY_TextBox").clear()
    driver.find_element_by_id("FromMMYY_TextBox").send_keys(period_start)
    driver.find_element_by_id("ToMMYY_TextBox").clear()
    driver.find_element_by_id("ToMMYY_TextBox").send_keys(period_end)
    driver.find_element_by_id("Display_Button").click()

    soup = BeautifulSoup(driver.page_source)
    financials = soup.find(id="TableWriter1")

    headers = []
    data = []

    for index, row in enumerate(financials.findAll('tr')):
        if index == 0:
            t_headers = financials.findAll('tr')[0].find_all('th')
            for h in t_headers:
                headers.append(h.text.strip())
        else:
            line_item = row.findAll('td')
            line_data = []
            for i in line_item:
                if isinstance(i, bs4.element.Tag):
                    try:
                        line_data.append(i.text.strip())
                    except AttributeError:
                        print("")
            data.append(line_data)

    df = pd.DataFrame(data=data)
    return df