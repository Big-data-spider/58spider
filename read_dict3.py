# -*- coding:utf-8 -*-

import ast

def dictit():
    '''
    地市列表读取
    :return:
    '''

    try:
        fd = open('inde_dictss.txt', 'r')

        try:
            all_text = fd.read()

        finally:
            fd.close()

    except IOError:
        print('open error')

    print()

    dict_res = ast.literal_eval(all_text)

    # print dict_res
    # print type(dict_res)

    return dict_res
