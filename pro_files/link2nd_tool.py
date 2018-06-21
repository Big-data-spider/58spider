# -*- coding:utf-8 -*-


from lxml import etree


def linkstr(content):
    dom = etree.HTML(content)
    try:
        if ('//*[@id="fcNav"]/em/a[1]') != None:
            url_list = dom.xpath('//*[@id="fcNav"]/em/a[1]')
            # 判断是否有其他二级域名
            if dom.xpath('//*[@id="fcNav"]/em/a[2]') != None:
                url_list.append((dom.xpath('//*[@id="fcNav"]/em/a[2]'))[0])
                if dom.xpath('//*[@id="fcNav"]/em/a[3]') != None:
                    url_list.append((dom.xpath('//*[@id="fcNav"]/em/a[3]'))[0])
    except:
        print('官方个别分站内容未填充，已跳过。。。')


    second_link = []

    for urls in url_list:
        if len(urls.attrib) != 0:
            # print urls.attrib['href']
            second_link.append(urls.attrib['href'])

    # print second_link
    return second_link


import requests
import Useragent

# url = "http://qd.58.com"

# UA = {"User-Agent": Useragent.RandomUAMiddleware().process_request()}
#
#
# def gethtml(url, *args):
#     html = requests.get(url, *args).content
#
#     return html

# def main():
#     linkstr()
#
# main()
