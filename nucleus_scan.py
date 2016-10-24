# !/usr/bin/python
# -*- coding:utf8 -*-

import socket
import Queue
from multiprocessing.dummy import Pool as ThreadPool

res_queue = Queue.Queue()


def scan(info):
    conn = socket.socket(2, 1)
    res = conn.connect_ex((info.get('remote_server_ip'), info.get('port')))
    if res == 0:
        res_queue.put(u'Found: {}-{}'.format(info.get('remote_server_ip'), info.get('port')))
    conn.close()


def distribute_ip(remote_ip_list, db_scan=True):
    socket.setdefaulttimeout(0.5)
    db_port_list = [1521]
    remote_info = [
        {
            'remote_server_ip': socket.gethostbyname(each_remote_ip),
            'port': db_port,
        } for db_port in (db_port_list if db_scan else range(65536))
        for each_remote_ip in remote_ip_list
    ]
    pool = ThreadPool(processes=1024)
    pool.map(scan, remote_info)
    pool.close()
    pool.join()
    while not res_queue.empty():
        print res_queue.get()
