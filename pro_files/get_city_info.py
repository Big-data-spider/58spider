# -*- coding:utf-8 -*-

'''

行政区划
城市归属
地区归属
v3.1

'''

import json


def load_dict():
    '''
    读取内容
    :return:
    '''
    f = open('city_list_dict.json', 'r')
    lst = f.read()
    f.close()
    content = json.loads(lst)
    # print(content)
    return content


def get_provi(city_name):
    content = load_dict()

    for key, values in content[1].items():
        # 遍历城市
        # print(type(values))
        for city, short_name in values.items():
            # print(type(city))
            # city = str(city)
            city = city.encode("utf-8")
            if city_name == city:
                # print(type(key))
                # print(type(city_name))
                provi = key.replace(' ', '')
                # print(provi)
                return provi


def get_areas(city_name):
    content = load_dict()
    provi = get_provi(city_name)
    for areas, prov in content[0].items():
        # print(prov)
        for p, short_letter in prov.items():
            if p == provi:
                # print(areas)
                area = areas.replace(' ', '')
                print(area)
                print(provi)
                return area, provi

# cityname = "重庆"
# # get_result(cityname)
# get_areas(cityname)
# get_provi(cityname)
