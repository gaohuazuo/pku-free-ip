#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re


def fetch():
    url = 'https://its.pku.edu.cn/oper/liebiao.jsp'
    r = requests.get(url)
    m = re.search('<pre>网络号 *主机掩码 *网络掩码\r\n'
                  'network-number *host-bits *netmask\r\n'
                  '-* *-* *-*\r\n'
                  '(.*)</pre>',
                  r.text, re.DOTALL)
    return [l.split() for l in m.group(1).splitlines()]


if __name__ == '__main__':
    for l in fetch():
        print(*l)

