# -*- coding:utf-8 -*-
'''
获取分类分页url
'''

# import parents_urllist
import time
import numpy
import bs4
import IOutils
from lxml import etree
import re
import requests
from fake_useragent import UserAgent


def file_rt(page_list):
    '''
    结果保存
    :param page_list:
    :return:
    '''
    IOutils.rtfile_time(str(page_list), "txt")
    print "列表完成"


def chuzu_pages(url, page_list):
    '''
    xpath元素提取
    :param detail:
    :return:
    '''
    # detail = parents_urllist.detail(url)

    detail = requests.get(url=url, headers={'User-agent': UserAgent().random}).text

    try:

        soup = bs4.BeautifulSoup(detail)

        if soup.find(class_="next") != None:
            # print type(soup.find(class_="next"))
            tag = soup.find(class_="next")
            if tag == None:
                return
            else:
                link = tag['href']
                if 'http' not in str(link):
                    # 正则筛选页数
                    key = str(link)
                    regx = r"\S+\/(pn\d+\/)"
                    pattern1 = re.compile(regx)  # 我们在编译这段正则表达式
                    matcher1 = re.search(pattern1, key)  # 在源文本中搜索符合正则表达式的部分
                    # print matcher1.group(1)  # 打印出来
                    link = url + matcher1.group(1)
                    page_list.append(link)
                    print(page_list)
                    time.sleep(numpy.random.randint(1, 4))

                    return chuzu_pages(link, page_list)

                else:
                    page_list.append(link)
                    print(page_list)
                    time.sleep(numpy.random.randint(1, 4))

                    return chuzu_pages(link, page_list)
        else:
            print '页面爬完了或者触发反爬了'


    except:
        print "Emmmmmm"
    #
    finally:

        time.sleep(numpy.random.randint(1, 4))
        # page_list.append(url)

        return page_list

    # return chuzu_pages(link)

    # return


def chuzu_page3(url, pagelist):
    '''
    用xpath获取地址列表
    :param pagelist: 最终结果列表
    :param url: 初始地址
    :return: 
    '''
    try:
        detail = requests.get(url=url, headers={'User-agent': UserAgent().random}).text
        time.sleep(numpy.random.randint(1, 4))
        dom = etree.HTML(detail)
        # x_path = '//*[@id="bottom_ad_li"]/div[2]/a[4]'
        x_path = '//*[@class="next"]'
        if len(dom.xpath(x_path)) != 0:
            urlend = dom.xpath(x_path)
            end_ur = urlend[0].attrib['href']
            # print urlend[0].attrib['href']
            if 'http' not in end_ur:

                key = str(end_ur)
                regx = r"\S+\/(pn\d+\/)"
                pattern1 = re.compile(regx)
                matcher1 = re.search(pattern1, key)

                pattern2 = re.compile(r'http\:\/\/[a-z]+\.58\.com\/(chuzu|ershoufang|pinpaigongyu)')
                matcher2 = re.search(pattern2, url)
                res_url = matcher2.group() + matcher1.group(1)
                if '/pn' not in res_url:
                    res_url = res_url.replace('pn', '/pn')

                # res_url = url + end_ur[1:]
                # print res_url
                pagelist.append(res_url)
                print(pagelist)
                time.sleep(numpy.random.randint(1, 4))
                return chuzu_page3(res_url, pagelist)


            else:
                if '/pn' not in end_ur:
                    end_ur.replace('pn', '/pn')
                pagelist.append(end_ur)
                print(pagelist)
                time.sleep(numpy.random.randint(1, 4))
                return chuzu_page3(end_ur, pagelist)

        else:
            print "要么是页面爬完了已经写入文件，要么是被反了，打开地址检查一下"
            return

    except:
        print '出错了'

    finally:
        return pagelist


########################################################
'''
测试部分
'''

# def str_control(url):
#     '''
#     元素明文化
#     :param url:
#     :return:
#     '''
#     detail = parents_urllist.detail(url)
#
#     elem = chuzu_page3(detail)
#
#     for st in elem:
#         if len(st.attrib) != 0:
#             page = st.attrib['href']
#
#         return page


# '''
# test
# '''
# url = 'http://jincheng.58.com/chuzu/'
# page_list = [url]
# chuzu_page3(url, page_list)
#
# file_rt(page_list)

# detail = parents_urllist.detail(url)

# page_lst(url)

# linkpage(detail)
