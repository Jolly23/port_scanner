# !/usr/bin/python
# -*- coding:utf8 -*-


def get_ip_list():
    ip_list = []
    begin_remote_server_ip = raw_input("Enter the begin remote ip:")
    end_remote_server_ip = raw_input("Enter the end remote ip:")
    if not end_remote_server_ip:
        return [begin_remote_server_ip]

    else:
        args1 = begin_remote_server_ip.split('.')
        args2 = end_remote_server_ip.split('.')
        if '.'.join(args1[:2]) != '.'.join(args2[:2]):
            return []
        elif '.'.join(args1[:3]) == '.'.join(args2[:3]):
            for i in range(int(args1[3]), int(args2[3]) + 1):
                ip_l = [args1[0], args1[1], args1[2], str(i)]
                ip_list.append('.'.join(ip_l))
            return ip_list
        else:
            p_3 = [i for i in range(int(args1[2]) + 1, int(args2[2]))]
            for i in range(int(args1[3]), 256):
                ip_l = [args1[0], args1[1], args1[2], str(i)]
                ip_list.append('.'.join(ip_l))
            for each3 in p_3:
                for i in range(256):
                    ip_l = [args1[0], args1[1], str(each3), str(i)]
                    ip_list.append('.'.join(ip_l))
            for i in range(int(args2[3]) + 1):
                ip_l = [args1[0], args1[1], args2[2], str(i)]
                ip_list.append('.'.join(ip_l))
            return ip_list
