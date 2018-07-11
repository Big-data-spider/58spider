# -*- coding:utf-8 -*-

import IOutils
import get_itempage_url
import numpy
import time
import haoitem
import json
from result_ import list_check
import random
import get_city_info
import write_db


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
    # 出租房页面列表
    chuzu_list = list(set(chuzu_list))
    # 已有数据列表
    done_list = list_check.done_lis()
    print(done_list)
    # 出错列表
    error_list = []

    # 详情页处理
    item_pages = []
    random.shuffle(chuzu_list)
    for i in chuzu_list:
        # 显示当前页面地址
        print i
        it_urls = get_itempage_url.get_url(i)
        time.sleep(numpy.random.randint(3, 6))
        # 详情获取和保存
        for url in it_urls:
            if url not in done_list:
                if 'e.58.com' in url:
                    print('无效地址。。下一个')

                elif 'jxjump' in url:
                    print('无效地址。。下一个')
                else:
                    if 'short.58.com' in url:
                        url = url.replace('&end=end', '')
                    print('############################当前地址不在已完成列表中############################')
                    try:
                        # 得到页面数据
                        city, district, title, rental_type, phone_num, contacts, url_now, rent, lease, area, heading, community, address, detail, facility, advantage, pic = haoitem.get_items(
                            url)
                        # 得到处理后城市名
                        c_name = haoitem.get_cname()
                        # 所在地区和省份
                        region, province = get_city_info.get_areas(c_name)
                        # 保存到json的内容
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
                            "area": area.replace(' ', ''),
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
                        IOutils.rtfile_time_with_path(jStr, 'json')
                        write_db.data_in(detel)
                        time.sleep(numpy.random.randint(3, 6))

                    except:
                        print('########################看来有的页面有问题，触发反爬了,休息片刻########################')
                        print('#' * 20 + url + '\t' + '#' * 20)
                        error_list.append(url)
                        time.sleep(15)
            else:
                print('############################页面已经搞过了，下一个############################')
                time.sleep(numpy.random.randint(3, 5))
            # finally:
            #     return item_pages

            if it_urls != None:
                it_pages = item_pages.append(it_urls)

    print it_pages

    # 详情页列表保存
    file_zf = open('zf_item_list.txt', 'w')
    file_zf.write(repr(it_pages))
    file_zf.close()

    file_zf = open('error_list.txt', 'w')
    file_zf.write(repr(error_list))
    file_zf.close()

    return error_list


# 调用即可爬取数据并保存为json文件

step2()
