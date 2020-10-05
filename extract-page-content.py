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

from selenium.common.exceptions import NoSuchElementException

DEFAULT_WAIT_TIME_SECONDS=5

SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'

INPUT_DIR_NAME = 'link'
INPUT_FILE_PREFIX = 'link-'
INPUT_FILE_SUFFIX = '.txt.target'

CHECK_DIR_NAME = 'no-need-access-url'
CHECK_FILE_PREFIX = 'no-need-access-url-'
CHECK_FILE_SUFFIX='.json'

OUTPUT_DIR_NAME = 'page-content'
OUTPUT_FILE_PREFIX = 'page-content-'
OUTPUT_FILE_SUFFIX = '.tsv'

EXTRACT_COLUMN_LIST_DEFINE_DIR_NAME='extract-column-list'
EXTRACT_COLUMN_LIST_COMMON_FILE_NAME = EXTRACT_COLUMN_LIST_DEFINE_DIR_NAME + '/' + 'extract-column-list-common.json'
EXTRACT_COLUMN_LIST_SITE_PREFIX = EXTRACT_COLUMN_LIST_DEFINE_DIR_NAME + '/' + 'extract-column-list-site-'
EXTRACT_COLUMN_LIST_SITE_SUFFIX = '.json'

OFS = '\t'
ORS = '\n'

#取得項目の定義
MAIN_XPATH_EXPRESSION='MAIN_XPATH_EXPRESSION'
SUB_XPATH_EXPRESSION='SUB_XPATH_EXPRESSION'
EXTRACT_COLUMN_LIST='EXTRACT_COLUMN_LIST'
SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'

DEFAULT_NONE_VALUE = 'ないよーん'
EXTRACT_IS_COMPLETED = '1'
EXTRACT_IS_NOT_COMPLETED = '0'

#取得項目リスト
common_column_list_file = open(EXTRACT_COLUMN_LIST_COMMON_FILE_NAME,'r')

common_column_list = json.load(common_column_list_file)

OUTPUT_HEADER_LIST=set()
for common_column_name in common_column_list[EXTRACT_COLUMN_LIST] :

    OUTPUT_HEADER_LIST.add(common_column_name)

