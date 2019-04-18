# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 21:56:35 2019

@author: wozui
"""

print("\n".join(" ".join(["%d*%d=%-2d"%(i,j,i*j) for i in range(1,j+1)]) for j in range(1,10)))