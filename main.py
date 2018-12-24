#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import requests

URL = "https://www.baidu.com"


def requestURL():
   url = requests.get(URL)
   return url

"""
    main func
"""
def main():
    print("Hello World!")
    print("status = {0}".format(requestURL().status_code))


"""
    init
"""
if __name__ == "__main__":
    main()
