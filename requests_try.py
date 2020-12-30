#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 21:46:08 2020

@author: Wangjue
"""

import requests

r = requests.get('https://www.baidu.com/img/bd_logo1.png')

with open('baidu.png', 'wb') as f:
    f.write(r.content)