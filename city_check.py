# -*- coding:utf-8 -*-

import house_item
import place_map

url = 'http://cq.58.com/zufang/34405170401217x.shtml?fzbref=0&from=1-list-9&psid=177048582200413300325581577&iuType=gz_2&ClickID=2&apptype=0&key=&entinfo=34405170401217_0&params=busitime^desc&cookie=|||Ch8BCFsV5Kgb/jPrBvvWAg==&PGTID=0d3090a7-0002-546f-c14c-31f721d08b20&local=37&pubid=35376711&trackkey=34405170401217_40ccd3a6-a042-4dd1-9e55-10b0faec8b59_20180615110900_1529032140741&fcinfotype=gz'

city_name = house_item.get_items(url)

r = place_map.result(city_name)

print place_map.get_region(city_name)
