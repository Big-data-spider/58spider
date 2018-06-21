# -*- encoding:utf-8 -*-

'''
获取全国各地目标站点的二级分类页面地址
'''

import re
import link2nd_tool
import time
import numpy
import IOutils
import requests
from fake_useragent import UserAgent
import get_prox_list
import random

headers = UserAgent()
# print headers.random

UA = {
    'Host': 'hz.58.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'id58=Ch8BCFsV5Kgb/jPrBvvWAg==; 58tj_uuid=1b15b1d4-e3dc-4156-a8b1-6eec10531911; als=0; _ga=GA1.2.526787566.1528161449; commontopbar_myfeet_tooltip=end; xxzl_deviceid=TscvHcNrf5U7LgxDBgutxMSiiGpL9EEy%2FXIkrR0iGUp14ydsedcj1jYMhW3s6tf5; wmda_uuid=623700eb814b7e6db30f42724bb8f893; wmda_new_uuid=1; st=201865165725; __utmz=253535702.1528189977.5.5.utmcsr=g.58.com|utmccn=(referral)|utmcmd=referral|utmcct=/city; wmda_visited_projects=%3B2385390625025%3B1409632296065; gr_user_id=ed7175d2-d129-499e-a32a-a129d3c5ea64; quanguo=20186814027; __utma=253535702.526787566.1528161449.1528418407.1528437710.7; qd=201868144525; Hm_lvt_e15962162366a86a6229038443847be7=1528766236; GA_GTID=0d300060-0002-5db8-a1ce-7a91780e24c2; city=hz; 58home=hz; commontopbar_new_city_info=79%7C%E6%9D%AD%E5%B7%9E%7Chz; commontopbar_ipcity=cq%7C%E9%87%8D%E5%BA%86%7C0; wmda_session_id_2385390625025=1528867641873-ab416daa-d36e-bea5; new_uv=33; utm_source=; spm=; init_refer=http%253A%252F%252Fhz.58.com%252Fchuzu%252Fpn5%252F%253FPGTID%253D0d3090a7-0004-f0f2-7475-d85fcb58b3fd%2526ClickID%253D2; new_session=0; ppStore_fingerprint=F8BD216772CDE94ECBA564957F9440F28A74D0AFCD3F6DF3%EF%BC%BF1528867684762; Hm_lvt_dcee4f66df28844222ef0479976aabf1=1528799952,1528867685'

}

url = "http://www.58.com/changecity.aspx?PGTID=0d000000-0000-061c-9652-5a9c39dacda1&ClickID=1"
# prox = random.choice(get_prox_list.join_str())
# print(type(prox))

# 125.94.0.251:8080
# 182.129.211.23:9000


proxies = {"http": '182.129.211.23:9000'}


def detail(url):
    '''
    获取页面源码
    :return:
    '''
    try:
        # request = urllib2.Request(url, headers=UA)
        response = requests.get(url, headers=UA)
        # response = requests.get(url, headers=UA, proxies=proxies, timeout=10)
        # print response.read()
        # print '-' * 15
        details = response.text
    except:
        print("未获取到数据，代理有问题？")
    finally:
        return details


def regx_select(details):
    '''
    各地链接
    :param details:
    :return:
    '''

    # 地址匹配
    regx = r"(http\:\/\/[a-z]{2,14}\.58\.com)"
    pattern = re.compile(regx)
    v_list = pattern.findall(details)
    # print(v_list)

    # 删除无效地址
    v_list.remove("http://user.58.com")
    v_list.remove("http://static.58.com")
    v_list.remove("http://about.58.com")
    v_list.remove("http://quanguo.58.com")
    # v_list.remove("http://pic2.58.com")

    return v_list


def snd_url():
    '''
    拼接租房二级页面地址

    :return:
    '''
    # details = detail()
    index_list = regx_select(detail(url))
    finall_list = []

    inputname = raw_input('press in name:')

    try:
        for links in index_list:
            for sec in link2nd_tool.linkstr(detail(links)):
                print
                links + sec + '>>>>>>  is  found'
                finall_list.append(links + sec)
                print
                finall_list
                print
                "\r\n" * 10 + "-" * 30
                IOutils.rtfile_input(str(finall_list), (inputname + '.txt'))
                time.sleep(numpy.random.randint(1, 4))
    except:
        print("官方个别分站内容未填充，已跳过。。。")

    finally:
        return finall_list

#
# def main():
#     '''
#     将地址列表保存文件
#     :return:
#     '''
#     try:
#         content = snd_url()
#         IOutils.rtfile(content)
#     except:
#         print('虽然他会报错但是貌似已经干完活了')
#
#     finally:
#         pass
#
#
# main()
