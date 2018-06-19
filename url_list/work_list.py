# -*- coding:utf-8 -*-

import os
import os.path
import re
import sys
import codecs

# from ..IOutils import rtfile_input

reload(sys)
sys.setdefaultencoding('utf-8')

# 这里放着你要操作的文件夹名称
path = 'F:\\project\\project58\\url_list\\'

files = os.listdir(path.decode('utf-8'))

# sed_r_list = []
res_list = []

for file in files:
    if 'txt' in file:
        # 准确获取一个txt的位置，利用字符串的拼接
        txt_path = path + file.decode('utf-8')
    # print txt_path

    fd = open(txt_path, 'r')
    all_text = fd.read()
    fd.close()
    res_str = all_text

    # 列表字符处理
    L = res_str.replace('[', '')
    L = L.replace(']', '')
    L = L.replace('\'', '')
    list_u = L.split(",")

    list_u = list(set(list_u))

    # print list_u

    for i in list_u:
        i.replace(' ', '')
        res_list.append(i)

res_list = list(set(res_list))

# print res_list

#     if len(list_u) < 40:
#         sed_r_list.append(list_u[0])
#
# print sed_r_list

chuzu_list = []
esf_list = []
ppgy_list = []

for i in res_list:
    if '/chuzu/' in i:
        chuzu_list.append(i)
    elif '/ershoufang/' in i:
        esf_list.append(i)
    elif '/pinpaigongyu/' in i:
        ppgy_list.append(i)

#
fd = open('chuzu_list.txt', 'w')

fd.write(str(chuzu_list))

fd.close()
fd = open('esf_list.txt', 'w')

fd.write(str(esf_list))

fd.close()
fd = open('ppgy_list.txt', 'w')

fd.write(str(ppgy_list))

fd.close()


# 把结果保存了在contents中
# contents = codecs.open(txt_path.decode('utf-8'), 'r', encoding='utf-8')
# print contents
# # datas的数据清空
# datas.clear()
# #
# # 把数据add到datas中，可以去重
# for content in contents:
#     print(content.decode('utf-8'))
#     datas.add(content.decode('utf-8'))
#
#     # 去重后新的文件保存的路径
# new_txt_path = 'F:/project/project58/url_list/result_list/result.txt'
# unique_keywords = codecs.open(new_txt_path.decode('utf-8'), 'w', encoding='utf-8')
#
# # 把datas里的数据输出到新生成的txt中
# for data in datas:
#     unique_keywords.write(data + "\n")
#
#     # 释放资源
# unique_keywords.close()
