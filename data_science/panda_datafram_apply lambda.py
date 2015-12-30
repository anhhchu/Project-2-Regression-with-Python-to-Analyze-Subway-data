# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:19:26 2015

@author: jasmin may
"""
import pandas as pd
import numpy

gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0] #=> list
silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

data = {'gold' : pd.Series(gold),'silver' : pd.Series(silver),'bronze' : pd.Series(bronze)}
df = pd.DataFrame(data) 
#print df
#print df.apply(numpy.mean) 
#print df['gold'].apply(numpy.mean) #=> doesn't return result 
#if use df['gold'] because apply is used for data frame, not each column series
#if use df[['gold']] return result -> df['gold'] is column series, df[['gold']] is dataframe

'''print numpy.mean(df['gold']) #=df[['gold']].apply(numpy.mean)
print df['gold'].map(lambda x: x>0) #return boolean value for the series
print df.applymap(lambda x: x>2) #return boolean value for the whole data frames'''

nums = range(2, 50) 
for i in range(2, 8): 
    nums = filter(lambda x: x == i or x % i, nums)
print nums