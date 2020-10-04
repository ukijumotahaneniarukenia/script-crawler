#!/usr/bin/env python3

from bs4 import BeautifulSoup

import re

import lxml

import os

import glob

SOURCE_FILE_NAME='base-file-name-list.txt'

INPUT_PREFIX = 'page-detail-'
INPUT_SUFFIX = '.html'

OUTPUT_DIR_NAME = 'link'
OUTPUT_PREFIX = OUTPUT_DIR_NAME + '/' + 'link-'
OUTPUT_SUFFIX = '.txt'
ORS = '\n'

source_file = open(SOURCE_FILE_NAME,'r')

for site_url in source_file :

    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    input_file_pattern = INPUT_PREFIX + '*' + base_name + '*' + INPUT_SUFFIX

    output_file_name = OUTPUT_PREFIX + base_name + OUTPUT_SUFFIX

    input_file_name_list = glob.glob(input_file_pattern)

    if len(input_file_name_list) == 0 :

        continue

    for input_file_name in input_file_name_list :

        if not os.path.exists(input_file_name):

            continue

        print(input_file_name)

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

            #https://www.it-swarm-ja.tech/ja/python/%E6%AD%A3%E8%A6%8F%E8%A1%A8%E7%8F%BE%E5%86%85%E3%81%A7%E5%A4%89%E6%95%B0%E3%82%92%E4%BD%BF%E7%94%A8%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%E3%81%AF%EF%BC%9F/940649158/
            duplicate_pattern = r"" + re.escape(site_url.strip()) + r""

            if sub_url is None :

                continue

            duplicate_result = re.findall(duplicate_pattern, sub_url)

            if len(duplicate_result) == 0 :

                url_list.append(site_url.strip().replace('#','') + sub_url)

            else :

                url_list.append(sub_url)

        target_url_list = sorted(set(url_list))

        with open(output_file_name, mode='a') as f:

            for target_url in target_url_list:

                f.write(re.sub('/+$','',target_url).strip())
                f.write(ORS)

        target_file.close()

source_file.close()
