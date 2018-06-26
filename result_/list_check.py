# -*- coding:utf-8 -*-

import os.path
import sys
import json

# from ..IOutils import rtfile_input

reload(sys)
sys.setdefaultencoding('utf-8')

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

# result = json.dumps(yourdata, default=set_default)


def done_lis():
    '''
    已经拿到数据的项目的地址列表
    :return:
    '''

    # 获取目录下所有文件
    path = 'F:\\project\\project58\\result_\\'
    files = os.listdir(path.decode('utf-8'))
    # 已经有数据的url列表
    done_list = []
    json_list = []

    # 提取文件内容
    for file in files:
        if 'json' in file:
            # 准确获取一个txt的位置，利用字符串的拼接
            txt_path = path + file
            # print txt_path
            text = open(txt_path, 'r')
            text = text.read()
            dict_s = json.loads(text)
            # print dict_s
            url = dict_s["url_now"]
            url = str(url)
            # print(type(url))
            done_list.append(url)
            json_list.append(dict_s)
    # son_list = set(json_list)

    jStr = json.dumps(json_list, ensure_ascii=False, indent=1,default=set_default)
    fd = open('One.json', 'w')
    fd.write(jStr)
    fd.close()
    # print done_list
    return done_list

# 合并json数据到一个文件中
done_lis()
