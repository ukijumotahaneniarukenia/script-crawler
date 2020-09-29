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

def NNN(html, target_element, prev_xpath ,xpath_list):

    if len(target_element) == 0 :
        return xpath_list
    else :
        for child in target_element[0].getchildren() :

            xpath = prev_xpath + '/' + child.tag

            xpath_list.append(xpath)

            return xpath_list.extend(NNN(html, html.xpath(xpath), prev_xpath, xpath_list))


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
    NNN(html, [doc], prev_xpath ,xpath_list)
