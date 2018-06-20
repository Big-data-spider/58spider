# -*- coding:utf-8 -*-

'''
json读取保存，保存的文件名为保存的详细时间。
'''

import json
import IOutils


class JsonFromatter:
    '''
    设置字段
    '''

    def __init__(self,
                 region="中国",
                 province="",
                 city="",
                 district="未填写",
                 title="",
                 rental_type="",
                 url_now="",
                 rent="需详谈",
                 lease="未指定",
                 area="未填写",
                 heading="未填写",
                 community='未填写',
                 address="未填写",
                 contacts="未填写",
                 phone="未填写",
                 detail="未填写",
                 facility="未展示",
                 advantage="未填写",
                 pics={},
                 encoding="utf-8"
                 ):

        self.region = region
        self.province = province
        self.city = city
        self.district = district
        self.title = title
        self.rental_type = rental_type
        self.url_now = url_now
        self.rent = rent
        self.lease = lease
        self.area = area
        self.heading = heading
        self.community = community
        self.address = address
        self.contacts = contacts
        self.phone = phone
        self.detail = detail
        self.facility = facility
        self.advantage = advantage
        self.pics = pics
        self.encoding = encoding

    def detals(self):
        # 内容
        detel = {
            "region": self.region,
            "province": self.province,
            "city": self.city,
            "district": self.district,
            "title": self.title,
            "rental_type": self.rental_type,
            "url_now": self.url_now,
            "rent": self.rent,
            "lease": self.lease,
            "area": self.area,
            "heading": self.heading,
            "community": self.community,
            'address': self.address,
            "contacts": self.contacts,
            "phone": self.phone,
            "detail": self.detail,
            "facility": self.facility,
            "advantage": self.advantage,
            "pics": self.pics
        }
        # print(detel)

        return detel

    def json_dump_self(self):
        details = self.detals()
        jStr = json.dumps(details, ensure_ascii=False,indent=1)
        print(jStr)
        IOutils.rtfile_time(jStr, "json")


def main():
    JsonFromatter().json_dump_self()

main()