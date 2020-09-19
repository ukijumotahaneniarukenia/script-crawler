#!/usr/bin/env python3

import json

CRAWLER_TARGET_FILE='list.json'

crawler_target_file = open(CRAWLER_TARGET_FILE, 'r')

crawler_target_list = json.load(crawler_target_file)

print(type(crawler_target_list))
