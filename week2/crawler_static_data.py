#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 22:03:20 2020

@author: Wangjue
"""

import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://fas.calendar.utoronto.ca/section/Actuarial-Science')
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')
#带有h3标签以及 'views-accordion-courses_view-block-header' 内容的部分
pattern = soup.find_all('h3','views-accordion-courses_view-block-header')
for item in pattern:
    print(item.string)
    
print("========================")
#Using Regex to match proper content
pattern_s = re.compile('<h3 class="views-accordion-courses_view-block-header">\n(.*)</h3>')
p = re.findall(pattern_s, r.text)
for item in p:
    print(item)
print("Total courses: ", len(p))