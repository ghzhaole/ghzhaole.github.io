# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 10:03:49 2019

@author: wozui
"""

qsort = lambda arr: len(arr) > 1 and qsort(list(filter(lambda x: x <= arr[0], arr[1:]))) + arr[0:1] + qsort(list(filter(lambda x: x > arr[0], arr[1:]))) or arr
#https://www.zhihu.com/question/37046157
#快速排序
                       
                       
msort=lambda arr:[(y[0].pop(0) if y[0][0]<x[0][0] else x[0].pop(0)) if (y[0] and x[0]) else (y[0].pop(0) if y[0] else (x[0].pop(0) if x[0] else None)) for x in [[esort(arr[len(arr)/2:])],] for y in [[esort(arr[:len(arr)/2])],]  for i in range(len(arr)) if (y[0] or x[0])]   if len(arr)>1 else arr                    
#归并排序，实现的并不好，可否改进