# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:41:26 2019

@author: wozui
"""

_=[__import__('sys').stdout.write("\n".join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n========\n") for vec in __import__('itertools').permutations(xrange(8)) if 8 == len(set(vec[i]+i for i in xrange(8))) == len(set(vec[i]-i for i in xrange(8)))]


#作者：est
#链接：https://www.zhihu.com/question/37046157/answer/70747261
#来源：知乎
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。