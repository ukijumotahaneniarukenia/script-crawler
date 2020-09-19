#!/usr/bin/env python3
import sys

import glob

import re

import os

import datetime

import time

import json

from lxml import html

SOURCE_FILE_NAME='list-non-spa.json'

COMMON_COLUMN_LIST_FILE_NAME = ''

LINK_PREFFIX='link-'
LINK_SUFFIX='.txt'

COLUMN_LIST_PREFFIX='extract-site-column-list-'
COLUMN_LIST_SUFFIX='.json'

INPUT_PREFIX = 'page-detail-'
INPUT_SUFFIX = '.html'
OUTPUT_PREFIX = 'page-content-'
OUTPUT_SUFFIX = '.tsv'

OFS = '\t'
ORS = '\n'

#取得項目の定義
DATE_TIME='DATE_TIME'
MAIN_XPATH_EXPRESSION='MAIN_XPATH_EXPRESSION'
SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'
SUB_XPATH_EXPRESSION='SUB_XPATH_EXPRESSION'
TITLE_NAME='TITLE_NAME'

EXTRACT_COLUMN_LIST='EXTRACT_COLUMN_LIST'

#取得項目共通リスト

#取得項目リスト
#json定義ファイルからいいかんじにしたいな
EXTRACT_LIST=[
         'EXTRACT_URL_NAME'
        ,'EXTRACT_PAGE_NAME'
        ,'EXTRACT_SITE_NAME'
        ,'EXTRACT_SITE_URL'
        ,'EXTRACT_BASE_NAME'
        ,'EXTRACT_TITLE_NAME'
        ,'EXTRACT_IS_COMPLETED_TITLE_NAME_FLG'
        ,'EXTRACT_DATE_TIME'
        ,'EXTRACT_IS_COMPLETED_DATE_TIME_FLG'
        ]

DTM = datetime.datetime.today().strftime('%Y-%m-%dT%H-%M-%S')
DST = os.getcwd() #実行ディレクトリ

source_file = open(SOURCE_FILE_NAME,'r')

crawler_target_list = json.load(source_file)

for crawler_target in crawler_target_list:

    site_name = crawler_target[SITE_NAME]
    site_url = crawler_target[SITE_URL]
    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    output_file_name = OUTPUT_PREFIX + base_name + OUTPUT_SUFFIX

    #前回分の出力結果ファイルが存在すれば削除
    if os.path.exists(output_file_name):

        os.remove(output_file_name)

    #ファイルの新規作成
    with open(output_file_name,'a') as f:

        f.write("\t".join(EXTRACT_LIST))
        f.write(ORS)

    link_file_name = LINK_PREFFIX + base_name + LINK_SUFFIX

    if os.path.exists(link_file_name):

        if re.search(base_name,link_file_name):

            link_file_name_list = open(link_file_name,'r')

            for link_file_name in link_file_name_list:

               domain_name = re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0]

               input_file_name = INPUT_PREFIX + link_file_name.strip().replace(domain_name,base_name).replace('/','-').replace('&','-').replace('?','-').replace('^','-').replace(':','-').replace('#','-').replace('=','-') + INPUT_SUFFIX

               if os.path.exists(input_file_name):

                   extract_list = []

                   if re.search(base_name,input_file_name) and ( not site_url ==link_file_name.strip() + "/" ):
                       #トップエントリ以外を処理対象とする

                       #取得項目値の格納用の変数
                       EXTRACT_TITLE_NAME='-'
                       EXTRACT_DATE_TIME='-'
                       EXTRACT_IS_COMPLETED_TITLE_NAME_FLG='0'
                       EXTRACT_IS_COMPLETED_DATE_TIME_FLG='0'

                       EXTRACT_URL_NAME = link_file_name.strip()
                       extract_list.append(EXTRACT_URL_NAME)

                       EXTRACT_PAGE_NAME = input_file_name
                       extract_list.append(EXTRACT_PAGE_NAME)

                       EXTRACT_SITE_NAME = crawler_target[SITE_NAME]
                       EXTRACT_SITE_URL = crawler_target[SITE_URL]
                       EXTRACT_BASE_NAME = base_name

                       extract_list.append(EXTRACT_SITE_NAME)
                       extract_list.append(EXTRACT_SITE_URL)
                       extract_list.append(EXTRACT_BASE_NAME)

                       target_file = open(input_file_name,'r')

                       target_file_content = target_file.read()

                       target_dom = html.fromstring(target_file_content)



                       #site_column_list_file = open(COLUMN_LIST_PREFFIX + base_name + COLUMN_LIST_SUFFIX,'r')

                       #site_column_list = json.load(site_column_list_file)


                       target_xpath_list = crawler_target[EXTRACT_COLUMN_LIST][TITLE_NAME]

                       for target_xpath in target_xpath_list:

                           main_xpath = target_xpath[MAIN_XPATH_EXPRESSION]
                           sub_xpath = target_xpath[SUB_XPATH_EXPRESSION]


                           if not len(main_xpath) == 0 :

                               result_list = target_dom.xpath(main_xpath)

                               if not len(result_list) == 0:

                                   extract_title_name = result_list[0].text

                                   if extract_title_name is not None :

                                       EXTRACT_TITLE_NAME = extract_title_name
                                       EXTRACT_IS_COMPLETED_TITLE_NAME_FLG = '1'

                                       extract_list.append(EXTRACT_TITLE_NAME)
                                       extract_list.append(EXTRACT_IS_COMPLETED_TITLE_NAME_FLG)

                                   else :

                                       extract_list.append(EXTRACT_TITLE_NAME)
                                       extract_list.append(EXTRACT_IS_COMPLETED_TITLE_NAME_FLG)

                           if not len(sub_xpath) == 0 :
                               #複数件への対応

                               pass

                       target_xpath_list = crawler_target[EXTRACT_COLUMN_LIST][DATE_TIME]

                       for target_xpath in target_xpath_list:

                           main_xpath = target_xpath[MAIN_XPATH_EXPRESSION]
                           sub_xpath = target_xpath[SUB_XPATH_EXPRESSION]

                           if not len(main_xpath) == 0 :

                               result_list = target_dom.xpath(main_xpath)

                               if not len(result_list) == 0:

                                   extract_date_time = result_list[0].text

                                   if extract_date_time is not None :

                                       EXTRACT_DATE_TIME = extract_date_time
                                       EXTRACT_IS_COMPLETED_DATE_TIME_FLG = '1'

                                       extract_list.append(EXTRACT_DATE_TIME)
                                       extract_list.append(EXTRACT_IS_COMPLETED_DATE_TIME_FLG)

                                   else :

                                       extract_list.append(EXTRACT_DATE_TIME)
                                       extract_list.append(EXTRACT_IS_COMPLETED_DATE_TIME_FLG)

                           if not len(sub_xpath) == 0 :
                               #複数件への対応

                               pass

                       target_file.close()

                   else:

                       continue

                   with open(output_file_name,'a') as f:

                       f.write("\t".join(extract_list))
                       f.write(ORS)
