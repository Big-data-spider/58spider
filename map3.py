from lxml import etree
import requests
from fake_useragent import UserAgent
import IO3



def map_dict():


    map_dicts = {
        ('华北', '河北'): ['北京', '天津'],
        ('华东', '浙江'): ['上海', '杭州'],
        ('华南', '广东'): ['广州', '深圳'],
        ('西南', '四川'): ['成都', '重庆'],
        ('中南', '江苏'): ['南京'],
        ('华中', '湖北'): ['武汉'],
    }

    url = 'http://www.58.com/changecity.aspx?PGTID=0d000000-0000-06f6-e5ac-eeb40259a664&ClickID=1'
    content = requests.get(url=url, headers={'User-Agent': UserAgent().random}).text

    # print content

    dom = etree.HTML(content, parser=etree.HTMLParser(encoding='utf-8'))

    # 华东 山东 江苏 浙江 安徽

    huadong = '华中'
    # print huadong

    # 山东
    shandong = '山东'
    # print shandong
    sd_citys = dom.xpath('//*[@id="clist"]/dd[2]/a/text()')
    # print sd_citys

    if map_dicts.get((huadong, shandong)) == None:
        map_dicts[(huadong, shandong)] = sd_citys
    else:
        sd_c = map_dicts.get((huadong, shandong))
        for i in sd_citys:
            sd_c.append(i)
        map_dicts[(huadong, shandong)] = list(set(sd_c))
    # print map_dicts

    # 江苏
    jiangsu = '江苏'
    js_citys = dom.xpath('//*[@id="clist"]/dd[3]/a/text()')

    if map_dicts.get((huadong, jiangsu)) == None:
        map_dicts[(huadong, jiangsu)] = js_citys
    else:
        js_c = map_dicts.get((huadong, jiangsu))
        for i in js_citys:
            js_c.append(i)
        map_dicts[(huadong, jiangsu)] = list(set(js_c))

    # 浙江
    zhejiang = '浙江'
    zj_citys = dom.xpath('//*[@id="clist"]/dd[4]/a/text()')

    if map_dicts.get((huadong, zhejiang)) == None:
        map_dicts[(huadong, zhejiang)] = zj_citys
    else:
        zj_c = map_dicts.get((huadong, zhejiang))
        for i in zj_citys:
            zj_c.append(i)
        map_dicts[(huadong, zhejiang)] = list(set(zj_c))

    # 安徽
    anhui = '安徽'
    ah_citys = dom.xpath('//*[@id="clist"]/dd[5]/a/text()')

    if map_dicts.get((huadong, anhui)) == None:
        map_dicts[(huadong, anhui)] = ah_citys
    else:
        ah_c = map_dicts.get((huadong, anhui))
        for i in ah_citys:
            ah_c.append(i)
        map_dicts[(huadong, anhui)] = list(set(ah_c))

    # 华南 广东 福建 广西 海南
    huanan = '华南'

    # 广东
    guangdong = '广东'
    gd_citys = dom.xpath('//*[@id="clist"]/dd[6]/a/text()')

    if map_dicts.get((huanan, guangdong)) == None:
        map_dicts[(huanan, guangdong)] = gd_citys
    else:
        gd_c = map_dicts.get((huanan, guangdong))
        for i in gd_citys:
            gd_c.append(i)
        map_dicts[(huanan, guangdong)] = list(set(gd_c))

    # 福建
    fujian = '福建'
    fj_citys = dom.xpath('//*[@id="clist"]/dd[7]/a/text()')

    if map_dicts.get((huanan, fujian)) == None:
        map_dicts[(huanan, fujian)] = fj_citys
    else:
        fj_c = map_dicts.get((huanan, fujian))
        for i in fj_citys:
            fj_c.append(i)
        map_dicts[(huanan, fujian)] = list(set(fj_c))

    # 广西
    guangxi = '广西'
    gx_citys = dom.xpath('//*[@id="clist"]/dd[8]/a/text()')

    if map_dicts.get((huanan, guangxi)) == None:
        map_dicts[(huanan, guangxi)] = gx_citys
    else:
        gx_c = map_dicts.get((huanan, guangxi))
        for i in gx_citys:
            gx_c.append(i)
        map_dicts[(huanan, guangxi)] = list(set(gx_c))

    # 海南
    hainan = '海南'
    hn_citys = dom.xpath('//*[@id="clist"]/dd[9]/a/text()')

    if map_dicts.get((huanan, hainan)) == None:
        map_dicts[(huanan, hainan)] = hn_citys
    else:
        hn_c = map_dicts.get((huanan, hainan))
        for i in hn_citys:
            hn_c.append(i)
        map_dicts[(huanan, hainan)] = list(set(hn_c))

    # 中南 河南 湖北 湖南 江西
    zhongnan = '中南'

    # 河南
    henan = '河南'
    hen_citys = dom.xpath('//*[@id="clist"]/dd[10]/a/text()')

    if map_dicts.get((zhongnan, henan)) == None:
        map_dicts[(zhongnan, henan)] = hen_citys
    else:
        hen_c = map_dicts.get((zhongnan, henan))
        for i in hen_citys:
            hen_c.append(i)
        map_dicts[(zhongnan, henan)] = list(set(hen_c))

    # 湖北
    hubei = '湖北'
    hb_citys = dom.xpath('//*[@id="clist"]/dd[11]/a/text()')

    if map_dicts.get((zhongnan, hubei)) == None:
        map_dicts[(zhongnan, hubei)] = hb_citys
    else:
        hb_c = map_dicts.get((zhongnan, hubei))
        for i in hb_citys:
            hb_c.append(i)
        map_dicts[(zhongnan, hubei)] = list(set(hb_c))

    hunan = '湖南'
    hun_citys = dom.xpath('//*[@id="clist"]/dd[11]/a/text()')

    if map_dicts.get((zhongnan, hunan)) == None:
        map_dicts[(zhongnan, hunan)] = hun_citys
    else:
        hun_c = map_dicts.get((zhongnan, hunan))
        for i in hun_citys:
            hun_c.append(i)
        map_dicts[(zhongnan, hunan)] = list(set())

    jiangxi = '江西'
    jx_citys = dom.xpath('//*[@id="clist"]/dd[13]/a/text()')

    if map_dicts.get((zhongnan, jiangxi)) == None:
        map_dicts[(zhongnan, jiangxi)] = jx_citys
    else:
        jx_c = map_dicts.get((zhongnan, jiangxi))
        for i in jx_citys:
            jx_c.append(i)
        map_dicts[(zhongnan, jiangxi)] = list(set(jx_c))

    # 东北 辽宁 黑龙江 吉林
    dongbei = '东北'

    liaoning = '辽宁'
    ln_citys = dom.xpath('//*[@id="clist"]/dd[14]/a/text()')

    if map_dicts.get((dongbei, liaoning)) == None:
        map_dicts[(dongbei, liaoning)] = ln_citys
    else:
        ln_c = map_dicts.get((dongbei, liaoning))
        for i in ln_citys:
            ln_c.append(i)
        map_dicts[(dongbei, liaoning)] = list(set(ln_c))

    heilongjiang = '黑龙江'
    hlj_citys = dom.xpath('//*[@id="clist"]/dd[15]/a/text()')

    if map_dicts.get((dongbei, heilongjiang)) == None:
        map_dicts[(dongbei, heilongjiang)] = hlj_citys
    else:
        hlj_c = map_dicts.get((dongbei, heilongjiang))
        for i in hlj_citys:
            hlj_c.append(i)
        map_dicts[(dongbei, heilongjiang)] = list(set(hlj_c))

    jilin = '吉林'
    jl_citys = dom.xpath('//*[@id="clist"]/dd[16]/a/text()')

    if map_dicts.get((dongbei, jilin)) == None:
        map_dicts[(dongbei, jilin)] = jl_citys
    else:
        jl_c = map_dicts.get((dongbei, jilin))
        for i in jl_citys:
            jl_c.append(i)
        map_dicts[(dongbei, jilin)] = list(set(jl_c))

    xinan = '西南'

    sichuan = '四川'
    sc_citys = dom.xpath('//*[@id="clist"]/dd[17]/a/text()')

    if map_dicts.get((xinan, sichuan)) == None:
        map_dicts[(xinan, sichuan)] = sc_citys
    else:
        sc_c = map_dicts.get((xinan, sichuan))
        for i in sc_citys:
            sc_c.append(i)
        map_dicts[(xinan, sichuan)] = list(set(sc_c))

    yunnan = '云南'
    yn_citys = dom.xpath('//*[@id="clist"]/dd[18]/a/text()')

    if map_dicts.get((xinan, yunnan)) == None:
        map_dicts[(xinan, yunnan)] = yn_citys
    else:
        yn_c = map_dicts.get((xinan, yunnan))
        for i in yn_citys:
            yn_c.append(i)
        map_dicts[(xinan, yunnan)] = list(set(yn_c))

    guizhou = '贵州'
    gz_citys = dom.xpath('//*[@id="clist"]/dd[19]/a/text()')

    if map_dicts.get((xinan, guizhou)) == None:
        map_dicts[(xinan, guizhou)] = gz_citys
    else:
        gz_c = map_dicts.get((xinan, guizhou))
        for i in gz_citys:
            gz_c.append(i)
        map_dicts[(xinan, guizhou)] = list(set(gz_c))

    xizang = '西藏'
    xz_citys = dom.xpath('//*[@id="clist"]/dd[20]/a/text()')

    if map_dicts.get((xinan, xizang)) == None:
        map_dicts[(xinan, xizang)] = xz_citys
    else:
        xz_c = map_dicts.get((xinan, xizang))
        for i in xz_citys:
            xz_c.append(i)
        map_dicts[(xinan, xizang)] = list(set(xz_c))

    huabei = '华北'

    hebei = '河北'
    heb_citys = dom.xpath('//*[@id="clist"]/dd[21]/a/text()')

    if map_dicts.get((huabei, hebei)) == None:
        map_dicts[(huabei, hebei)] = heb_citys
    else:
        heb_c = map_dicts.get((huabei, hebei))
        for i in heb_citys:
            heb_c.append(i)
        map_dicts[(huabei, hebei)] = list(set(heb_c))

    shanxi = '山西'
    sx_citys = dom.xpath('//*[@id="clist"]/dd[22]/a/text()')

    if map_dicts.get((huabei, shanxi)) == None:
        map_dicts[(huabei, shanxi)] = sx_citys
    else:
        sx_c = map_dicts.get((huabei, shanxi))
        for i in sx_citys:
            sx_c.append(i)
        map_dicts[(huabei, shanxi)] = list(set(sx_c))

    neimenggu = '内蒙古'
    nmg_citys = dom.xpath('//*[@id="clist"]/dd[23]/a/text()')

    if map_dicts.get((huabei, neimenggu)) == None:
        map_dicts[(huabei, neimenggu)] = nmg_citys
    else:
        nmg_c = map_dicts.get((huabei, neimenggu))
        for i in nmg_citys:
            nmg_c.append(i)
        map_dicts[(huabei, neimenggu)] = list(set(nmg_c))

    xibei = '西北'

    shanxi2 = '陕西'
    sx2_citys = dom.xpath('//*[@id="clist"]/dd[24]/a/text()')

    if map_dicts.get((xibei, shanxi2)) == None:
        map_dicts[(xibei, shanxi2)] = sx2_citys
    else:
        sx2_c = map_dicts.get((xibei, shanxi2))
        for i in sx2_citys:
            sx2_c.append(i)
        map_dicts[(xibei, shanxi2)] = list(set(sx2_c))

    xinjiang = '新疆'
    xj_citys = dom.xpath('//*[@id="clist"]/dd[25]/a/text()')

    if map_dicts.get((xibei, xinjiang)) == None:
        map_dicts[(xibei, xinjiang)] = xj_citys
    else:
        xj_c = map_dicts.get((xibei, xinjiang))
        for i in xj_citys:
            xj_c.append(i)
        map_dicts[(xibei, xinjiang)] = list(set(xj_c))

    gansu = '甘肃'
    gs_citys = dom.xpath('//*[@id="clist"]/dd[26]/a/text()')

    if map_dicts.get((xibei, gansu)) == None:
        map_dicts[(xibei, gansu)] = gs_citys
    else:
        gs_c = map_dicts.get((xibei, gansu))
        for i in gs_citys:
            gs_c.append(i)
        map_dicts[(xibei, gansu)] = list(set(gs_c))

    ningxia = '宁夏'
    nx_citys = dom.xpath('//*[@id="clist"]/dd[27]/a/text()')

    if map_dicts.get((xibei, ningxia)) == None:
        map_dicts[(xibei, ningxia)] = nx_citys
    else:
        nx_c = map_dicts.get((xibei, ningxia))
        for i in nx_citys:
            nx_c.append(i)
        map_dicts[(xibei, ningxia)] = list(set(nx_c))

    qinghai = '青海'
    qh_citys = dom.xpath('//*[@id="clist"]/dd[28]/a/text()')
    # for i in qh_citys:
    #     print i

    if map_dicts.get((xibei, qinghai)) == None:
        map_dicts[(xibei, qinghai)] = qh_citys
    else:
        qh_c = map_dicts.get((xibei, qinghai))
        for i in qh_citys:
            qh_c.append(i)
        map_dicts[(xibei, qinghai)] = list(set(qh_c))

    qita = '其他'
    qt_citys = dom.xpath('//*[@id="clist"]/dd[29]/a/text()')

    if map_dicts.get((qita, qita)) == None:
        map_dicts[(qita, qita)] = qt_citys
    else:
        qt_c = map_dicts.get((qita, qita))
        for i in qt_citys:
            qt_c.append(i)
        map_dicts[(qita, qita)] = list(set(qt_c))

    # for kv in map_dicts.items():
    #     for i in kv:
    #         for p in i:
    #             print p
    # print map_dicts

    return map_dicts

    # return map_dicts

    # def city_info(city_name):
    #     '''
    #     城市所在字典条目读取
    #     :param city_name:
    #     :return:
    #     '''
    #     dict_map = map_dict(url)

def save_dicts():
    dic = map_dict()
    strs = repr(dic)
    print(strs)

    IO3.rtfile(strs)


def result(city_name):
    map_dicts = map_dict()
    for key, value in map_dicts.items():
        if city_name in value:
            # print key
            # for i in key:
            #     print i
            # print type(key)
            x = list(key)
            o = []
            for i in x:
                o.append(i)
            # print o
            return o
    # print o

def get_res(city_name):
    res = result(city_name)
    return res



def get_region(city):
    # content = page_content(url)
    # dom = etree.HTML(content)
    #
    # city = dom.xpath('//div[@class="nav-top-bar fl c_888 f12"]/a/text()')[0].replace('58同城', '')

    region = get_res(city)

    # 省份
    province = get_res(city)

    return [region, province]


###########################

save_dicts()

# url = 'http://cq.58.com/zufang/34391304233283x.shtml?from=1-list-15&iuType=i_2&PGTID=0d3090a7-0002-5b2e-6486-07791c63fe7a&ClickID=3'

# dicts = map_dict()

# city = get_items(url)

# result('西安')
# print get_region(city)

