#!/usr/bin/env python3
import os

import re

import json

import requests

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

DEFAULT_WAIT_TIME_SECONDS=5

SOURCE_FILE_NAME='list.json'

OUTPUT_PREFIX = 'page-detail-'
OUTPUT_SUFFIX = '.html'

OFS = '\t'
ORS = '\n'

#取得項目の定義
SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'
MIN_PAGE_NUMBER='MIN_PAGE_NUMBER'
MAX_PAGE_NUMBER='MAX_PAGE_NUMBER'

source_file = open(SOURCE_FILE_NAME,'r')

crawler_target_list = json.load(source_file)

#ブラウザ起動オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
options.add_argument('/usr/local/src/chrome-linux/chrome')

for crawler_target in crawler_target_list:

    site_name = crawler_target[SITE_NAME]
    site_url = crawler_target[SITE_URL]
    min_page_number = crawler_target[MIN_PAGE_NUMBER]
    max_page_number = crawler_target[MAX_PAGE_NUMBER]
    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    output_file_name = OUTPUT_PREFIX + base_name + OUTPUT_SUFFIX

    #前回分の出力結果ファイルが存在すれば削除
    if os.path.exists(output_file_name):

        os.remove(output_file_name)

    for page_number in range(min_page_number,max_page_number+1):

        crawler_target_url = site_url + str(page_number)

        print(crawler_target_url)

        response = requests.get(crawler_target_url.strip())

        status_code = response.status_code

        if status_code == 200:

            driver = webdriver.Chrome(options=options)

            driver.get(crawler_target_url)

            time.sleep(DEFAULT_WAIT_TIME_SECONDS)

            html = driver.page_source

            domain_name = re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0]

            output_file_name = OUTPUT_PREFIX + crawler_target_url.strip().replace(domain_name,base_name).replace('/','-').replace('&','-').replace('?','-').replace('^','-').replace(':','-').replace('#','-').replace('=','-') + OUTPUT_SUFFIX

            #前回分の出力結果ファイルが存在すれば削除
            if os.path.exists(output_file_name):

                os.remove(output_file_name)

            with open(output_file_name, 'w', encoding='utf-8') as f:
                f.write(html)

            driver.quit()

        else:

            continue

source_file.close()
