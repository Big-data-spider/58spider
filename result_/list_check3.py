import os.path
# import sys
import json


# # from ..IOutils import rtfile_input
#
# reload(sys)
# sys.setdefaultencoding('utf-8')


def done_lis():
    '''
    已经拿到数据的项目的地址列表
    :return:
    '''

    # 获取目录下所有文件
    path = 'F:\\project\\project58\\result_\\'
    files = os.listdir(path)
    # 已经有数据的url列表
    done_list = []
    json_list = []

    # 提取文件内容
    for file in files:
        if 'json' in file:
            # 准确获取一个txt的位置，利用字符串的拼接
            txt_path = path + file
            # print txt_path
            text = open(txt_path, 'r', encoding='utf-8')
            text = text.read()
            dict_s = json.loads(text)
            # print dict_s
            url = dict_s["url_now"]
            url = str(url)
            # print(type(url))
            done_list.append(url)
            json_list.append(dict_s)

    son_list = set()
    print(son_list)
    json_list = tuple(json_list)
    son_list.add(json_list)
    print(son_list)
    jStr = json.dumps(son_list, ensure_ascii=False, indent=1)
    fd = open('One.json', 'w')
    fd.write(jStr)
    fd.close()
    # print done_list
    return done_list


done_lis()
