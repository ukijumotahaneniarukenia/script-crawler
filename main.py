#!/usr/bin/env python3

import json

CRAWLER_TARGET_FILE='list.json'

crawler_target_file = open(CRAWLER_TARGET_FILE, 'r')

crawler_target_list = json.load(crawler_target_file)

DATE_TIME='DATE_TIME'
MAIN_XPATH_EXPRESSION='MAIN_XPATH_EXPRESSION'
SITE_NAME='SITE_NAME'
SITE_URL='SITE_URL'
SUB_XPATH_EXPRESSION='SUB_XPATH_EXPRESSION'
TITLE_NAME='TITLE_NAME'

for crawler_target in crawler_target_list:

    print(crawler_target[SITE_NAME])
    print(crawler_target[SITE_URL])

    target_xpath_list = crawler_target[TITLE_NAME]

    for target_xpath in target_xpath_list:

        print(target_xpath[MAIN_XPATH_EXPRESSION])

        print(target_xpath[SUB_XPATH_EXPRESSION])










print(type(crawler_target_list))
