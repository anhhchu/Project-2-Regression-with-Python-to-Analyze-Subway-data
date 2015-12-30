# -*- coding: utf-8 -*-
"""
Created on Sun Sep 06 11:21:40 2015

@author: jasmin may
"""

import numpy as np
import statsmodels.api as sm

Y = [1,3,4,5,2,3,4]
X = range(1,8)
X = sm.add_constant(X)

model = sm.OLS(Y,X)
results = model.fit()
print results 
print results.params[0]
#array([ 2.14285714,  0.25      ])
print results.tvalues
#array([ 1.87867287,  0.98019606])
print results.t_test([1, 0])
#T test: effect=array([ 2.14285714]), sd=array([[ 1.14062282]]), t=array([[ 1.87867287]]), p=array([[ 0.05953974]]), df_denom=5>
print results.f_test(np.identity(2))
#F test: F=array([[ 19.46078431]]), p=[[ 0.00437251]], df_denom=5, df_num=2>



def linear_regression(features, values):
    """
    Performs linear regression given a dataset with an arbitrary number of features.
    'features' is the input data points (or the X's) and 'values' is the output data points
    (or the Y's).
    
    Returns the intercept and the parameters, that is, the optimal values of theta.
    
    This page contains example code that may be helpful:
    http://statsmodels.sourceforge.net/0.5.0/generated/statsmodels.regression.linear_model.OLS.html
    """

    features = sm.add_constant(features)
    model = sm.OLS(values, features)
    results = model.fit()
    intercept = results.params[0]
    params = results.params[1:]
    return intercept, params
    
Yo'''ur intercept: 199.07125028
Your parameters: [-4.44124847  0.91818241]

This means homeruns will be predicted using the equation
homeruns = -4.44 * height + 0.92 * weight + 199.07'''

'''Note that add_constant adds the constant feature as the first feature, so the intercept is at index 0 of the array results.params. 
The remaining values of results.params, from index 1 to the end, are the parameters, or weights, of the real features.

Also note that values comes before features when creating the OLS model, just as Y came before X in the example code.'''