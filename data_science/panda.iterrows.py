# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 09:53:47 2015

@author: jasmin may
"""

import pandas as pd
x=pd.Series([1,2,3,4])
y=pd.Series([5.0,6.0,7.0,1.0])
df = pd.DataFrame({x,y}, columns=['x', 'y'])
print df
'''row = next(df.iterrows())[2]
print(row['x'].dtype)

print(df['x'].dtype)'''
