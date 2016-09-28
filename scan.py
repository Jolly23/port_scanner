# !/usr/bin/python
# -*- coding:utf8 -*-

import socket
from multiprocessing.dummy import Pool as ThreadPool


def scan_port(info):
    this_ip_ports = []
    try:
        s = socket.socket(2, 1)
        res = s.connect_ex((info.get('remote_server_ip'), info.get('port')))
        if res == 0:
            this_ip_ports.append(info.get('port'))
        s.close()
    except:
        pass

    db_port = [3306, 1521, 5432, 1433]
    for i in db_port:
        if i in this_ip_ports:
            print u'**********Found: {}-{}**********'.format(info.get('remote_server_ip'), i)


def scan(remote_ip):
    socket.setdefaulttimeout(0.5)
    remote_info = [{
        'remote_server_ip': socket.gethostbyname(remote_ip),
        'port': i,
    } for i in range(65535)]

    pool = ThreadPool(processes=1024)
    pool.map(scan_port, remote_info)
    pool.close()
    pool.join()
