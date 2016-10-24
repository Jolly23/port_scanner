# !/usr/bin/python
# -*- coding:utf8 -*-

from create_ip_list import get_ip_list
from nucleus_scan import distribute_ip


if __name__ == "__main__":
    distribute_ip(get_ip_list(), db_scan=True)
