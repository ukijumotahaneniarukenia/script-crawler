from urllib import request
from lxml import etree
import lxml.html
import re

crawler_target_url = 'https://ukijumotahaneniarukenia.site/'

local_file_url = '/home/aine/PycharmProjects/pythonProject/test.html'


# https://docs.python.org/ja/3/library/xml.etree.elementtree.html

def NNN(html, target_element, prev_target_element_tag, prev_xpath, xpath_list):

    print("＠" * 80)

    print(xpath_list)

    if etree.iselement(target_element) and not len(target_element.getchildren()) == 0:

        target_children_list = target_element.getchildren()

        target_children_cnt = len(target_children_list)

        for target_idx in range(0, target_children_cnt):

            target_element_tag = target_children_list[target_idx].tag

            if target_element.tag == 'html':
                # 初回
                print("初回")

                print(prev_target_element_tag, target_element_tag, str(target_idx), prev_xpath, sep='\t')

                current_xpath = prev_xpath + '/' + target_element_tag
                xpath_list.append(current_xpath)
                print(current_xpath)

                # ここで何を状態管理して変更するか考える
                print('=' * 40 + "a" * 10 + '=' * 40)
                print("current_element".ljust(30) + ':' + html.xpath(prev_xpath + '/' + target_element_tag)[0].tag)
                print("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                print("current_xpath".ljust(30) + ':' + current_xpath)
                print("prev_xpath".ljust(30) + ':' + prev_xpath)
                print("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                    prev_xpath, xpath_list)

            else:
                # ２回目以降
                print("２回目以降")

                print(prev_target_element_tag, target_element_tag, str(target_idx), xpath_list[-1], sep='\t')

                # ここに同一階層の同一タグを管理する
                same_hierarchy_list = html.xpath(xpath_list[-1] + '/' + target_element_tag)

                print('same_hierarchy_list :' + str(len(same_hierarchy_list)))

                if len(same_hierarchy_list) > 1:

                    for idx in range(0, len(same_hierarchy_list)):
                        print('=' * 40 + "b" * 10 + '=' * 40)
                        current_xpath = prev_xpath + '/' + target_element_tag + '[' + str(idx + 1) + ']'
                        xpath_list.append(current_xpath)

                        # ここで何を状態管理して変更するか考える
                        print('=' * 40 + "c" * 10 + '=' * 40)
                        print("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                        print("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                        print("current_xpath".ljust(30) + ':' + current_xpath)
                        print("prev_xpath".ljust(30) + ':' + xpath_list[-1])
                        print("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                        NNN(html, html.xpath(current_xpath)[0], html.xpath(xpath_list[-1])[0].tag,
                            xpath_list[-1], xpath_list)

                elif len(same_hierarchy_list) == 1:

                    print('=' * 40 + "d" * 10 + '=' * 40)
                    # print(same_hierarchy_list[0].tag)
                    current_xpath = xpath_list[-1] + '/' + target_element_tag
                    xpath_list.append(current_xpath)
                    print(current_xpath)

                else:

                    print('=' * 40 + "e" * 10 + '=' * 40)
                    # print(same_hierarchy_list[0].tag)
                    xpath = prev_xpath + '/' + target_element_tag
                    xpath_list.append(xpath)
                    print(xpath)
                    # NNN(html, html.xpath(xpath)[0], html.xpath(xpath)[0].tag,
                    #     xpath, xpath_list)


with open(local_file_url, 'r') as f:
    data = f.read()

    doc = etree.HTML(data)

    html = lxml.html.fromstring(data)

    # a = html.xpath('/html/body/ul/li[2]/ul/li')
    # a = html.xpath('/html/body/ul')
    # a = html.xpath('/html/body/ul/li')
    # a = html.xpath('/html/body/ul/li[1]')
    # a = html.xpath('/html/body/ul/li[2]/ul/li')
    # a = html.xpath('/html/body/ul/li[2]/ul')
    # a = html.xpath('/html/body/ul/li[2]')
    # a = html.xpath('/html/body/ul/li[3]')

    # for e in a:
    #     print(e.tag)
    #     print(e.text.strip())

    xpath_list = list()
    prev_target_element_tag = doc.tag
    prev_xpath = '/' + prev_target_element_tag
    xpath_list.append(prev_xpath)

    # 元ネタは持ち回る必要がある
    NNN(html, doc, prev_target_element_tag, prev_xpath, xpath_list)
    # print(xpath_list)

# Output
# /home/aine/PycharmProjects/pythonProject/venv/bin/python /home/aine/PycharmProjects/pythonProject/main.py
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html']
# html	head	0	/html
# [<Element head at 0x7f2708cc02c0>]
# same_hierarchy_list :1
# ========================================aaaaaaaaaa========================================
# /html/head
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :head
# prev_target_element_tag             :html
# prev_xpath                          :/html
# xpath_list                          :/html,/html/head
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head']
# head	meta	0	/html/head
# [<Element meta at 0x7f2708cc0310>]
# same_hierarchy_list :1
# ========================================aaaaaaaaaa========================================
# /html/head/meta
# head	title	1	/html/head/meta
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/head/title
# head	link	2	/html/head/title
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/head/link
# head	script	3	/html/head/link
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/head/script
# html	body	1	/html/head/script
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/body
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :body
# prev_target_element_tag             :html
# prev_xpath                          :/html
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body']
# body	ul	0	/html/body
# [<Element ul at 0x7f2708cc0360>]
# same_hierarchy_list :1
# ========================================aaaaaaaaaa========================================
# /html/body/ul
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :ul
# prev_target_element_tag             :body
# prev_xpath                          :/html/body
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul']
# ul	li	0	/html/body/ul
# [<Element li at 0x7f2708cc0400>, <Element li at 0x7f2708cc0450>, <Element li at 0x7f2708cc04a0>]
# same_hierarchy_list :3
# ========================================bbbbbbbbbb========================================
# /html/body/ul/li[1]
# ========================================dddddddddd========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul/li[1]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1]
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]']
# ========================================bbbbbbbbbb========================================
# /html/body/ul/li[2]
# ========================================dddddddddd========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul/li[2]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2]
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]']
# li	ul	0	/html/body/ul/li[2]
# [<Element ul at 0x7f2708cc04f0>]
# same_hierarchy_list :1
# ========================================aaaaaaaaaa========================================
# /html/body/ul/li[2]/ul
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :ul
# prev_target_element_tag             :li
# prev_xpath                          :/html/body/ul/li[2]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul']
# ul	li	0	/html/body/ul/li[2]/ul
# [<Element li at 0x7f2708cc0590>, <Element li at 0x7f2708cc05e0>]
# same_hierarchy_list :2
# ========================================bbbbbbbbbb========================================
# /html/body/ul/li[2]/ul/li[1]
# ========================================dddddddddd========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul/li[2]/ul/li[1]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul,/html/body/ul/li[2]/ul/li[1]
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul', '/html/body/ul/li[2]/ul/li[1]']
# ========================================bbbbbbbbbb========================================
# /html/body/ul/li[2]/ul/li[2]
# ========================================dddddddddd========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul/li[2]/ul/li[2]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul,/html/body/ul/li[2]/ul/li[1],/html/body/ul/li[2]/ul/li[2]
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul', '/html/body/ul/li[2]/ul/li[1]', '/html/body/ul/li[2]/ul/li[2]']
# ul	li	1	/html/body/ul/li[2]/ul/li[2]
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/body/ul/li[2]/ul/li
# ========================================bbbbbbbbbb========================================
# /html/body/ul/li[3]
# ========================================dddddddddd========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul/li[3]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul,/html/body/ul/li[2]/ul/li[1],/html/body/ul/li[2]/ul/li[2],/html/body/ul/li[2]/ul/li,/html/body/ul/li[3]
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul', '/html/body/ul/li[2]/ul/li[1]', '/html/body/ul/li[2]/ul/li[2]', '/html/body/ul/li[2]/ul/li', '/html/body/ul/li[3]']
# ul	li	1	/html/body/ul/li[3]
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/body/ul/li
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul,/html/body/ul/li[2]/ul/li[1],/html/body/ul/li[2]/ul/li[2],/html/body/ul/li[2]/ul/li,/html/body/ul/li[3],/html/body/ul/li
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul', '/html/body/ul/li[2]/ul/li[1]', '/html/body/ul/li[2]/ul/li[2]', '/html/body/ul/li[2]/ul/li', '/html/body/ul/li[3]', '/html/body/ul/li']
# li	ul	0	/html/body/ul/li
# [<Element ul at 0x7f2708cc05e0>]
# same_hierarchy_list :1
# ========================================aaaaaaaaaa========================================
# /html/body/ul/li/ul
# ========================================cccccccccc========================================
# target_children_list[target_idx]    :ul
# prev_target_element_tag             :li
# prev_xpath                          :/html/body/ul/li
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul,/html/body/ul/li[2]/ul/li[1],/html/body/ul/li[2]/ul/li[2],/html/body/ul/li[2]/ul/li,/html/body/ul/li[3],/html/body/ul/li,/html/body/ul/li/ul
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul', '/html/body/ul/li[2]/ul/li[1]', '/html/body/ul/li[2]/ul/li[2]', '/html/body/ul/li[2]/ul/li', '/html/body/ul/li[3]', '/html/body/ul/li', '/html/body/ul/li/ul']
# ul	li	0	/html/body/ul/li/ul
# [<Element li at 0x7f2708cc07c0>, <Element li at 0x7f2708cc0810>]
# same_hierarchy_list :2
# ========================================bbbbbbbbbb========================================
# /html/body/ul/li/ul/li[1]
# ========================================dddddddddd========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul/li/ul/li[1]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul,/html/body/ul/li[2]/ul/li[1],/html/body/ul/li[2]/ul/li[2],/html/body/ul/li[2]/ul/li,/html/body/ul/li[3],/html/body/ul/li,/html/body/ul/li/ul,/html/body/ul/li/ul/li[1]
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul', '/html/body/ul/li[2]/ul/li[1]', '/html/body/ul/li[2]/ul/li[2]', '/html/body/ul/li[2]/ul/li', '/html/body/ul/li[3]', '/html/body/ul/li', '/html/body/ul/li/ul', '/html/body/ul/li/ul/li[1]']
# ========================================bbbbbbbbbb========================================
# /html/body/ul/li/ul/li[2]
# ========================================dddddddddd========================================
# target_children_list[target_idx]    :li
# prev_target_element_tag             :ul
# prev_xpath                          :/html/body/ul/li/ul/li[2]
# xpath_list                          :/html,/html/head,/html/head/meta,/html/head/title,/html/head/link,/html/head/script,/html/body,/html/body/ul,/html/body/ul/li[1],/html/body/ul/li[2],/html/body/ul/li[2]/ul,/html/body/ul/li[2]/ul/li[1],/html/body/ul/li[2]/ul/li[2],/html/body/ul/li[2]/ul/li,/html/body/ul/li[3],/html/body/ul/li,/html/body/ul/li/ul,/html/body/ul/li/ul/li[1],/html/body/ul/li/ul/li[2]
# ＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# ['/html', '/html/head', '/html/head/meta', '/html/head/title', '/html/head/link', '/html/head/script', '/html/body', '/html/body/ul', '/html/body/ul/li[1]', '/html/body/ul/li[2]', '/html/body/ul/li[2]/ul', '/html/body/ul/li[2]/ul/li[1]', '/html/body/ul/li[2]/ul/li[2]', '/html/body/ul/li[2]/ul/li', '/html/body/ul/li[3]', '/html/body/ul/li', '/html/body/ul/li/ul', '/html/body/ul/li/ul/li[1]', '/html/body/ul/li/ul/li[2]']
# ul	li	1	/html/body/ul/li/ul/li[2]
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/body/ul/li/ul/li
# ul	li	2	/html/body/ul/li/ul/li
# []
# same_hierarchy_list :0
# ========================================aaaaaaaaaa========================================
# /html/body/ul/li
#
# Process finished with exit code 0
