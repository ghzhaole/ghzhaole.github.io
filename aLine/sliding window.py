# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 21:50:06 2019

@author: wozui
"""


i, j = 3, 3


s = 'abcdefghijklmnopqrstuvwxyz'
sw = zip(*(s[ii::j] for ii in range(i)))
print(sw)

#[('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'), ('j', 'k', 'l'), ('m', 'n', 'o'), ('p', 'q', 'r'), ('s', 't', 'u'), ('v', 'w', 'x')]