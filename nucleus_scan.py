# !/usr/bin/python
# -*- coding:utf8 -*-

import socket
from multiprocessing.dummy import Pool as ThreadPool


def scan(info):
    conn = socket.socket(2, 1)
    res = conn.connect_ex((info.get('server_ip'), info.get('port')))
    if res == 0:
        print u'Found: {}:{}\n'.format(info.get('server_ip'), info.get('port'))
    conn.close()


def distribute_ip(remote_ip_list, db_scan=True):
    socket.setdefaulttimeout(0.5)
    db_port_list = [1433, 1521, 3306, 5432, 6379]
    remote_info = [
        {
            'server_ip': socket.gethostbyname(each_remote_ip),
            'port': db_port,
        } for db_port in (db_port_list if db_scan else range(65536))
        for each_remote_ip in remote_ip_list
        ]
    print u'--- Scan Begin ---'
    print u'共需扫描{0}个IP，{1}个端口\n'.format(len(remote_ip_list), len(remote_info))
    pool = ThreadPool(processes=1024)
    pool.map(scan, remote_info)
    pool.close()
    pool.join()
