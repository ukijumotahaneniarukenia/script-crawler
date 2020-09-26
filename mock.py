#!/usr/bin/env python3
import json

import datetime

import sys

import os

import re

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#ブラウザ起動オプションの設定
options = webdriver.ChromeOptions()
options.add_argument('/usr/local/src/chromedriver_linux64/chromedriver')
options.add_argument('/usr/local/src/chrome-linux/chrome')

driver = webdriver.Chrome(options=options)

if not len(sys.argv[1:]) == 1:
    sys.exit(0)

driver.get(sys.argv[1])
