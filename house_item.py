# -*- coding:utf-8 -*-

from lxml import etree
import requests
from fake_useragent import UserAgent
import place_map
import read_dict
import sys

reload(sys)


def page_content(url):
    '''
    获取页面源码
    :param url:
    :return:
    '''
    content = requests.get(url=url, headers={'User-Agent': UserAgent().random}).text

    type_s = sys.getdefaultencoding()
    content = content.decode('utf-8').encode(type_s)

    # print content
    return content


def get_items(url):
    '''
    获取
    :param content:
    :return:
    '''

    content = page_content(url)
    dom = etree.HTML(content,parser=etree.HTMLParser(encoding='utf-8'))
    # 整租
    zufang = dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')
    # 合租
    # hezu = dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')
    # # 二手房
    # esf = dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')
    # 品牌公寓
    ppgy = dom.xpath('//div[@class="curmbar"]/a/text()')
    # str_conditions = dom.xpath('/html/body/div[3]/div/a[2]/text()')

    if len(dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')) != 0:
        '''
        单间和出租房元素提取
        '''
        if '租房' in zufang[1]:
            '''
            单间和整租
            '''

            # 城市名
            city = dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')[0].replace('58同城', '')
            coco = dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')
            print city
            dodo = []
            for i in coco:
                h = i.encode('utf8')
                dodo.append(h)
                print h

            dodo = dodo[0].replace('58同城', '')
            print dodo

            # 所在区
            district = dom.xpath('//a[@class="c_333 ah"]/text()')[1]
            print district

            # 标题
            title = dom.xpath('//h1[@class="c_333 f20"]/text()')[0]
            print title

            # 整租还是单间出租
            rental_type = dom.xpath('//ul[@class="f14"]/li[1]//span/text()')[1]
            print rental_type

            # 租房电话
            if len(dom.xpath('//p[@class="phone-num"]/text()')) != 0:
                phone_num = dom.xpath('//p[@class="phone-num"]/text()')[0]
            elif len(dom.xpath('//span[@class="house-chat-txt"]/text()')) != 0:
                phone_num = dom.xpath('//span[@class="house-chat-txt"]/text()')[0]
            # print phone_num[0].replace(' ', '')
            print phone_num

            # 租房联系人
            contacts = dom.xpath('//a[@class="c_000"]/text()')[0]
            # print contacts[0].replace(' ', '')
            print contacts

            # 当前页面链接地址
            url_now = url
            print(url_now)

            # 租金
            rent = dom.xpath('//b[@class="f36"]/text()')[0]
            print rent

            # 租赁方式
            lease = dom.xpath('//span[@class="c_333"]/text()')[0]
            print lease

            # 房屋套型
            area = dom.xpath('//ul[@class="f14"]/li[2]/span[2]/text()')[0]
            # /html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/span[2]
            print area

            # 朝向和楼层位置
            heading = dom.xpath('//ul[@class="f14"]/li[3]/span[2]/text()')[0]
            # /html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[3]/span[2]
            print heading

            # 所在小区
            community = dom.xpath('//a[@class="c_333 ah"]/text()')[0]
            print community

            # 详细地址
            address = dom.xpath('//span[@class="dz"]/text()')[0]
            print address

            # 详情描述
            detail = dom.xpath('//ul[@class="introduce-item"]/li[2]/span[2]/text()')[0]
            # /html/body/div[4]/div[3]/div[1]/div[2]/ul/li[2]/span[2]
            print detail

            # 包含设施
            # /html/body/div[4]/div[3]/div[1]/ul[2]
            if len(dom.xpath('//ul[@class="house-disposal"]')) != 0:
                facility = dom.xpath('//ul[@class="house-disposal"]/li/text()')
                temp_list = ''
                for i in range(0, (len(facility) - 1)):
                    temp_list = temp_list + facility[i] + '.'
                facility = temp_list

            else:
                facility = '业主未提供此方面的信息'
            print facility

            # 房屋优势
            if len(dom.xpath('//ul[@class="introduce-item"]/li[1]/span[2]/text()')) != 0:
                advantage = dom.xpath('//ul[@class="introduce-item"]/li[1]/span[@class="a2"]/em/text()')[0]
            # /html/body/div[4]/div[3]/div[1]/div[2]/ul/li[1]/span[2]
            else:
                advantage = '未添加描述'
            print advantage

            # 图片
            pic = dom.xpath('//ul[@class="house-pic-list "]/li/img/@lazy_src')
            print pic


        elif '二手房' in zufang[1]:
            '''
            二手房 
            '''
            pass




    elif len(dom.xpath('//div[@class="curmbar"]/a/text()')) != 0:
        '''
        品牌公寓
        '''
        print ppgy[1]
    # elif str_conditions[0]:
    #     pass
    # elif str_conditions[0]:
    #     pass

    else:
        print '遇到了没有匹配的规则'

    return dodo


#############################################

'''
test_part
'''

# def get_region(url):
#
#     # content = page_content(url)
#     # dom = etree.HTML(content)
#     #
#     # city = dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')[0].replace('58同城', '')
#
#     region = place_map.result(city)[0]
#     print region
#
#     # 省份
#     province = place_map.result(city)[1]
#     print province


# 地区

# url = 'http://ch.58.com/zufang/34356781138239x.shtml?iuType=j_2&PGTID=0d3090a7-027f-5cb8-a136-8759d556fb5b&ClickID=1'

# url = 'http://short.58.com/zd_p/b196c590-1a85-485b-a43a-73eac841cd82/?target=eh-16-xgk_psfegvimob_85578462797327q-feykn&end=end&from=1-list-30'

url = 'http://cq.58.com/zufang/34405170401217x.shtml?fzbref=0&from=1-list-9&psid=177048582200413300325581577&iuType=gz_2&ClickID=2&apptype=0&key=&entinfo=34405170401217_0&params=busitime^desc&cookie=|||Ch8BCFsV5Kgb/jPrBvvWAg==&PGTID=0d3090a7-0002-546f-c14c-31f721d08b20&local=37&pubid=35376711&trackkey=34405170401217_40ccd3a6-a042-4dd1-9e55-10b0faec8b59_20180615110900_1529032140741&fcinfotype=gz'
#
name = get_items(url)
print place_map.get_region(name)
