# -*- coding: utf-8 -*-
"""
Created on Tue Sep 08 12:26:57 2015

@author: jasmin may
"""

#problem set 3: 1 - Exploratory Data Analysis
import numpy as np
import pandas
import matplotlib.pyplot as plt

def entries_histogram(turnstile_weather):
    '''
    Before we perform any analysis, it might be useful to take a
    look at the data we're hoping to analyze. More specifically, let's 
    examine the hourly entries in our NYC subway data and determine what
    distribution the data follows. This data is stored in a dataframe
    called turnstile_weather under the ['ENTRIESn_hourly'] column.
    
    Let's plot two histograms on the same axes to show hourly
    entries when raining vs. when not raining. Here's an example on how
    to plot histograms with pandas and matplotlib:
    turnstile_weather['column_to_graph'].hist()
    
    Your histogram may look similar to bar graph in the instructor notes below.
    
    You can read a bit about using matplotlib and pandas to plot histograms here:
    http://pandas.pydata.org/pandas-docs/stable/visualization.html#histograms
    
    You can see the information contained within the turnstile weather data here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    plt.figure()
    turnstile_weather_rain = turnstile_weather[turnstile_weather.rain == 1]
    turnstile_weather_notrain = turnstile_weather[turnstile_weather.rain == 0]
    #print turnstile_weather_notrain
    turnstile_weather_notrain['ENTRIESn_hourly'].hist(alpha=0.5,label='no rain',bins=20, range = (0,4500)) # your code here to plot a historgram for hourly entries when it is not raining
    turnstile_weather_rain['ENTRIESn_hourly'].hist(label='rain',bins = 20, range=(0,4500)) # your code here to plot a historgram for hourly entries when it is raining    
    plt.legend(loc='upper right')
    plt.xlabel('Entries per hour')
    plt.ylabel('Frequency')
    return plt


#problem set 3: 3 - Mann-Whitney U-Test
import numpy as np
import scipy
import scipy.stats
import pandas

def mann_whitney_plus_means(turnstile_weather):
    '''
    This function will consume the turnstile_weather dataframe containing
    our final turnstile weather data. 
    
    You will want to take the means and run the Mann Whitney U-test on the 
    ENTRIESn_hourly column in the turnstile_weather dataframe.
    
    This function should return:
        1) the mean of entries with rain
        2) the mean of entries without rain
        3) the Mann-Whitney U-statistic and p-value comparing the number of entries
           with rain and the number of entries without rain
    
    You should feel free to use scipy's Mann-Whitney implementation, and you 
    might also find it useful to use numpy's mean function.
    
    Here are the functions' documentation:
    http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.mannwhitneyu.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    
    You can look at the final turnstile weather data at the link below:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
    '''
    
    with_rain = turnstile_weather[turnstile_weather.rain == 1]
    without_rain = turnstile_weather[turnstile_weather.rain == 0]
    with_rain_mean = np.mean(with_rain['ENTRIESn_hourly'])
    without_rain_mean = np.mean(without_rain['ENTRIESn_hourly'])
    U_and_p=scipy.stats.mannwhitneyu(with_rain['ENTRIESn_hourly'],without_rain['ENTRIESn_hourly'])
    U = U_and_p[0]
    p = U_and_p[1]
    #print with_rain_mean,without_rain_mean
    return with_rain_mean, without_rain_mean, U, p # leave this line for the grader
'''(1105.4463767458733, 1090.278780151855, 1924409167.0, 0.024999912793489721)'''


#problem set 3: 5 - Linear Regression
"""
In this question, you need to:
1) implement the linear_regression() procedure
2) Select features (in the predictions procedure) and make predictions.

"""
import statsmodels.api as sm
    
def linear_regression(features, values):
    """
    Perform linear regression given a data set with an arbitrary number of features.
    
    This can be the same code as in the lesson #3 exercise.
    """
    features = sm.add_constant(features)
    model = sm.OLS(values,features)
    result = model.fit()
    print result.summary() #return the descriptive statistic summary
    intercept = result.params[0]
    params = result.params[1:]
    return intercept, params

def predictions(dataframe):
    '''
    The NYC turnstile data is stored in a pandas dataframe called weather_turnstile.
    Using the information stored in the dataframe, let's predict the ridership of
    the NYC subway using linear regression with gradient descent.
    
    You can download the complete turnstile weather dataframe here:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv    
    
    Your prediction should have a R^2 value of 0.40 or better.
    You need to experiment using various input features contained in the dataframe. 
    We recommend that you don't use the EXITSn_hourly feature as an input to the 
    linear model because we cannot use it as a predictor: we cannot use exits 
    counts as a way to predict entry counts. 
    
    Note: Due to the memory and CPU limitation of our Amazon EC2 instance, we will
    give you a random subet (~10%) of the data contained in 
    turnstile_data_master_with_weather.csv. You are encouraged to experiment with 
    this exercise on your own computer, locally. If you do, you may want to complete Exercise
    8 using gradient descent, or limit your number of features to 10 or so, since ordinary
    least squares can be very slow for a large number of features.
    
    If you receive a "server has encountered an error" message, that means you are 
    hitting the 30-second limit that's placed on running your program. Try using a
    smaller number of features.
    '''
    ################################ MODIFY THIS SECTION #####################################
    # Select features. You should modify this section to try different features!             #
    # We've selected rain, precipi, Hour, meantempi, and UNIT (as a dummy) to start you off. #
    # See this page for more info about dummy variables:                                     #
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.get_dummies.html          #
    ##########################################################################################
    features = dataframe[['fog','meantempi','rain']]
    dummy_units = pandas.get_dummies(dataframe['UNIT'], prefix='unit')
    dummy_hours = pandas.get_dummies(dataframe['Hour'], prefix='hours')
    features = features.join(dummy_units)
    features = features.join(dummy_hours)
    
    # Values
    values = dataframe['ENTRIESn_hourly']

    # Perform linear regression
    intercept, params = linear_regression(features, values)
    
    predictions = intercept + np.dot(features, params)
    return predictions

'''                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const       2122.8193    142.443     14.903      0.000      1843.610  2402.028
fog          179.7374     44.192      4.067      0.000        93.115   266.360
meantempi    -12.7933      2.252     -5.681      0.000       -17.207    -8.379
rain          -8.6837     35.025     -0.248      0.804       -77.338    59.971
r square = 0.522'''
'''                  coef    std err          t      P>|t|      [95.0% Conf. Int.]
--------------------------------------------------------------------------------
const         1771.5186    170.029     10.419      0.000      1438.237  2104.800
fog            190.3090     44.257      4.300      0.000       103.558   277.060
meantempi       -9.6792      2.397     -4.038      0.000       -14.377    -4.981
rain           -14.4979     35.041     -0.414      0.679       -83.183    54.187
meanwindspdi    29.9611      7.928      3.779      0.000        14.421    45.501
r square = 0.5225'''
'''                    coef    std err          t      P>|t|      [95.0% Conf. Int.]
---------------------------------------------------------------------------------
const          7592.3522   3391.324      2.239      0.025       944.846  1.42e+04
fog             164.4419     45.194      3.639      0.000        75.856   253.028
meantempi       -12.9694      2.254     -5.753      0.000       -17.388    -8.550
rain            -16.8291     35.384     -0.476      0.634       -86.188    52.530
meanpressurei  -189.9573    117.677     -1.614      0.107      -420.622    40.707
r square = 0.5221'''
'''                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
---------------------------------------------------------------------------------
const          7345.6797   3351.328      2.192      0.028       776.572  1.39e+04
fog             155.6155     41.206      3.777      0.000        74.845   236.386
meantempi       -12.7511      2.207     -5.777      0.000       -17.077    -8.425
meanpressurei  -181.9760    116.471     -1.562      0.118      -410.276    46.324
r square = 0.522'''
'''                   coef    std err          t      P>|t|      [95.0% Conf. Int.]
--------------------------------------------------------------------------------
const         1758.4075    167.044     10.527      0.000      1430.976  2085.839
fog            181.9476     39.373      4.621      0.000       104.771   259.124
meantempi       -9.5090      2.361     -4.027      0.000       -14.137    -4.881
meanwindspdi    29.8171      7.920      3.765      0.000        14.293    45.342
r square =  0.522567058516
                   coef    std err          t      P>|t|      [95.0% Conf. Int.]
