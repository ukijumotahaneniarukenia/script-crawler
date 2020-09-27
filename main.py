from urllib import request
from lxml import etree
import lxml.html
import re

crawler_target_url = 'https://ukijumotahaneniarukenia.site/'

local_file_url = '/home/aine/PycharmProjects/pythonProject/test.html'

# https://docs.python.org/ja/3/library/xml.etree.elementtree.html

def NNN(html, target_element, prev_target_element_tag, prev_xpath, xpath_list):

    print("=" * 80)

    print(xpath_list)

    if etree.iselement(target_element) and not len(target_element.getchildren()) == 0:

        target_children_list = target_element.getchildren()

        target_children_cnt = len(target_children_list)

        for target_idx in range(0, target_children_cnt):

            target_element_tag = target_children_list[target_idx].tag

            print(prev_target_element_tag, target_element_tag, str(target_idx), xpath_list[-1], sep='\t')

            #ここに同一階層の同一タグを管理する





            if prev_target_element_tag == target_element_tag:
                print("bbbbbbbbb")
                xpath = prev_xpath + '/' + target_element_tag + '[' + str(target_idx + 1) + ']'
                print(xpath)
            else:
                print("aaaaaaaaa")
                xpath = prev_xpath + '/' + target_element_tag
                print(xpath)

            xpath_list.append(xpath)

            if len(target_children_list[target_idx].getchildren()) != 0:

                # ここで何を状態管理して変更するか考える
                print('='*40 + "cccccccccc" + '='*40 )
                print("target_children_list[target_idx]    :" + target_children_list[target_idx].tag)
                print("prev_target_element_tag             :" + prev_target_element_tag)
                print("prev_xpath                          :" + prev_xpath)
                print("xpath_list                          :" + ','.join(xpath_list))

                # prev_xpath = xpath
                # prev_target_element_tag = target_element_tag
                NNN(target_children_list[target_idx], target_children_list[target_idx].tag, prev_xpath + '/' + target_children_list[target_idx].tag, xpath_list)

with open(local_file_url, 'r') as f:
    data = f.read()

    doc = etree.HTML(data)

    html = lxml.html.fromstring(data)

    a = html.xpath('/html/body/ul/li[2]/ul/li')
    a = html.xpath('/html/body/ul')
    # a = html.xpath('/html/body/ul/li')
    # a = html.xpath('/html/body/ul/li[1]')
    # a = html.xpath('/html/body/ul/li[2]')
    # a = html.xpath('/html/body/ul/li[3]')

    for e in a:
        print(e.tag)
        print(e.text.strip())

    xpath_list = list()
    prev_target_element_tag = doc.tag
    prev_xpath = '/' + prev_target_element_tag
    xpath_list.append(prev_xpath)

    #元ネタは持ち回る必要がある
    NNN(html, doc, prev_target_element_tag, prev_xpath, xpath_list)
    # print(xpath_list)

#Output
# /home/aine/PycharmProjects/pythonProject/venv/bin/python /home/aine/PycharmProjects/pythonProject/main.py
# ================================================================================
# ['/html']
# html	head
# aaaaaaaaa
# /html/head
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :head
# prev_target_element_tag             :html
# prev_xpath                          :/html
# xpath_list                          :/html,/html/head
# ================================================================================
# ['/html', '/html/head']
# head	meta
# aaaaaaaaa
# /html/head/meta
# head	title
# aaaaaaaaa
# /html/head/title
# head	link
# aaaaaaaaa
# /html/head/link
# head	script
# aaaaaaaaa
# /html/head/script
# html	body
# aaaaaaaaa
# /html/body
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :body
# prev_target_element_tag             :html
# prev_xpath                          :/html
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body
# ================================================================================
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body']
# body	ul
# aaaaaaaaa
# /html/body/ul
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :ul
# prev_target_element_tag             :body
# prev_xpath                          :/html/body
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul
# ================================================================================
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul']
# ul	li
# aaaaaaaaa
# /html/body/ul/li
# ul	li
# aaaaaaaaa
# /html/body/ul/li
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li,/html/body/ul/li
# ================================================================================
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li', '/html/body/ul/li']
# li	ul
# aaaaaaaaa
# /html/body/ul/li/ul
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :ul
# prev_target_element_tag             :li
# prev_xpath                          :/html/body/ul/li
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li,/html/body/ul/li,/html/body/ul/li/ul
# ================================================================================
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li', '/html/body/ul/li', '/html/body/ul/li/ul']
# ul	li
# aaaaaaaaa
# /html/body/ul/li/ul/li
# ul	li
# aaaaaaaaa
# /html/body/ul/li/ul/li
# ul	li
# aaaaaaaaa
# /html/body/ul/li
#
# Process finished with exit code 0
