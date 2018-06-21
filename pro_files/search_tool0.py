# -*- coding:utf-8 -*-

import urllib2
import urllib
import Useragent


UA = Useragent.RandomUAMiddleware().process_request()

keyword = raw_input("press in keyword")
get_param = {
    "key": keyword
}

data = urllib.urlencode(get_param)

url = "http://cq.58.com/chuzu/?"

full_url = url + data

print full_url

print '*'*14

request = urllib2.Request(full_url)

responses = urllib2.urlopen(request)

print responses.read()
