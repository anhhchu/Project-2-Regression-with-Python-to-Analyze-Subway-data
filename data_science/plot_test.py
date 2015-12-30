# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 22:17:12 2015

@author: jasmin may
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

'''a = range(0,10)
b = range(0,20,2)
c = range(0,30,3)
d = range(0,40,4)

plot1 = plt.figure()

plt.plot(a,b, 'r-o')

plt.show()

plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
plt.close()'''


'''plt.plot([1,2,3,4], [1,4,9,16], 'ro') #ro: show data in red circles
plt.axis([0, 6, 0, 20]) #show min, max value of x and y
plt.show()
plt.close()'''

# evenly sampled time at 200ms intervals
'''t = np.arange(0., 5., 0.2)
series = {'number':pd.Series(t),'number*2':pd.Series(t*t),'number*3':pd.Series(t*t*t)} #Series turns t from a list in row to column with index number and column title
#print series
df = pd.DataFrame(series)
print df'''


# red dashes, blue squares and green triangles
'''plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.axis([0,6,0,120])
plt.show()'''

#set property - setp () function for line 
'''x = np.arange(0,1.0,0.01)
y = np.arange(0,1.0,0.01)
lines = plt.plot(x, y)
plt.setp(lines, linewidth=5, color='r')'''

x = np.arange(0, 5, 0.1)
y = np.sin(x)
print pd.Series(y)
plt.plot(x, y)