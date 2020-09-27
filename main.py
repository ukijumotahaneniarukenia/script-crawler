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

            print("+++++++++++++++" + target_element.tag)

            if target_element.tag == 'html':
                # 初回
                print("初回")

                print(prev_target_element_tag, target_element_tag, str(target_idx), prev_xpath, sep='\t')

                current_xpath = prev_xpath + '/' + target_element_tag
                xpath_list.append(current_xpath)

                # ここで何を状態管理して変更するか考える
                print('=' * 40 + "a" * 10 + '=' * 40)
                print("current_element".ljust(30) + ':' + html.xpath(prev_xpath + '/' + target_element_tag)[0].tag)
                print("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                print("current_xpath".ljust(30) + ':' + current_xpath)
                print("prev_xpath".ljust(30) + ':' + prev_xpath)
                print("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                    current_xpath, xpath_list)

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

                        # ここで何を状態管理して変更するか考える
                        print('=' * 40 + "c" * 10 + '=' * 40)
                        print("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                        print("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                        print("current_xpath".ljust(30) + ':' + current_xpath)
                        print("prev_xpath".ljust(30) + ':' + xpath_list[-1])
                        print("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                        xpath_list.append(current_xpath)

                        NNN(html, html.xpath(current_xpath)[0], html.xpath(xpath_list[-1])[0].tag,
                            current_xpath, xpath_list)

                elif len(same_hierarchy_list) == 1:

                    print('=' * 40 + "d" * 10 + '=' * 40)
                    current_xpath = xpath_list[-1] + '/' + target_element_tag

                    print("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                    print("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                    print("current_xpath".ljust(30) + ':' + current_xpath)
                    print("prev_xpath".ljust(30) + ':' + xpath_list[-1])
                    print("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                    xpath_list.append(current_xpath)

                    NNN(html, html.xpath(current_xpath)[0], html.xpath(xpath_list[-1])[0].tag,
                        current_xpath, xpath_list)
                else:

                    print('=' * 40 + "e" * 10 + '=' * 40)
                    print("xpath_list".ljust(30) + ':' + ','.join(xpath_list))
                    # print(same_hierarchy_list[0].tag)
                    xpath = prev_xpath + '/' + target_element_tag
                    xpath_list.append(xpath)
                    print(xpath)


with open(local_file_url, 'r') as f:
    data = f.read()

    doc = etree.HTML(data)

    html = lxml.html.fromstring(data)

    # a = html.xpath("/html")
    # a = html.xpath("/html/head")
    # a = html.xpath("/html/head/meta")
    # a = html.xpath("/html/head/title")
    # a = html.xpath("/html/head/link")
    # a = html.xpath("/html/head/script")
    # a = html.xpath("/html/body")
    # a = html.xpath("/html/body/ul")
    # a = html.xpath("/html/body/ul/li[1]")
    # a = html.xpath("/html/body/ul/li[2]")
    # a = html.xpath("/html/body/ul/li[2]/ul")
    # a = html.xpath("/html/body/ul/li[2]/ul/li[1]")
    # a = html.xpath("/html/body/ul/li[2]/ul/li[2]")
    # a = html.xpath("/html/body/ul/li[2]/ul/li")
    # a = html.xpath("/html/body/ul/li[3]")
    # a = html.xpath("/html/body/ul/li")

    print(len(a))

    for e in a:
        print(e.tag)
        print(e.text.strip())

    xpath_list = list()
    prev_target_element_tag = doc.tag
    prev_xpath = '/' + prev_target_element_tag
    xpath_list.append(prev_xpath)

    # 元ネタは持ち回る必要がある
    # NNN(html, doc, prev_target_element_tag, prev_xpath, xpath_list)
    # print(xpath_list)