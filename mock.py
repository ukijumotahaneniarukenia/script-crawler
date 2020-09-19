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
crawler_target_url_list = ['https://jp.reuters.com/article/kono-idJPKBN2690PY?taid=5f64b07f1266d20001bb2bee&utm_campaign=trueAnthem:+Trending+Content&utm_medium=trueAnthem&utm_source=twitter']

for crawler_target_url in crawler_target_url_list:

    print(crawler_target_url)

    driver.get(crawler_target_url)

    time.sleep(DEFAULT_WAIT_TIME_SECONDS)

    date_time_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div/time[1]').text

    print(date_time_text)

    #title_text = driver.find_element_by_xpath('/html/body/div[6]/article/div[1]/h1').text
    title_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/h1').text

    print(title_text)

driver.quit()