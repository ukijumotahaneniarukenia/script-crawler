from urllib import request
from lxml import etree
import lxml.html
import re

local_file_url = '/home/aine/script-crawler/sample.html'

is_debug = 0


def debug_log(msg):
    if is_debug:
        print(msg)

# https://docs.python.org/ja/3/library/xml.etree.elementtree.html

def NNN(html, target_element, xpath_list):

    if len(target_element) == 0 :
        pass
    else :
        for child in target_element[0].getchildren() :

            #print(xpath_list[-1])

            xpath = xpath_list[-1] + '/' + child.tag

            print(xpath)

            print(html.xpath(xpath))

            #NNN(html,html.xpath(xpath)[0],target_element_list)


with open(local_file_url, 'r') as f:
    data = f.read()

    doc = etree.HTML(data)

    html = lxml.html.fromstring(data)

    #a = html.xpath('/html/head/title')

    #print(a[0].getchildren())

    xpath_list = list()
    prev_target_element_tag = doc.tag
    prev_xpath = '/' + prev_target_element_tag

    xpath_list.append(prev_xpath)

    # 元ネタは持ち回る必要がある
    NNN(html, [doc], xpath_list)
