#!/usr/bin/env python3

from bs4 import BeautifulSoup

import re

import lxml

import os

SOURCE_FILE_NAME='base-file-name-list.txt'

INPUT_PREFIX = 'page-'
INPUT_SUFFIX = '.html'

OUTPUT_PREFIX = 'link-'
OUTPUT_SUFFIX = '.txt'
ORS = '\n'

source_file = open(SOURCE_FILE_NAME,'r')

for site_url in source_file :

    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    input_file_name = INPUT_PREFIX + base_name + INPUT_SUFFIX

    output_file_name = OUTPUT_PREFIX + base_name + OUTPUT_SUFFIX

    target_file = open(input_file_name,'r')

    target_file_content = target_file.read()

    soup = BeautifulSoup(target_file_content, 'lxml')

    anchor_tag_list = soup.find_all('a')

    #前回分の出力結果ファイルが存在すれば削除
    if os.path.exists(output_file_name):
        os.remove(output_file_name)

    url_list = []
    for anchor_tag in anchor_tag_list:

        sub_url = anchor_tag.get('href')

        url_list.append(site_url.strip() + sub_url)

    target_url_list = sorted(set(url_list))

    with open(output_file_name, mode='a') as f:

        for target_url in target_url_list:

            f.write(target_url)
            f.write(ORS)

    target_file.close()

source_file.close()