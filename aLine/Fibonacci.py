# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:37:50 2019

@author: wozui
"""

print zip(*[(a[i][0],a.append([a[i][1],a[i][0]+a[i][1]])) for a in [[[1,1]],] for i in xrange(10)])[0]
#参考https://blog.csdn.net/python233/article/details/70491587