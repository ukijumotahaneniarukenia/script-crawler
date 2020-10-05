#!/usr/bin/env python3
import os

import re

import json

import requests

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.common.exceptions import NoSuchElementException

DEFAULT_WAIT_TIME_SECONDS = 5

SCROLL_WAIT_TIME_SECONDS = 3

SOURCE_FILE_NAME='list.json'

OUTPUT_DIR_NAME = 'page-detail'

if not os.path.exists(OUTPUT_DIR_NAME) :
    os.makedirs(OUTPUT_DIR_NAME)

OUTPUT_FILE_PREFIX = 'page-detail-'
OUTPUT_FILE_SUFFIX = '.html'

OFS = '\t'
ORS = '\n'

#取得項目の定義
SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'
MIN_PAGE_NUMBER='MIN_PAGE_NUMBER'
MAX_PAGE_NUMBER='MAX_PAGE_NUMBER'
DOM_STRUCTURE_PATTERN='DOM_STRUCTURE_PATTERN'

DOWN_SCROLL='DOWN_SCROLL'
PAGER='PAGER'

source_file = open(SOURCE_FILE_NAME,'r')

crawler_target_list = json.load(source_file)

#ブラウザ起動オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
options.add_argument('/usr/local/src/chrome-linux/chrome')
options.add_argument('--headless')

for crawler_target in crawler_target_list:

    site_name = crawler_target[SITE_NAME]
    site_url = crawler_target[SITE_URL]
    min_page_number = crawler_target[MIN_PAGE_NUMBER]
    max_page_number = crawler_target[MAX_PAGE_NUMBER]
    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    if not os.path.exists(OUTPUT_DIR_NAME + '/' + base_name) :
        os.makedirs(OUTPUT_DIR_NAME + '/' + base_name)

    driver = webdriver.Chrome(options=options)

    for page_number in range(min_page_number,max_page_number+1):

        if crawler_target[DOM_STRUCTURE_PATTERN] == DOWN_SCROLL:

            crawler_target_url = site_url

            print(crawler_target_url)

            response = requests.get(crawler_target_url.strip())

            status_code = response.status_code

            if status_code == 200:

                if page_number == 1:
                    #初回のみWEBページ起動

                    driver.get(crawler_target_url)

                    time.sleep(DEFAULT_WAIT_TIME_SECONDS)

                # 現在のWEBページのDOM全体の高さを取得
                last_height = driver.execute_script("return document.body.scrollHeight")

                # 最下部まで下スクロール
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                time.sleep(SCROLL_WAIT_TIME_SECONDS)

                html = driver.page_source

                domain_name = re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0]

                output_file_name = OUTPUT_DIR_NAME + '/' + base_name + '/' + OUTPUT_FILE_PREFIX + (crawler_target_url + str(page_number)).strip().replace(domain_name,base_name).replace('/','-').replace('&','-').replace('?','-').replace('^','-').replace(':','-').replace('#','-').replace('=','-') + OUTPUT_FILE_SUFFIX

                print(output_file_name)

                #前回分の出力結果ファイルが存在すれば削除
                if os.path.exists(output_file_name):

                    os.remove(output_file_name)

                with open(output_file_name, 'w', encoding='utf-8') as f:
                    f.write(html)

                # 現在のWEBページのDOM全体の高さを取得
                new_height = driver.execute_script("return document.body.scrollHeight")

                if new_height == last_height:
                    # 現在のWEBページのDOM全体の高さと前回のWEBページのDOM全体の高さが同じ場合

                    break

                #現在のWEBページのDOM全体の高さを前回分に設定
                last_height = new_height

            else:

                continue

        elif crawler_target[DOM_STRUCTURE_PATTERN] == PAGER:

            crawler_target_url = site_url + str(page_number)

            print(crawler_target_url)

            response = requests.get(crawler_target_url.strip())

            status_code = response.status_code

            if status_code == 200:

                driver.get(crawler_target_url)

                time.sleep(DEFAULT_WAIT_TIME_SECONDS)

                html = driver.page_source

                domain_name = re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0]

                output_file_name = OUTPUT_DIR_NAME + '/' + base_name + '/' + OUTPUT_FILE_PREFIX + crawler_target_url.strip().replace(domain_name,base_name).replace('/','-').replace('&','-').replace('?','-').replace('^','-').replace(':','-').replace('#','-').replace('=','-') + OUTPUT_FILE_SUFFIX

                print(output_file_name)

                #前回分の出力結果ファイルが存在すれば削除
                if os.path.exists(output_file_name):

                    os.remove(output_file_name)

                with open(output_file_name, 'w', encoding='utf-8') as f:
                    f.write(html)

            else:

                continue

        else :

            continue

    driver.quit()

source_file.close()
