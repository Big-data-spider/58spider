# -*- coding:utf-8 -*-

# import requests
# import re
import IOutils
import parents_urllist


def url_list():
    list_u = IOutils.readfile()

    return list_u


class linkQuence:
    def __init__(self):
        self.visited = []  # 已访问过的url初始化列表
        self.unvisited = []  # 未访问过的url初始化列表

    def getVisitedUrl(self):  # 获取已访问过的url
        return self.visited

    def getUnvisitedUrl(self):  # 获取未访问过的url
        return self.unvisited

    def addVisitedUrl(self, url):  # 添加已访问过的url
        return self.visited.append(url)

    def addUnvisitedUrl(self, url):  # 添加未访问过的url
        if url != '' and url not in self.visited and url not in self.unvisited:
            return self.unvisited.insert(0, url)

    def removeVisited(self, url):
        return self.visited.remove(url)

    def popUnvisitedUrl(self):  # 从未访问过的url中取出一个url
        try:  # pop动作会报错终止操作，所以需要使用try进行异常处理
            return self.unvisited.pop()
        except:
            return None

    def unvisitedUrlEmpty(self):  # 判断未访问过列表是不是为空
        return len(self.unvisited) == 0


class Spider:
    def __init__(self, url):
        self.linkQuence = linkQuence()
        self.linkQuence.addUnvisitedUrl(url)
        self.current_deepth = 1

    # def chuzu_regx(self, detail):
    #     dom = etree.HTML(detail)
    #     x_path = '//*[@id="bottom_ad_li"]/div[2]/a[4]'
    #     if x_path != None:
    #         urlend = dom.xpath(x_path)
    #         return urlend
    #
    #     else:
    #         print "not found"

    # def ershoufang_regx(self, detail):
    #
    #     pass
    #
    # def ppgy_regx(self, detail):
    #     pass

    def getPageLinks(self, url):

        url_nlist = [url]

        for url in url_list():

            if "chuzu" in url:
                detail = parents_urllist.detail(url)

                full_url = url + endurl
                url_nlist.append(full_url)




            elif "ershoufang" in url:
                pass

            elif "pinpaigongyu" in url:
                #先使用正则匹配地址再拼接字符串形成完整地址
                pass


    def get_all_link(self, url):
        pass

