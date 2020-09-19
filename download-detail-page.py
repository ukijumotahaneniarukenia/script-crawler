#!/usr/bin/env python3
import os

import re

import requests

SOURCE_FILE_NAME='base-file-name-list.txt'

INPUT_PREFIX = 'link-'
INPUT_SUFFIX = '.txt.min'
OUTPUT_PREFIX = 'page-detail-'
OUTPUT_SUFFIX = '.html'

ORS = '\n'

source_file = open(SOURCE_FILE_NAME,'r')

for site_url in source_file :

    base_name = "-".join(re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0].split(".")[::-1])

    input_file_name = INPUT_PREFIX + base_name + INPUT_SUFFIX

    if os.path.exists(input_file_name):

        target_file = open(input_file_name,'r')

        for url in target_file:

            response = requests.get(url.strip())

            status_code = response.status_code

            if status_code == 200:

                domain_name = re.findall(r'(?<=//).*?(?=/)', site_url.strip())[0]

                output_file_name = OUTPUT_PREFIX + url.strip().replace(domain_name,base_name).replace('/','-').replace('&','-').replace('?','-').replace('^','-').replace(':','-').replace('#','-') + OUTPUT_SUFFIX

                #前回分の出力結果ファイルが存在すれば削除
                if os.path.exists(output_file_name):

                    os.remove(output_file_name)

                with open(output_file_name,'a') as f:

                    f.write(response.text)
                    f.write(ORS)

            else:

                continue

        target_file.close()

    else:

        continue

source_file.close()
