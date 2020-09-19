#!/usr/bin/env python3

from bs4 import BeautifulSoup

import lxml

import xml.etree.ElementTree as ElementTree

from lxml import html

INPUT_PREFIX = ''
INPUT_SUFFIX = '.html'
ORS = '\n'

BASE_FILE_NAME='test'

INPUT_FILE_NAME=INPUT_PREFIX + BASE_FILE_NAME + INPUT_SUFFIX

target_file = open(INPUT_FILE_NAME,'r')

target_file_content = target_file.read()

target_dom = html.fromstring(target_file_content)

a = target_dom.xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div')

print(type(a))

print(len(a))

htmlstr = ElementTree.tostring(a[0], encoding='utf8', method='html')

print(a[0])

print(xmlstr)

target_file.close()
