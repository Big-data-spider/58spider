from lxml import etree
import requests
from fake_useragent import UserAgent
import read_dict3
import IO3


def page_content(url):
    '''
    获取页面源码
    :param url:
    :return:
    '''
    content = requests.get(url=url, headers={'User-Agent': UserAgent().random}).text

    return content


def get_items(url):
    '''
    获取
    :param content:
    :return:
    '''

    content = page_content(url)
    dom = etree.HTML(content, parser=etree.HTMLParser(encoding='utf-8'))
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

            fd = open('city_name_temp.txt', 'w', encoding='utf-8')
            fd.write(city)
            fd.close()

            # 所在区
            district = dom.xpath('//a[@class="c_333 ah"]/text()')[1]
            print(district)

            # 标题
            title = dom.xpath('//h1[@class="c_333 f20"]/text()')[0]
            print(title)

            # 整租还是单间出租
            rental_type = dom.xpath('//ul[@class="f14"]/li[1]//span/text()')[1]
            print(rental_type)

            # 租房电话
            if len(dom.xpath('//p[@class="phone-num"]/text()')) != 0:
                phone_num = dom.xpath('//p[@class="phone-num"]/text()')[0]
            elif len(dom.xpath('//span[@class="house-chat-txt"]/text()')) != 0:
                phone_num = dom.xpath('//span[@class="house-chat-txt"]/text()')[0]

            print(phone_num)

            # 租房联系人
            contacts = dom.xpath('//a[@class="c_000"]/text()')[0]

            print(contacts)

            # 当前页面链接地址
            url_now = url
            print(url_now)

            # 租金
            rent = dom.xpath('//b[@class="f36"]/text()')[0]
            print(rent)

            # 租赁方式
            lease = dom.xpath('//span[@class="c_333"]/text()')[0]
            print(lease)

            # 房屋套型
            area = dom.xpath('//ul[@class="f14"]/li[2]/span[2]/text()')[0]
            # /html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/span[2]
            print(area)

            # 朝向和楼层位置
            heading = dom.xpath('//ul[@class="f14"]/li[3]/span[2]/text()')[0]
            # /html/body/div[4]/div[2]/div[2]/div[1]/div[1]/ul/li[3]/span[2]
            print(heading)

            # 所在小区
            community = dom.xpath('//a[@class="c_333 ah"]/text()')[0]
            print(community)

            # 详细地址
            address = dom.xpath('//span[@class="dz"]/text()')[0]
            print(address)

            # 详情描述
            detail = dom.xpath('//ul[@class="introduce-item"]/li[2]/span[2]/text()')[0]
            # /html/body/div[4]/div[3]/div[1]/div[2]/ul/li[2]/span[2]
            print(detail)

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
            print(facility)

            # 房屋优势
            if len(dom.xpath('//ul[@class="introduce-item"]/li[1]/span[2]/text()')) != 0:
                advantage = dom.xpath('//ul[@class="introduce-item"]/li[1]/span[@class="a2"]/em/text()')[0]
            # /html/body/div[4]/div[3]/div[1]/div[2]/ul/li[1]/span[2]
            else:
                advantage = '未添加描述'
            print(advantage)

            # 图片
            pic = dom.xpath('//ul[@class="house-pic-list "]/li/img/@lazy_src')
            print(pic)


        elif '二手房' in zufang[1]:
            '''
            二手房 
            '''
            pass




    elif len(dom.xpath('//div[@class="curmbar"]/a/text()')) != 0:
        '''
        品牌公寓
        '''
        print(ppgy[1])


    else:
        print('遇到了没有匹配的规则')

    return city, district, title, rental_type, phone_num, contacts, url_now, rent, lease, area, heading, community, address, detail, facility, advantage, pic


def get_cname():
    fd = open('city_name_temp.txt', 'r', encoding='utf-8')

    all_text = fd.read()
    fd.close()
    city_name = all_text
    city_name = city_name.replace(' ', '')

    return city_name


def result(city_name):
    map_dicts = read_dict3.dictit()
    # print(map_dicts)
    kyes = []
    vs = []
    for key, value in map_dicts.items():
        kyes.append(key)
        vs.append(value)
    #
    # # print(kyes)
    # # print('000000000000000')
    # # print(vs)
    #
    for i in vs:
        if city_name in i:
            ind = vs.index(i)
            # print(ind)
            # print(vs[ind])
            # print(kyes[ind])
    res = list(kyes[ind])

    return res


def get_region(city):
    region = result(city)[0]
    print(region)

    # 省份
    province = result(city)[1]
    print(province)

    return region, province


#############################################



