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

def wrapper(file_name, *debug_mode):

    with open(file_name, 'r') as f:

        data = f.read()

        doc = etree.HTML(data)

        html = lxml.html.fromstring(data)

        result = html.xpath('/html/body/article/div/div/div[1]/div[1]/div/div')

        print(result)

        target_child_list = result[0].getchildren()

        print(target_child_list)

        #print(result)

        #result = html.xpath('/html/body/ul/li')

        #print(result)

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
