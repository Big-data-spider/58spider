# -*- coding:utf-8 -*-

'''
批量获取所有页面地址
需要配合反爬
'''

import IOutils
import get_pages
import numpy
import time
import re

index_list = IOutils.readfile()

# 列表字符处理
L = index_list.replace('[', '')
L = L.replace(']', '')
L = L.replace('\'', '')
list_u = L.split(",")

list_u = list(set(list_u))

print list_u


for url in list_u:
    '''
    再次处理url列表
    '''
    key = str(url)
    regx = r'http\:\/\/[a-z]+\.58\.com\/(chuzu|ershoufang|pinpaigongyu)\/'
    pattern1 = re.compile(regx)
    matcher1 = re.search(pattern1, key)
    out_url = matcher1.group()
    list_u.remove(url)
    list_u.append(out_url)

print list_u


def page_list_print(index_list):
    '''
    获取所有页面地址
    :param index_list:
    :return:
    '''
    for url in index_list:
        page_list = [url]
        result_list = get_pages.chuzu_page3(url, page_list)
        # result_list = get_pages.chuzu_pages(url, page_list)
        if len(result_list) <= 1:
            print('页数获取失败了')
        else:
            get_pages.file_rt(result_list)
        time.sleep(numpy.random.randint(2, 6))


def step1():
    '''
    检测是否被反
    :return:
    '''
    try:
        # 成功并保存
        page_list_print(list_u)
    except:
        print('被反扒了')


step1()
