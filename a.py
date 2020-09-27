from urllib import request
from lxml import etree
import re

crawler_target_url = 'https://ukijumotahaneniarukenia.site/'

with request.urlopen(crawler_target_url) as f:

    data = f.read().decode('utf-8')

    print(type(data))

    dom_tree = etree.HTML(data)

    print(dom_tree)

    print(dom_tree.tag)
