#!/usr/bin/env python3
import json

import datetime

import sys

import os

import time

import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DEFAULT_WAIT_TIME_SECONDS=10

#ブラウザ起動オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
options.add_argument('/usr/local/src/chrome-linux/chrome')

driver = webdriver.Chrome(options=options)

#crawler_target_url_list = ['https://edition.cnn.com/2020/09/18/politics/ruth-bader-ginsburg-dead/index.html']
crawler_target_url_list = ['https://www.asahi.com//articles/ASN9373V6N93UBQU00B.html?iref=comtop_list_api_f02']

for crawler_target_url in crawler_target_url_list:

    print(crawler_target_url)

    driver.get(crawler_target_url)

    time.sleep(DEFAULT_WAIT_TIME_SECONDS)

    #date_time_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div/time[1]').text

    #print(date_time_text)

    #title_text = driver.find_element_by_xpath('/html/body/div[6]/article/div[1]/h1').text
    title_text = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div/h1').text

    print(title_text)

driver.quit()
