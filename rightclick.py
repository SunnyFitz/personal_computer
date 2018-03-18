#!/usr/bin/env python  
# -*- coding: utf-8 -*-  
  
  
import time

import win32api  
import win32con  
  
while 1:
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  
    time.sleep(0.05)  
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)  
  

  
      
      
