from urllib import request
from lxml import etree
from termcolor import colored
import lxml.html
import re
import sys
import os


def usage():
    filename = re.sub(".*/", "", __file__)
    usage = """

Usage:

CMD:  {filename} test.html

or

CMD:  {filename} test.html --debug

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


def NNN(html, target_element, prev_target_element_tag, prev_xpath, xpath_list, prev_xpath_list):
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
                prev_xpath_list.append(prev_xpath)

                debug_log_magenta('=' * 40 + "a" * 10 + '=' * 40)
                debug_log_magenta(
                    "current_element".ljust(30) + ':' + html.xpath(prev_xpath + '/' + target_element_tag)[0].tag)
                debug_log_magenta("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                debug_log_magenta("current_xpath".ljust(30) + ':' + current_xpath)
                debug_log_magenta("prev_xpath".ljust(30) + ':' + prev_xpath)
                debug_log_magenta("xpath_list".ljust(30) + ':' + ','.join(xpath_list))
                debug_log_magenta("prev_xpath_list".ljust(30) + ':' + ','.join(prev_xpath_list))

                NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                    current_xpath, xpath_list, prev_xpath_list)

            else:
                debug_log_red("２回目以降")

                #タグ名問わず、同一階層に存在している子ノードリストを取得
                same_hierarchy_children_list = html.xpath(prev_xpath)[0].getchildren()

                debug_log_red(prev_xpath)
                debug_log_red(prev_xpath + '/' + target_element_tag)
                debug_log_red("xpath_list".ljust(30) + ':' + ','.join(xpath_list))
                debug_log_red("prev_xpath_list".ljust(30) + ':' + ','.join(prev_xpath_list))

                for same_idx in range(0, len(same_hierarchy_children_list)):

                    debug_log_red(prev_xpath + '/' + same_hierarchy_children_list[same_idx].tag)

                    #タグ名が同じで同一階層に存在している子ノードリストを取得
                    same_tag_hierarchy_children_list = html.xpath(prev_xpath + '/' + same_hierarchy_children_list[same_idx].tag)

                    #同一のタグの出現回数を管理するために取得
                    same_tag_hierarchy_children_list_cnt = len(same_tag_hierarchy_children_list)

                    if same_tag_hierarchy_children_list_cnt == 1 :
                        #単一の場合
                        debug_log_cyan('=' * 40 + "b" * 10 + '=' * 40)
                        current_xpath = prev_xpath + '/' + same_hierarchy_children_list[same_idx].tag

                        # 前回訪問済みの場合はスキップ
                        if current_xpath in xpath_list:
                            continue

                        debug_log_cyan("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                        debug_log_cyan("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                        debug_log_cyan("current_xpath".ljust(30) + ':' + current_xpath)
                        debug_log_cyan("prev_xpath".ljust(30) + ':' + prev_xpath)
                        debug_log_cyan("xpath_list".ljust(30) + ':' + ','.join(xpath_list))
                        debug_log_cyan("prev_xpath_list".ljust(30) + ':' + ','.join(prev_xpath_list))

                        xpath_list.append(current_xpath)
                        prev_xpath_list.append(prev_xpath)

                        NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                            current_xpath, xpath_list, prev_xpath_list)

                    else :
                        #複数の場合
                        for same_tag_idx in range(0, same_tag_hierarchy_children_list_cnt) :

                            debug_log_cyan('=' * 40 + "c" * 10 + '=' * 40)

                            current_xpath = prev_xpath + '/' + same_hierarchy_children_list[same_idx].tag + '[' + str(same_tag_idx + 1) + ']'

                            # 前回訪問済みの場合はスキップ
                            if current_xpath in xpath_list:
                                continue

                            debug_log_cyan("current_element".ljust(30) + ':' + html.xpath(current_xpath)[0].tag)
                            debug_log_cyan("prev_target_element_tag".ljust(30) + ':' + prev_target_element_tag)
                            debug_log_cyan("current_xpath".ljust(30) + ':' + current_xpath)
                            debug_log_cyan("prev_xpath".ljust(30) + ':' + prev_xpath)
                            debug_log_cyan("xpath_list".ljust(30) + ':' + ','.join(xpath_list))
                            debug_log_cyan("prev_xpath_list".ljust(30) + ':' + ','.join(prev_xpath_list))

                            xpath_list.append(current_xpath)
                            prev_xpath_list.append(prev_xpath)

                            NNN(html, html.xpath(current_xpath)[0], html.xpath(prev_xpath)[0].tag,
                                current_xpath, xpath_list, prev_xpath_list)


def wrapper(file_name, *debug_mode):
    with open(file_name, 'r') as f:
        data = f.read()

        doc = etree.HTML(data)

        html = lxml.html.fromstring(data)

        xpath_list = list()
        prev_xpath_list = list()
        prev_target_element_tag = doc.tag
        prev_xpath = '/' + prev_target_element_tag
        xpath_list.append(prev_xpath)

        # 元ネタは持ち回る必要がある
        NNN(html, doc, prev_target_element_tag, prev_xpath, xpath_list, prev_xpath_list)


IS_DEBUG = 0


def main():
    global IS_DEBUG

    try:

        if (len(sys.argv[1:])) == 0:

            usage()

        else:

            if not len(sys.argv[1:]) <= 2:
                usage()

            if len(sys.argv[1:]) == 2:

                input_file_name = sys.argv[1]

                if not sys.argv[2] == '--debug':
                    usage()

                IS_DEBUG = 1

            if len(sys.argv[1:]) == 1:
                input_file_name = sys.argv[1]

            if not os.path.exists(input_file_name):
                usage()

            wrapper(input_file_name, IS_DEBUG)

    except KeyboardInterrupt:

        usage()


if __name__ == "__main__":
    main()

    sys.exit(0)
