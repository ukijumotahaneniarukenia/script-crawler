#!/usr/bin/env python3

import requests

INPUT_PREFIX = 'link-'
INPUT_SUFFIX = '.txt.min'
ORS = '\n'

MAIN_URL = 'https://jp.reuters.com'

BASE_FILE_NAME = 'com-reuters-jp'

INPUT_FILE_NAME = INPUT_PREFIX + BASE_FILE_NAME + INPUT_SUFFIX

with open(INPUT_FILE_NAME,'r') as f:

    for url in f:

        response = requests.get(url.strip())

        status_code = response.status_code

        if status_code == 200:

            print(url.strip())
            print(status_code)
            print(response.text)

        else:

            continue

