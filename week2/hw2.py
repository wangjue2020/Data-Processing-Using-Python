#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 22:16:39 2021

@author: Wangjue
"""
import random

'''
1. 使用以下语句存储一个字符串： 

  string = 'My moral standing  is: 0.98765' 

将其中的数字字符串转换成浮点数并输出。   

（提示：可以使用find()方法和字符串切片或split()方法，提取出字符串中冒号后面的部分，然后使用float函数，将提取出来的字符串转换为浮点数）
'''

def q1():
    str = 'My moral standing  is: 0.98765' 
    l = str.split(':')
    num = l[1].lstrip()
    print(float(num))
    
'''
2. 自定义函数move_substr(s, flag, n)，将传入的字符串s按照flag（1代表循环左移，2代表循环右移）
的要求左移或右移n位（例如对于字符串abcde12345，循环左移两位后的结果为cde12345ab，循环右移两位后的结果为45abcde123），
结果返回移动后的字符串，若n超过字符串长度则结果返回-1。__main__模块中从键盘输入字符串、左移和右移标记以及移动的位数，
调用move_substr()函数若移动位数合理则将移动后的字符串输出，否则输出“the n is too large”。
'''
def move_substr(s, flag, n):
    if n > len(s):
        return -1
    if flag == 1:
        return s[n:]+s[:n]
    else:
        return s[-n:]+s[:-n]
        
'''
3.定义函数countchar()按字母表顺序统计字符串中26个字母出现的次数（不区分大小写）。例如字符串“Hope is a good thing.”的统计结果为：

[1, 0, 0, 1, 1, 0, 2, 2, 2, 0, 0, 0, 0, 1, 3, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0] 
'''

def countchar(s):
    lst = [0 for i in range(26)]
    for i in s:
        if i.isalpha():
            loc = ord(i)-ord('a')
            lst[loc]+=1
    return lst

'''
4. 从键盘输入整数n（1-9之间），对于1-100之间的整数删除包含n并且能被n整除的数，例如如果n为6，则要删掉包含6的如6，16这样的数及是6的倍数的如12和18这样的数，输出所有满足条件的数，要求每满10个数换行。 

测试数据： 

Enter the number: 6 
'''
def q4(n):
    count = 1
    for i in range(1,101):
        f = True
        if str(n) not in str(i) and i % n !=0 :
            if(count % 10 != 0):
                print(i, end=',')
            else:
                print(i, end='\n')
            count+=1

'''
5. 请用随机函数产生500行1-100之间的随机整数存入文件random.txt中，
编程寻找这些整数的众数并输出，众数即为一组数中出现最多的数。
'''

def q5():
    with open('random.txt', 'w+') as f:
        for i in range(500):
            f.write(str(random.randint(1,100)))
            f.write('\n')
        f.seek(0)
        nums = f.readlines() 
    nums = [int(i[:-1]) for i in nums]
    '''
    方法一：
    map = {}
    maxi = 0
    for i in nums  :
        if i in map:
            map[i] += 1
        else:
            map[i] = 1
        maxi = max(maxi, map[i])
        print(maxi)
    '''
    #方法二：
    maxi = 0
    maxi_num = None
    numSet = set(nums)
    for num in numSet:
        temp_maxi = max(nums.count(num), maxi)
        print(num, ":", nums.count(num))
        if maxi != temp_maxi:
            maxi = temp_maxi
            maxi_num = num
    print(maxi_num, " occurs ", maxi, "times")
    return maxi

'''
6. 文件article.txt中存放了一篇英文文章（请自行创建并添加测试文本），
假设文章中的标点符号仅包括“,”、“.”、“!”、“?”和“…”，编程找出其中最长的单词并输出。 
'''
def q6(fileName):
    with open(fileName,'r') as f:
        lst = f.read()
    lst = lst.replace(',', ' ')
    lst = lst.replace('.', ' ')
    lst = lst.replace('!', ' ')
    lst = lst.replace('?', ' ')
    lst = lst.replace('...', ' ')
    lst = lst.split(' ')
    length = [len(i) for i in lst]
    ind = length.index(max(length))
    print(lst[ind])

'''
7. 请完成以下文件综合编程迷你项目（提示：可以利用list的insert函数）。 

(1) 创建一个文件Blowing in the wind.txt，其内容是： 

(2) 在文件头部插入歌名“Blowin’ in the wind” 

(3) 在歌名后插入歌手名“Bob Dylan” 

(4) 在文件末尾加上字符串“1962 by Warner Bros. Inc.” 

(5) 在屏幕上打印文件内容 

'''
def createFile():
    with open('BlowingInTheWind.txt', 'w') as f:
        f.write("How many roads must a man walk down \n\nBefore they call him a man \n\nHow many seas must a white dove sail \n\nBefore she sleeps in the sand \n\nHow many times must the cannon balls fly \n\nBefore they're forever banned \n\nThe answer my friend is blowing in the wind \n\nThe answer is blowing in the wind ")
def insert_line(lines):
    lines.insert(0, "Blowin' in the wind\n")
    lines.insert(1, "Bob Dylan\n")
    lines.append("1962 by Warner Bros. Inc.")
    return ''.join(lines)
def q7():
    with open('BlowingInTheWind.txt', 'r+') as f:
        lines = f.readlines()
        string = insert_line(lines)
        print(string)
        f.seek(0)
        f.write(string)


if __name__ == '__main__':
    #q1
    q1()
    
    
    #q2
    
    s = input("please give me a string:")
    f = True
    while f:
        try:
            flag = int(input("right shift(1) or left shit(2), please type 1 or 2: "))
            if flag in [1,2]:
                f = False
        except ValueError:
            print("invalid input")
    f = True
    while f:
        try:
            n = int(input("how many bits you want to shif? Please give an integer "))
            f = False
        except ValueError:
            print("invalid input")
    result = move_substr(s,flag, n)
    if result == -1:
        print('the n is too large')
    else:
        print(result)
     
     
    #q3
    result = countchar("Hope is a good thing.".lower())
    print(result)
    
    #q4
    q4(int(input("number 1~9:")))
    
    #q5
    q5()
    
    #q6
    q6('article.txt')
    
    createFile()
    q7()