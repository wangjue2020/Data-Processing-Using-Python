#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 21:10:00 2020

@author: Wangjue


"""

import requests
import re
from bs4 import BeautifulSoup

'''
抓取university of Toronto Faculty of Arts and Science底下
computer science program所提供的所有课程编码以及课程名称,并计算每一个level有多少门课
'''
def computerScienceCourses():
    r = requests.get('https://fas.calendar.utoronto.ca/section/Computer-Science')
    '''
    soup = BeautifulSoup(r.text, 'lxml')
    
    result  = soup.find_all('h3','views-accordion-courses_view-block-header')
    for item in result:
        print(item)
     '''
    pattern = re.compile('<h3 class="views-accordion-courses_view-block-header">\s+CSC(\d{3})H1\s+-\s+(.*)\s+<\/h3>')
    result = re.findall(pattern, r.text)
    count1 = 0;
    count2 = 0;
    count3 = 0;
    count4 = 0;
    for course_code, course_name in result:
        #print(course_code, course_name, sep=',')
        if course_code.startswith('1'):
            count1+=1
        elif course_code.startswith('2'):
            count2+=1
        elif course_code.startswith('3'):
            count3+=1
        else:
            count4+=1
    print("There are {0} 100-level courses, {1} 200-level courses, {2} 300-level courses, and {3} 400-level courses.".format(count1, count2, count3,count4))
    print("Total: {} courses".format(len(result)))
    



'''
在“https://money.cnn.com/data/markets/nasdaq/”抓取纳斯达克成分股数据并将以下数据表抓取到一个列表中输出
'''
def nasDaq(url):
    answer = []
    r = requests.get(url)
    #获取<thead>...</thead>中的信息
    head = re.findall('<thead>(.*?)</thead>', r.text)
    table_heads = ['Company']+ re.findall('<th>(.+?)<\/th>',head[0])
    table_heads[-1] = table_heads[-1].replace('<br/>', ' ')
    answer.append(table_heads)
    body = re.findall('<tbody>(.*?)<\/tbody>', r.text)
    content_pattern = '<td.*?><a.*?>(.*?)<\/a>&nbsp;<\/td><td><span.*?>(.*?)<\/span><\/td><td><span.*?><span.*?>(.*?)<\/span><\/span><\/td><td><span.*?><span.*?>(.*?)<\/span><\/span><\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td>'
    table_content = re.findall(content_pattern, body[0])
    for item in table_content:
        temp = list(item)
        if temp[-1] != '--':
            newYTD = re.findall('<span.*?>(.*?)</span>', temp[-1])
            temp[-1] = newYTD[0]
        answer.append(temp)
    return answer

def volleyball(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as err:
        return err
    r.encoding = r.apparent_encoding
    # 一定要把下面这3行写在同一行上
    pattern = re.compile('href="/en/vnl/%s/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td></td>\s+<td class=".*?">(.*?)</td>\s+<td class=".*?">(.*?)</td>\s+<td class=".*?">(.*?)</td>' % 2019)
    p = re.findall(pattern, r.text)
    return p



if __name__ == "__main__":
    #computerScienceCourses()
    #ans = nasDaq('https://money.cnn.com/data/markets/nasdaq/')
    #print(ans)
    url = 'http://www.volleyball.world/en/vnl/%s/women/resultsandranking/round1' % 2019
    result = volleyball(url)
    print(result)