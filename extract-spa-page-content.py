#!/usr/bin/env python3
import json

import datetime

import sys

import os

import time

import re

import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DEFAULT_WAIT_TIME_SECONDS=5

SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'

LINK_PREFFIX='link-'
LINK_SUFFIX='.txt'

SOURCE_FILE_NAME='list-spa.json'

source_file = open(SOURCE_FILE_NAME,'r')

crawler_target_list = json.load(source_file)

#ブラウザ起動オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
options.add_argument('/usr/local/src/chrome-linux/chrome')

for crawler_target in crawler_target_list:

    site_name = crawler_target[SITE_NAME]
    site_url = crawler_target[SITE_URL]
    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    link_file_name = LINK_PREFFIX + base_name + LINK_SUFFIX

    if os.path.exists(link_file_name):

        if re.search(base_name,link_file_name):

            link_file_name_list = open(link_file_name,'r')

            for link_file_name in list(link_file_name_list)[0:4]:

                crawler_target_url = link_file_name.strip()

                response = requests.get(crawler_target_url)

                if response.status_code == 200 :

                    driver = webdriver.Chrome(options=options)
                    driver.get(crawler_target_url)

                    time.sleep(DEFAULT_WAIT_TIME_SECONDS)

                #date_time_text = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div/div/time[1]').text

                #print(date_time_text)

                #title_text = driver.find_element_by_xpath('/html/body/div[6]/article/div[1]/h1').text
                #title_text = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div/h1').text

                #print(title_text)

                    driver.quit()
                else :

                    continue