--------------------------------------------------------------------------------
const         1786.2029    167.860     10.641      0.000      1457.172  2115.234
fog            221.8835     46.067      4.817      0.000       131.585   312.182
meantempi      -10.1623      2.393     -4.246      0.000       -14.853    -5.471
meanwindspdi    32.8135      8.120      4.041      0.000        16.896    48.730
precipi        -70.1744     42.032     -1.670      0.095      -152.563    12.215
r^2 value is 0.522671797413'''

                coef    std err          t      P>|t|      [95.0% Conf. Int.]
--------------------------------------------------------------------------------
const         1758.4075    167.044     10.527      0.000      1430.976  2085.839
fog            181.9476     39.373      4.621      0.000       104.771   259.124
meantempi       -9.5090      2.361     -4.027      0.000       -14.137    -4.881
meanwindspdi    29.8171      7.920      3.765      0.000        14.293    45.342
#problem set 3: 6 - Plotting Residuals
import matplotlib.pyplot as plt

def plot_residuals(turnstile_weather, predictions):
    '''
    Using the same methods that we used to plot a histogram of entries
    per hour for our data, why don't you make a histogram of the residuals
    (that is, the difference between the original hourly entry data and the predicted values).
    Try different binwidths for your histogram.

    Based on this residual histogram, do you have any insight into how our model
    performed?  Reading a bit on this webpage might be useful:

    http://www.itl.nist.gov/div898/handbook/pri/section2/pri24.htm
    '''
    
    plt.figure()
    (turnstile_weather['ENTRIESn_hourly'] - predictions).hist(bins = 30, range=(-5000,5000),label ='residuals')
    return plt
 
#problem set 3: 7 - Compute R^2  
def compute_r_squared(data, predictions):
    '''
    In exercise 5, we calculated the R^2 value for you. But why don't you try and
    and calculate the R^2 value yourself.
    
    Given a list of original data points, and also a list of predicted data points,
    write a function that will compute and return the coefficient of determination (R^2)
    for this data.  numpy.mean() and numpy.sum() might both be useful here, but
    not necessary.

    Documentation about numpy.mean() and numpy.sum() below:
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html
    http://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html
    '''
    
    nominator = np.sum((data-predictions)**2)
    denominator = np.sum((data-np.mean(data))**2)
    r_squared = 1 - nominator/denominator
    return r_squared
    
'''Your calculated R^2 value is: 0.47924770782'''