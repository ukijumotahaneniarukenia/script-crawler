#!/usr/bin/env python3

from bs4 import BeautifulSoup

import lxml

import os

INPUT_PREFIX = 'page-'
INPUT_SUFFIX = '.html'

OUTPUT_PREFIX = 'link-'
OUTPUT_SUFFIX = '.txt'
ORS = '\n'

MAIN_URL='https://jp.reuters.com'

BASE_FILE_NAME='com-reuters-jp'

INPUT_FILE_NAME=INPUT_PREFIX + BASE_FILE_NAME + INPUT_SUFFIX

OUTPUT_FILE_NAME=OUTPUT_PREFIX + BASE_FILE_NAME + OUTPUT_SUFFIX

target_file = open(INPUT_FILE_NAME,'r')

target_file_content = target_file.read()

soup = BeautifulSoup(target_file_content, 'lxml')

anchor_tag_list = soup.find_all('a')

#前回分の出力結果ファイルが存在すれば削除
if os.path.exists(OUTPUT_FILE_NAME):
    os.remove(OUTPUT_FILE_NAME)

url_list = []
for anchor_tag in anchor_tag_list:

    sub_url = anchor_tag.get('href')

    url_list.append(MAIN_URL + sub_url)

with open(OUTPUT_FILE_NAME, mode='a') as f:

    for url in url_list:

        f.write(url)
        f.write(ORS)

target_file.close()
