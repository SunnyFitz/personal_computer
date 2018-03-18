#!/usr/bin/env python
# -*-  coding:utf-8 -*-

import requests
import re
import time

title2 = ' '



def get():

    global title2
    url = 'http://top.baidu.com/buzz?b=1'
    try:

        response = requests.get(url)

        response.encoding = 'gb2312'

        data = response.text


        title = re.findall(r'{\'text\':\'(.*?) ',data)
        print(title)

        if title2 != title:
            title2 = title
            f = open('C:\\Users\\gaore\\Desktop\\python\\hot_point.txt','a',encoding = 'utf-8')
            f.write(time.asctime( time.localtime(time.time()) ))
            f.write('   ')
            f.write(title[0])
            f.write('\n')

    except:
        get()


if __name__ == "__main__" :
    while 1:
        get()
        time.sleep(10)

