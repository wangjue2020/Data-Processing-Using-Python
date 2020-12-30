#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 21:34:31 2020

@author: Wangjue
抓取需要遵守爬虫协议
抓取动态生成数据的页面：
    1、打开浏览器inspection
    2、inspection -> Network -> refresh page
    3、找到左边Name栏里跟get有关的一项并点击
    4、查看request url以及其他信息
"""

import requests
import re


r = requests.get('https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.34180284985036713&callback=jQuery111206947064704714496_1609295367193&_=1609295367194')

print("status_code: ", r.status_code)

decoded =r.text.encode('utf-8').decode('unicode-escape')#为了能将中文显示出来

print(decoded)
pattern = re.compile('"title":"(.*?)"')
#"title":"快讯：汽车板块大幅回暖 长城汽车大涨6%"
result = re.findall(pattern, decoded)
for i in result:
    print("\n\n")
    print(i)