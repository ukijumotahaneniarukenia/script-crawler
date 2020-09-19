#!/usr/bin/env python3

from lxml import html

INPUT_PREFIX = 'page-'
INPUT_SUFFIX = '.html'
ORS = '\n'

BASE_FILE_NAME='com-reuters-jp'

INPUT_FILE_NAME=INPUT_PREFIX + BASE_FILE_NAME + INPUT_SUFFIX

target_file = open(INPUT_FILE_NAME,'r')

target_file_content = target_file.read()

target_dom = html.fromstring(target_file_content)

a = target_dom.xpath('/html/body/div[4]/section[2]/div/div[1]/div[1]/section/div/div[1]/section/div/div[1]/div[1]/section/section/div[2]/h2/a')

print(type(a))

print(len(a))

print(a[0].text)

target_file.close()
