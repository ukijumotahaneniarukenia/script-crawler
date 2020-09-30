from urllib import request
from lxml import etree
import lxml.html
import re

local_file_url = '/home/aine/script-crawler/test.html'

is_debug = 0


def debug_log(msg):
    if is_debug:
        print(msg)

# https://docs.python.org/ja/3/library/xml.etree.elementtree.html

def NNN(html, prev_xpath ,xpath_list):

    print(xpath_list)
    print(html.xpath(prev_xpath))
    if len(html.xpath(prev_xpath)) == 0:

        return xpath_list
        # pass

    elif len(html.xpath(prev_xpath)[0].getchildren()) == 0:

        return xpath_list
        # pass

    else:

        for child in html.xpath(prev_xpath)[0].getchildren():

            same_hierarchy_list = html.xpath(prev_xpath)

            if len(same_hierarchy_list) > 1 :

                for idx in range(0, len(same_hierarchy_list)):

                    current_xpath = prev_xpath + '/' + child.tag + '[' + str(idx + 1) + ']'

                    xpath_list.append(current_xpath)

                    # return xpath_list.extend(NNN(html, current_xpath, xpath_list))
                    NNN(html, current_xpath, xpath_list)

            else:

                current_xpath = prev_xpath + '/' + child.tag

                xpath_list.append(current_xpath)

                # return xpath_list.extend(NNN(html, current_xpath, xpath_list))
                NNN(html, current_xpath, xpath_list)


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
    NNN(html, prev_xpath, xpath_list)