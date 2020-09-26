#!/usr/bin/env python3
import json

import datetime

import sys

import os

import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

#ブラウザ起動オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
options.add_argument('/usr/local/src/chrome-linux/chrome')

driver = webdriver.Chrome(options=options)

if not len(sys.argv[1:]) == 1:
    sys.exit(0)

driver.get(sys.argv[1])



time.sleep(5)


extract_sub_tag_list = driver.find_elements_by_xpath('/html/body/div[13]/div[1]/div[3]/div[1]/div[12]/div[2]/table[1]/tbody/tr[6]/td/p')

for sub_tag in extract_sub_tag_list :

    extract_text = sub_tag.find_element_by_xpath('.').text

    print(extract_text)
