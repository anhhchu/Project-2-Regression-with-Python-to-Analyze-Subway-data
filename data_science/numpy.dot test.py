# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 17:42:08 2015

@author: jasmin may
"""
import numpy as np
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
#print np.dot(b, a)

c = np.arange(3*4*5*6).reshape((3,4,5,6))
d = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))
print c
#print d
#print np.dot(c, d)[2,3,2,1,2,2]
#499128
#>>> sum(a[2,3,2,:] * b[1,2,:,2])
#499128