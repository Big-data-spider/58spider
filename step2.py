# -*- coding:utf-8 -*-

import IOutils
import get_itempage_url
import numpy
import time
import haoitem
import json


def step2():
    '''
    得到数据
    :return:
    '''

    # 读取上一阶段保存的列表
    fd = open('chuzu_list.txt', 'r')
    all_text = fd.read()
    fd.close()
    # 列表处理
    L = all_text.replace('[', '')
    L = L.replace(']', '')
    L = L.replace('\'', '')
    chuzu_list = L.split(",")
    chuzu_list = list(set(chuzu_list))

    # 详情页处理
    item_pages = []
    for i in chuzu_list:
        print i
        it_urls = get_itempage_url.get_url(i)
        time.sleep(numpy.random.randint(3, 6))
        # 详情获取和保存
        for url in it_urls:
            try:
                city, district, title, rental_type, phone_num, contacts, url_now, rent, lease, area, heading, community, address, detail, facility, advantage, pic = haoitem.get_items(
                    url)
                c_name = haoitem.get_cname()
                region, province = haoitem.get_region(c_name)

                detel = {
                    "region": region,
                    "province": province,
                    "city": city,
                    "district": district,
                    "title": title,
                    "rental_type": rental_type,
                    "url_now": url_now,
                    "rent": rent,
                    "lease": lease,
                    "area": area,
                    "heading": heading,
                    "community": community,
                    'address': address,
                    "contacts": contacts,
                    "phone": phone_num,
                    "detail": detail,
                    "facility": facility,
                    "advantage": advantage,
                    "pics": pic
                }

                jStr = json.dumps(detel, ensure_ascii=False, indent=1)
                IOutils.rtfile_time(jStr, 'json')
                time.sleep(numpy.random.randint(3, 6))
            except:
                print('看来有的页面有问题，触发反爬了,休息片刻')
                time.sleep(15)

            # finally:
            #     return item_pages

            if it_urls != None:
                it_pages = item_pages.append(it_urls)

    print it_pages

    # 详情页列表保存
    file_zf = open('zf_item_list.txt', 'w')
    file_zf.write(str(it_pages))
    file_zf.close()


# 调用即可爬取数据并保存为json文件

step2()
