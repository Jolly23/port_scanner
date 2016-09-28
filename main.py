# !/usr/bin/python
# -*- coding:utf8 -*-

from create_ip_list import get_ip_list
from scan import scan


if __name__ == "__main__":
    ip_list = get_ip_list()
    counter = 0
    for i in ip_list:
        counter += 1
        print u'{} / {}'.format(counter, len(ip_list))
        scan(i)
