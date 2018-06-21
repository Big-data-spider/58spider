# -*- coding:utf-8 -*-

'''
代理地址验证
'''

import requests
from project58 import get_prox_list
from fake_useragent import UserAgent

headers = {'User-Agent': UserAgent().random}

templist = get_prox_list.join_str()

# part3 = '"http": "'
# part4 = '",'
# part1 = 'http://'
# part2 = ''

sname = "success.txt"
proxies = {'http': ''}

use_abled = []


def use_able():
    for jc in templist:
        proxies['http'] = jc

        try:
            requests.get('http://www.baidu.com', headers=headers, proxies=proxies, timeout=10)

        except:
            print("失败，放弃保存")
        else:
            with open(sname, "a") as su:
                su.write(jc + '\n')

            use_abled.append(jc)
            print("可用，已经存入本地")

    return use_abled

use_able()
