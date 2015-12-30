# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 23:22:47 2015

@author: jasmin may
"""

from pandas import *
from ggplot import *

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''
    print turnstile_weather
   
    pandas.options.mode.chained_assignment = None
 
    #Add the day of the week
    turnstile_weather['day_of_week'] = pandas.to_datetime(turnstile_weather['DATEn']).dt.dayofweek
    print turnstile_weather['day_of_week']
    # Is it a weekday?
    turnstile_weather["weekday"] = (turnstile_weather["day_of_week"] < 5).astype(float)
 
    hLength = len(turnstile_weather["Hour"])
 
    # The data points will be displaced according to the UNIT
    turnstile_weather['unit_number'] = (turnstile_weather['UNIT'].map(lambda x: x.lstrip('R'))).astype(float)
    turnstile_weather["hour_plot2"]  = turnstile_weather["Hour"] + (turnstile_weather['unit_number'])/700
 
 
    plot = ggplot(aes(x='hour_plot2', y='ENTRIESn_hourly', color='weekday'), data=turnstile_weather) + geom_point(alpha = 0.1, size = 20)
    plot = plot + xlim(-0.5, 24.5) + ylim(0, 20000) + scale_y_continuous(name="Hourly Entries")
    plot = plot + theme_bw() + scale_x_discrete(name="Hour", minor_breaks = list(range(0, 24, 1)), breaks = list(range(0, 24, 1)))
    plot = plot + labs(title = "Scatterplot of hourly entries per hour of the day in all turnstiles")
   
 
    return plot
    
# entries by hour
     
    plot = ggplot(turnstile_weather,aes(x='Hour',y='ENTRIESn_hourly'))+geom_point(color='blue')+ggtitle('Entries by hours')+xlab('Hour')+ylab('Entry') 
    plot=plot+xlim(0,24)+ylim(0,50000)
    return plot
    
# etries by day
    weekday = []
    for date in turnstile_weather['DATEn']:
        day=datetime.datetime.strptime(date,'%Y-%m-%d').strftime('%w')
        weekday.append(day)
    turnstile_weather['day_in_week'] = pandas.Series(weekday)
    #print turnstile_weather['day_in_week']
    
    plot = ggplot(turnstile_weather, aes(x='day_in_week', y='ENTRIESn_hourly'))+geom_point(color='blue')+ggtitle('Entries by days')+xlab('Day')+ylab('Entry')
    plot = plot+xlim(-1,7)+ylim(0,50000)
    return plot

