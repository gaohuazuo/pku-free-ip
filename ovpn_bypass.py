#!/usr/bin/env python3

import os

from fetch import fetch


def main():
    ip_list = fetch()
    print('# PKU free ip')
    for ip, _, netmask in ip_list:
        print('route', ip, netmask, 'net_gateway')


if __name__ == '__main__':
    main()

