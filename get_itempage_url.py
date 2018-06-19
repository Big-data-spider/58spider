# -*- coding:utf-8 -*-

'''
获取详情页链接
'''

import time
import numpy
from lxml import etree
import requests
from fake_useragent import UserAgent


def get_url(url):
    '''
    获取详情页链接
    :param url:
    :return:
    '''
    try:
        detail = requests.get(url=url, headers={'User-agent': UserAgent().random}).text
        time.sleep(numpy.random.randint(1, 4))
        dom = etree.HTML(detail)
        if '/chuzu/' in url:
            x_path = '//div[@class="des"]/h2/a/@href'
        elif '/ershoufang/' in url:
            x_path = '//h2[@class="title"]/a/@href'
        elif '/pinpaigongyu/' in url:
            x_path = '//ul[@class="list"]/li/a/@href'

        if dom.xpath(x_path) != None:
            urls = dom.xpath(x_path)
        print urls
        real_list = []
        for url in urls:
            if ('/zd_p/' or '/hezu/' or '/chuzu/' or '/ershoufang/' or '/pinpaigongyu/' or '/legoclick.58.com/') in url:
                real_list.append(url)
            elif '//legoclick.58.com/' in url:
                url_e = 'http:' + url
                real_list.append(url_e)

            else:
                print("%s 站点规则未编写"%url)

            # time.sleep(numpy.random.randint(2, 6))

    except:
        print('没有获取到数据！')

    finally:
        print real_list
        return real_list


###############################################
# '''
# test
# '''
#
# url = 'http://cd.58.com/pinpaigongyu/'
#
# get_url(url)
