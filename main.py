from urllib import request
from lxml import etree
import re

crawler_target_url = 'https://ukijumotahaneniarukenia.site/'

local_file_url = '/home/aine/PycharmProjects/pythonProject/test.html'


# https://docs.python.org/ja/3/library/xml.etree.elementtree.html

def NNN(target_element, prev_target_element_tag, prev_xpath, xpath_list):
    print("=" * 80)

    print(xpath_list)

    if etree.iselement(target_element) and not len(target_element.getchildren()) == 0:

        target_children_list = target_element.getchildren()

        target_children_cnt = len(target_children_list)

        for target_idx in range(0, target_children_cnt):

            target_element_tag = target_children_list[target_idx].tag

            print(prev_target_element_tag, target_element_tag, sep='\t')

            if prev_target_element_tag == target_element_tag:

                xpath = prev_xpath + '/' + target_element_tag + '[' + str(target_idx + 1) + ']'
                print(xpath)
            else:
                xpath = prev_xpath + '/' + target_element_tag
                print(xpath)

            xpath_list.append(xpath)

            if len(target_children_list[target_idx].getchildren()) != 0:
                prev_xpath = xpath
                prev_target_element_tag = target_element_tag
                NNN(target_children_list[target_idx], prev_target_element_tag, prev_xpath, xpath_list)

with open(local_file_url, 'r') as f:
    data = f.read()

    doc = etree.HTML(data)

    xpath_list = list()
    prev_target_element_tag = doc.tag
    prev_xpath = '/' + prev_target_element_tag
    xpath_list.append(prev_target_element_tag)
    NNN(doc, prev_target_element_tag, prev_xpath, xpath_list)
    # print(xpath_list)
