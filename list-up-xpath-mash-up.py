from urllib import request
from lxml import etree
from termcolor import colored
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

def debug_log_blue(msg):
    if IS_DEBUG:
        print(colored(msg, 'blue'))

def debug_log_red(msg):
    if IS_DEBUG:
        print(colored(msg, 'red'))

def debug_log_magenta(msg):
    if IS_DEBUG:
        print(colored(msg, 'magenta'))

def debug_log_cyan(msg):
    if IS_DEBUG:
        print(colored(msg, 'cyan'))

def debug_log_green(msg):
    if IS_DEBUG:
        print(colored(msg, 'green'))

def debug_log_yellow(msg):
    if IS_DEBUG:
        print(colored(msg, 'yellow'))

def NNN(html, target_element, prev_target_element_tag, prev_xpath, xpath_list):

    print(xpath_list[-1])

    if etree.iselement(target_element) and not len(target_element.getchildren()) == 0:

        target_children_list = target_element.getchildren()

        target_children_cnt = len(target_children_list)

        for target_idx in range(0, target_children_cnt):

            target_element_tag = target_children_list[target_idx].tag

            if target_element.tag == 'html':
                debug_log_red("初回")

                current_xpath = prev_xpath + '/' + target_element_tag

                xpath_list.append(current_xpath)

                debug_log_magenta('=' * 40 + "a" * 10 + '=' * 40)
                debug_log_magenta("current_element".ljust(30) + ':' + html.xpath(prev_xpath + '/' + target_element_tag)[0].tag)
                debug_log_magenta("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                debug_log_magenta("current_xpath".ljust(30) + ':' + current_xpath)
                debug_log_magenta("prev_xpath".ljust(30) + ':' + prev_xpath)
                debug_log_magenta("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                    current_xpath, xpath_list)

            else:
                debug_log_red("２回目以降")

                #same_hierarchy_list = html.xpath(xpath_list[-1] + '/' + target_element_tag) #親の位置から見るためには直前を見てはだめ
                same_hierarchy_list = html.xpath(prev_xpath + '/' + target_element_tag)

                debug_log_red(prev_xpath + '/' + target_element_tag)
                debug_log_red(xpath_list[-1] + '/' + target_element_tag)
                debug_log_red("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                if len(same_hierarchy_list) > 1:

                    for idx in range(0, len(same_hierarchy_list)):
                        debug_log_cyan('=' * 40 + "b" * 10 + '=' * 40)
                        current_xpath = prev_xpath + '/' + target_element_tag + '[' + str(idx + 1) + ']'

                        debug_log_cyan("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                        debug_log_cyan("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                        debug_log_cyan("current_xpath".ljust(30) + ':' + current_xpath)
                        debug_log_cyan("prev_xpath".ljust(30) + ':' + prev_xpath)
                        debug_log_cyan("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                        xpath_list.append(current_xpath)

                        NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                            current_xpath, xpath_list)

                elif len(same_hierarchy_list) == 1:

                    debug_log_green('=' * 40 + "c" * 10 + '=' * 40)
                    current_xpath = prev_xpath + '/' + target_element_tag

                    debug_log_green("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                    debug_log_green("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                    debug_log_green("current_xpath".ljust(30) + ':' + current_xpath)
                    debug_log_green("prev_xpath".ljust(30) + ':' + prev_xpath)
                    debug_log_green("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                    xpath_list.append(current_xpath)

                    NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                        current_xpath, xpath_list)

                else:
                    debug_log_blue('=' * 40 + "d" * 10 + '=' * 40)
                    current_xpath = prev_xpath + '/' + target_element_tag

                    debug_log_blue("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                    debug_log_blue("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                    debug_log_blue("current_xpath".ljust(30) + ':' + current_xpath)
                    debug_log_blue("prev_xpath".ljust(30) + ':' + prev_xpath)
                    debug_log_blue("xpath_list".ljust(30) + ':' + ','.join(xpath_list))

                    xpath_list.append(current_xpath)

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

IS_DEBUG = 0

def main():

  global IS_DEBUG

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

            IS_DEBUG = int(sys.argv[2])

        if len(sys.argv[1:]) == 1 :

            input_file_name = sys.argv[1]

        if not os.path.exists(input_file_name):

            usage()

        wrapper(input_file_name, IS_DEBUG)

  except KeyboardInterrupt:

    usage()

if __name__=="__main__":

  main()

  sys.exit(0)
