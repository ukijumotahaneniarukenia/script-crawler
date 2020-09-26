#!/usr/bin/env python3
import json

import datetime

import sys

import os

import re

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DEFAULT_WAIT_TIME_SECONDS=5

#ブラウザ起動オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
options.add_argument('/usr/local/src/chrome-linux/chrome')

#new_height:16576
#last_height:12556
#new_height:20194
#last_height:16576
#new_height:24646
#last_height:20194
#new_height:30586
#last_height:24646
#new_height:36616
#last_height:30586

driver = webdriver.Chrome(options=options)

if not len(sys.argv[1:]) == 1:
    sys.exit(0)

driver.get(sys.argv[1])


time.sleep(DEFAULT_WAIT_TIME_SECONDS)

SCROLL_PAUSE_TIME = 3

# 現在のWEBページのDOM全体の高さを取得
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
       # 最下部まで下スクロール
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

       time.sleep(SCROLL_PAUSE_TIME)

       # 現在のWEBページのDOM全体の高さを取得
       new_height = driver.execute_script("return document.body.scrollHeight")

       print("new_height:" + str(new_height))
       print("last_height:" + str(last_height))

       if new_height == last_height:
           # 現在のWEBページのDOM全体の高さと前回のWEBページのDOM全体の高さが同じ場合

           break

       #現在のWEBページのDOM全体の高さを前回分に設定
       last_height = new_height