SOURCE_FILE_NAME='list.json'

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
    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    if not os.path.exists(OUTPUT_DIR_NAME + '/' + base_name) :
        os.makedirs(OUTPUT_DIR_NAME + '/' + base_name)

    check_file_name = CHECK_DIR_NAME + '/' + base_name + '/' + CHECK_FILE_PREFIX + base_name + CHECK_FILE_SUFFIX

    output_file_name = OUTPUT_DIR_NAME + '/' + base_name + '/' + OUTPUT_FILE_PREFIX + base_name + OUTPUT_FILE_SUFFIX

    #前回分の出力結果ファイルが存在すれば削除
    #if os.path.exists(output_file_name):

    #    os.remove(output_file_name)

    link_file_name = INPUT_DIR_NAME + '/' + base_name + '/' + INPUT_FILE_PREFIX + base_name + INPUT_FILE_SUFFIX

    if not os.path.exists(link_file_name):

        continue

    if not re.search(base_name,link_file_name) :

        continue

    link_file_name_list = open(link_file_name,'r')

    cnt = 0

    for link_file_name_entry in link_file_name_list:

        if site_url == link_file_name_entry.strip() + "/" :

            continue

        crawler_target_url = link_file_name_entry.strip()

        if re.match(r'^(https?)',crawler_target_url) is None :

            continue

        if os.path.exists(check_file_name):
        #前回分のチェックファイルが存在すれば実施

            check_file = open(check_file_name,'r')

            check_list = json.load(check_file)

            if crawler_target_url in check_list :

                continue

        response = requests.get(crawler_target_url)

        if response.status_code == 200 :

            extract_list = []

            cnt = cnt + 1

            EXTRACT_URL_NAME = link_file_name_entry.strip()
            EXTRACT_SITE_NAME = crawler_target[SITE_NAME]
            EXTRACT_SITE_URL = crawler_target[SITE_URL]
            EXTRACT_BASE_NAME = base_name

            extract_list.append(EXTRACT_URL_NAME)
            extract_list.append(EXTRACT_SITE_NAME)
            extract_list.append(EXTRACT_SITE_URL)
            extract_list.append(EXTRACT_BASE_NAME)

            site_column_list_file = open(EXTRACT_COLUMN_LIST_SITE_PREFIX + base_name + EXTRACT_COLUMN_LIST_SITE_SUFFIX,'r')

            site_column_list = json.load(site_column_list_file)

            driver = webdriver.Chrome(options=options)
            driver.get(crawler_target_url)

            time.sleep(DEFAULT_WAIT_TIME_SECONDS)

            for site_column_name in site_column_list[EXTRACT_COLUMN_LIST] :

                OUTPUT_HEADER_LIST.add(site_column_name)
                OUTPUT_HEADER_LIST.add(site_column_name + '_IS_EXTRACT_COMPLETED_FLG' )

                target_xpath_list = crawler_target[EXTRACT_COLUMN_LIST][site_column_name]

                extract_sub_list = []

                pre_check_pattern_key_list  = list(map(lambda entry : list(entry.keys())[0],target_xpath_list))

                for target_xpath in target_xpath_list:

                    if not any(key in target_xpath for key in  {MAIN_XPATH_EXPRESSION,SUB_XPATH_EXPRESSION}) :

                        continue

                    main_xpath = target_xpath[MAIN_XPATH_EXPRESSION]
                    sub_xpath = target_xpath[SUB_XPATH_EXPRESSION]

                    if not len(main_xpath) == 0 and len(sub_xpath) == 0 :

                        try:

                            extract_text = driver.find_element_by_xpath(main_xpath).text

                            for pre_check_pattern_key in pre_check_pattern_key_list:

                                match_result = re.findall(r'.*_PATTERN', pre_check_pattern_key)

                                if not len(match_result) == 0 :

                                    check_pattern_entry  = list(filter(lambda entry : not len(re.findall(r'.*_PATTERN', list(entry.keys())[0])) == 0,target_xpath_list))[0]

                                    for check_pattern_key,check_pattern_value_list in check_pattern_entry.items():

                                        for check_pattern_value in check_pattern_value_list:

                                            if len(check_pattern_value) == 0:

                                                continue

                                            check_pattern_regexp = r"" + check_pattern_value + r""

                                            valid_pattern_list = re.findall(check_pattern_regexp, extract_text)

                                            if not len(valid_pattern_list) == 0:

                                                extract_sub_list.append(extract_text)
                                                extract_sub_list.append(EXTRACT_IS_COMPLETED)

                                            else :
                                                #unmatch

                                                pass

                                else :
                                    #unmatch

                                    pass

                        except NoSuchElementException:

                            pass

                    elif not len(main_xpath) == 0 and not len(sub_xpath) == 0 :

                        try:

                            extract_sub_tag_list = driver.find_elements_by_xpath(main_xpath)

                            extract_sub_text_list = []

                            for sub_tag in extract_sub_tag_list :

                                extract_text = sub_tag.find_element_by_xpath(sub_xpath).text

                                for pre_check_pattern_key in pre_check_pattern_key_list:

                                    match_result = re.findall(r'.*_PATTERN', pre_check_pattern_key)

                                    if not len(match_result) == 0 :

                                        check_pattern_entry  = list(filter(lambda entry : not len(re.findall(r'.*_PATTERN', list(entry.keys())[0])) == 0,target_xpath_list))[0]

                                        for check_pattern_key,check_pattern_value_list in check_pattern_entry.items():

                                            for check_pattern_value in check_pattern_value_list:

                                                if len(check_pattern_value) == 0:

                                                    continue

                                                check_pattern_regexp = r"" + check_pattern_value + r""

                                                valid_pattern_list = re.findall(check_pattern_regexp, extract_text)

                                                if not len(valid_pattern_list) == 0:

                                                    extract_sub_text_list.append(extract_text.replace('\n','\\n'))

                                                else :
                                                    #unmatch

                                                    pass

                                    else :
                                        #unmatch

                                        pass

                            if not len(extract_sub_text_list) == 0:

                                extract_sub_list.append('\\n'.join(extract_sub_text_list))
                                extract_sub_list.append(EXTRACT_IS_COMPLETED)

                            else :

                                pass

                        except NoSuchElementException:

                            pass

                    else :

                        pass

                if not len(extract_sub_list) == 0 :

                    extract_list.append(extract_sub_list[0])
                    extract_list.append(extract_sub_list[1])

                else :

                    extract_list.append(DEFAULT_NONE_VALUE)
                    extract_list.append(EXTRACT_IS_NOT_COMPLETED)

            driver.quit()

            site_column_list_file.close()

        else :

            continue

        if cnt == 1:
            #ファイルの新規作成
            with open(output_file_name,'a') as f:

                f.write(re.sub('[0-9]+_','','\t'.join(sorted(OUTPUT_HEADER_LIST))))
                f.write(ORS)
                f.write('\t'.join(extract_list))
                f.write(ORS)
        else :

            with open(output_file_name,'a') as f:
                f.write('\t'.join(extract_list))
                f.write(ORS)

    link_file_name_list.close()
