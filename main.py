#!/usr/bin/env python3
import json

import datetime

import sys

import os

import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#クロール対象ファイルの定義
CRAWLER_TARGET_FILE='list.json'

#取得項目の定義
DATE_TIME='DATE_TIME'
MAIN_XPATH_EXPRESSION='MAIN_XPATH_EXPRESSION'
SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'
SUB_XPATH_EXPRESSION='SUB_XPATH_EXPRESSION'
TITLE_NAME='TITLE_NAME'

ORS = '\n'
OFS = '-'
DTM = datetime.datetime.today().strftime('%Y-%m-%dT%H-%M-%S')
DST = os.getcwd() #実行ディレクトリ

DEFAULT_WAIT_TIME_SECONDS=10

def usage():
    filename = re.sub('.*/', '', __file__)
    usage_message = '''
Usage:

  PRE: pip3 install --user selenium

       which chrome
       /usr/local/src/chrome-linux/chrome

       which chromedriver
       /usr/local/src/chromedriver_linux64/chromedriver

  CMD: {filename} --debug wait_time_seconds:2

    or

  CMD: {filename} --debug

    or

  CMD: {filename} --non-debug

'''.format(filename=filename)

    print(usage_message)

    sys.exit(0)

def crawl(execute_args):

    #ブラウザ起動オプションの設定
    options = webdriver.ChromeOptions()
    options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
    options.add_argument('/usr/local/src/chrome-linux/chrome')

    for arg in execute_args:

        if arg == '--non-debug':
            #ブラウザ立ち上げない

            options.add_argument('--headless')

            continue

        if arg == '--debug':
            #ブラウザ立ち上げる

            continue

        WAIT_TIME_SECONDS = re.findall(r'(?<=wait_time_seconds:)[0-9]+',arg)

        if len(WAIT_TIME_SECONDS) != 1:

            usage()

        DEFAULT_WAIT_TIME_SECONDS = int(WAIT_TIME_SECONDS[0])

    driver = webdriver.Chrome(options=options)

    crawler_target_file = open(CRAWLER_TARGET_FILE, 'r')

    crawler_target_list = json.load(crawler_target_file)

    for crawler_target in crawler_target_list:

        print(crawler_target[SITE_NAME])
        print(crawler_target[SITE_URL])

        target_xpath_list = crawler_target[TITLE_NAME]

        for target_xpath in target_xpath_list:

            print(target_xpath[MAIN_XPATH_EXPRESSION])

            print(target_xpath[SUB_XPATH_EXPRESSION])

    driver.quit()

    crawler_target_file.close()

def main():

    try:
        if (len(sys.argv[1:])) == 0:
            # パイプ経由引数の場合

            args_via_pipe = list(map(lambda x: x.strip().split(), sys.stdin.readlines()))

            execute_args = sum(args_via_pipe,[])

            print(execute_args)

            crawl(execute_args)

        else:
            # コマンドライン経由引数の場合

            execute_args = sys.argv[1:]

            print(execute_args)

            crawl(execute_args)

    except KeyboardInterrupt:

        usage()

if __name__ == '__main__':
    main()
