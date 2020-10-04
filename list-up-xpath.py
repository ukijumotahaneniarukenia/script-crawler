from urllib import request
from lxml import etree
import lxml.html
import re
import sys
import os

def usage():
  filename=__file__
  usage="""

Usage:

CMD:  {filename} test.html

or

DEBUG_MODE

CMD:  {filename} test.html 1

""".format(filename=filename)

  print(usage)
  sys.exit(0)

def debug_log(msg):
    if is_debug:
        print(msg)

def NNN(html, target_element, prev_target_element_tag, prev_xpath, xpath_list):

    print(xpath_list[-1])

    if etree.iselement(target_element) and not len(target_element.getchildren()) == 0:

        target_children_list = target_element.getchildren()

        target_children_cnt = len(target_children_list)

        for target_idx in range(0, target_children_cnt):

            target_element_tag = target_children_list[target_idx].tag

            if target_element.tag == 'html':
                # 初回
                debug_log("初回")

                debug_log(prev_target_element_tag + '\t' + target_element_tag + '\t' + str(target_idx) + '\t' + prev_xpath)

                current_xpath = prev_xpath + '/' + target_element_tag

                xpath_list.append(current_xpath)

                # ここで何を状態管理して変更するか考える
                debug_log('=' * 40 + "a" * 10 + '=' * 40)
                debug_log("current_element".ljust(30) + ':' + html.xpath(prev_xpath + '/' + target_element_tag)[0].tag)
                debug_log("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                debug_log("current_xpath".ljust(30) + ':' + current_xpath)
                debug_log("prev_xpath".ljust(30) + ':' + prev_xpath)
                debug_log("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                    current_xpath, xpath_list)

            else:
                # ２回目以降
                debug_log("２回目以降")

                debug_log(
                    prev_target_element_tag + '\t' + target_element_tag + '\t' + str(target_idx) + '\t' + xpath_list[
                        -1])

                # ここに同一階層の同一タグを管理する
                same_hierarchy_list = html.xpath(xpath_list[-1] + '/' + target_element_tag)

                # print('same_hierarchy_list :' + str(len(same_hierarchy_list)))

                if len(same_hierarchy_list) > 1:

                    for idx in range(0, len(same_hierarchy_list)):
                        debug_log('=' * 40 + "b" * 10 + '=' * 40)
                        current_xpath = prev_xpath + '/' + target_element_tag + '[' + str(idx + 1) + ']'

                        # ここで何を状態管理して変更するか考える
                        debug_log('=' * 40 + "c" * 10 + '=' * 40)
                        debug_log("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                        debug_log("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                        debug_log("current_xpath".ljust(30) + ':' + current_xpath)
                        debug_log("prev_xpath".ljust(30) + ':' + xpath_list[-1])
                        debug_log("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                        xpath_list.append(current_xpath)

                        NNN(html, html.xpath(current_xpath)[0], html.xpath(xpath_list[-1])[0].tag,
                            current_xpath, xpath_list)

                elif len(same_hierarchy_list) == 1:

                    debug_log('=' * 40 + "d" * 10 + '=' * 40)
                    current_xpath = xpath_list[-1] + '/' + target_element_tag

                    debug_log("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                    debug_log("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                    debug_log("current_xpath".ljust(30) + ':' + current_xpath)
                    debug_log("prev_xpath".ljust(30) + ':' + xpath_list[-1])
                    debug_log("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                    xpath_list.append(current_xpath)

                    NNN(html, html.xpath(current_xpath)[0], html.xpath(xpath_list[-1])[0].tag,
                        current_xpath, xpath_list)
                else:
                    debug_log('=' * 40 + "e" * 10 + '=' * 40)
                    debug_log("xpath_list".ljust(30) + ':' + ','.join(xpath_list))
                    current_xpath = prev_xpath + '/' + target_element_tag
                    xpath_list.append(current_xpath)
                    debug_log(current_xpath)

def wrapper(file_name, *debug_mode):

    with open(file_name, 'r') as f:

        data = f.read()

        doc = etree.HTML(data)

        html = lxml.html.fromstring(data)

        xpath_list = list()
        prev_target_element_tag = doc.tag
        prev_xpath = '/' + prev_target_element_tag
        xpath_list.append(prev_xpath)

        # 元ネタは持ち回る必要がある
        NNN(html, doc, prev_target_element_tag, prev_xpath, xpath_list)

is_debug = 0

def main():

  global is_debug

  try:

    if (len(sys.argv[1:]))==0:

        usage()

    else:

        if not len(sys.argv[1:]) <= 2 :

            usage()

        if len(sys.argv[1:]) == 2 :

            input_file_name = sys.argv[1]

            if not int(sys.argv[2]) == 1:

                usage()

            is_debug = int(sys.argv[2])

        if len(sys.argv[1:]) == 1 :

            input_file_name = sys.argv[1]

        if not os.path.exists(input_file_name):

            usage()

        wrapper(input_file_name, is_debug)

  except KeyboardInterrupt:

    usage()

if __name__=="__main__":

  main()

  sys.exit(0)
