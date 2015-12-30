# -*- coding: utf-8 -*-
"""
Created on Wed Sep 02 16:40:43 2015

@author: jasmin may
"""

import pandas as pd
import matplotlib.pyplot as plt
xl = pd.ExcelFile(r"D:\udacity-data analysis\Intro to python programming\Obes-phys-acti-diet-eng-2014-tab.xls") #read the Excel file
#print xl.sheet_names
xl_age = xl.parse (u'7.2', skiprows=4, skipfooter = 14) #Get the data of interest and skip the unnecessary
#print xl_age 
xl_age.rename(columns = {u'Unnamed: 0':u'Year'},inplace = True) #Rename the column Unnamed    
xl_age.dropna(inplace=True) #drop the NaN row (Return object with labels on given axis omitted where alternately any or all of the data are missin)
xl_age.set_index('Year', inplace = True)
#print "After clean up data:"
#print xl_age
#xl_age.plot()
#plt.show()

#We want to get rid of Total line on the graph
xl_age_minus_total = xl_age.drop('Total',axis=1)
#xl_age_minus_total.plot()


#Compare parent and children on the graph
# Plot children vs adults
'''plt.close()
xl_age['Under 16'].plot(label="Under 16")
xl_age['35-44'].plot(label="35-44")
plt.legend(loc = "upper left")
plt.show()'''

kids_value = xl_age['Under 16'].values #get the value of column Under 16
x_axis = range(len(kids_value))


