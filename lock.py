#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import threading
import time

num = 0
mutex = threading.Lock()

class MyThread(threading.Thread):
    
    def run(self):
        mutex.acquire()
        global num
        num += 1
        time.sleep(0.5)
        print('\n' + self.name + 'set num to' + str(num))
        mutex.release()
        

def test():
    for i in range(5):
        
        t = MyThread()
        t.start()

if __name__ == '__main__' :
    test()
