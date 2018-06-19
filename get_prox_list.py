# -*- coding:utf-8 -*-

'''
获取快代理免费代理列表前六页的代理

'''

import requests
from fake_useragent import UserAgent
from lxml import etree
import time
import numpy

url = [
    'https://www.kuaidaili.com/free/',
    'https://www.kuaidaili.com/free/inha/2/',
    'https://www.kuaidaili.com/free/inha/3/',
    'https://www.kuaidaili.com/free/inha/4/',
    'https://www.kuaidaili.com/free/inha/5/',
    'https://www.kuaidaili.com/free/inha/6/',
    'https://www.kuaidaili.com/free/inha/7/',
    'https://www.kuaidaili.com/free/inha/8/',
    'https://www.kuaidaili.com/free/inha/9/',
    'https://www.kuaidaili.com/free/inha/10/',
    'https://www.kuaidaili.com/free/inha/11/',
    'https://www.kuaidaili.com/free/inha/12/',
    'https://www.kuaidaili.com/free/inha/13/',
    'https://www.kuaidaili.com/free/inha/14/',
    'https://www.kuaidaili.com/free/inha/15/',
    'https://www.kuaidaili.com/free/inha/16/',
    'https://www.kuaidaili.com/free/inha/17/',
    'https://www.kuaidaili.com/free/inha/17/',
    'https://www.kuaidaili.com/free/inha/18/',
    'https://www.kuaidaili.com/free/inha/19/',
    'https://www.kuaidaili.com/free/inha/20/',
    'https://www.kuaidaili.com/free/inha/21/',
    'https://www.kuaidaili.com/free/inha/22/',
    'https://www.kuaidaili.com/free/inha/23/',
    'https://www.kuaidaili.com/free/inha/24/',
    'https://www.kuaidaili.com/free/inha/25/',
    'https://www.kuaidaili.com/free/inha/26/',
    'https://www.kuaidaili.com/free/inha/27/',
    'https://www.kuaidaili.com/free/inha/28/',
    'https://www.kuaidaili.com/free/inha/29/'
]

UA = UserAgent()
print UA.random

headers = {'User-Agent': UA.random}
# headers = {
#     'Host': 'www.kuaidaili.com',
#     'Connection': 'keep-alive',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'zh-CN,zh;q=0.9',
#     'Cookie': 'channelid=0; sid=1528848962659120; _ga=GA1.2.1306208225.1528848964; _gid=GA1.2.976491081.1528848964; Qs_lvt_161068=1528848963; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1528848964; Qs_pv_161068=3260104841590182000%2C1769917532507995000%2C2880488943219697000%2C350571991646144830%2C737281015617768800; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1528865411'
# }

pro_dict = {}


def proxy_dict(tpye, host_ip):
    pro_dict[tpye] = host_ip
    return pro_dict


def get_proxy(url):
    content = requests.get(url, headers=headers).text
    dom = etree.HTML(content)
    # print dom
    host_ips = dom.xpath(r'//td[@data-title="IP"]/text()')
    host_ports = dom.xpath(r'//td[@data-title="PORT"]/text()')

    return host_ips, host_ports


def join_str():
    '''
    生成最终代理列表供程序使用
    :return:
    '''
    try:
        lists = []
        for rl in url:
            lists.append(get_proxy(rl)[0])
            time.sleep(numpy.random.randint(3, 6))

        ports = []
        for rl in url:
            ports.append(get_proxy(rl)[1])
            time.sleep(numpy.random.randint(3, 6))

        # print lists
        p_list = sum(ports, [])
        i_list = sum(lists, [])

        ip_list = []
        for i in range(len(i_list)):
            ip = i_list[i] + ":" + p_list[i]
            ip_list.append(ip)

        print ip_list
    except:
        print('ip代理站已经启动反爬机制，换个ip吧')
    finally:
        return ip_list




'''
代码测试
'''

# join_str()

# def main():
#     list = sum(join_str(), [])
#     time.sleep(3)
#     print list
#     #
#     # print(dict)
#     #
#     # return dict
#
#
# main()
