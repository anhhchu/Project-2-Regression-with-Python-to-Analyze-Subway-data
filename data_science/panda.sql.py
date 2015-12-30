# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 23:07:05 2015

@author: jasmin may
"""

import pandas
import pandasql

def select_first_50(filename):
    # Read in our aadhaar_data csv to a pandas dataframe.  Afterwards, we rename the columns
    # by replacing spaces with underscores and setting all characters to lowercase, so the
    # column names more closely resemble columns names one might find in a table.
    aadhaar_data = pandas.read_csv(filename)
    aadhaar_data.rename(columns = lambda x: x.replace(' ', '_').lower(), inplace=True)
    #print aadhaar_data

    # Select out the first 50 values for "registrar" and "enrolment_agency"
    # in the aadhaar_data table using SQL syntax. 
    #
    # Note that "enrolment_agency" is spelled with one l. Also, the order
    # of the select does matter. Make sure you select registrar then enrolment agency
    # in your query.
    #
    # You can download a copy of the aadhaar data that we are passing 
    # into this exercise below:
    # https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv
    
    q = """
    SELECT 
    registrar, enrolment_agency
    FROM
    aadhaar_data
    """

    #Execute your SQL command against the pandas frame
    aadhaar_solution = pandasql.sqldf(q.lower(), locals())
    return aadhaar_solution    
    
print select_first_50('D:\udacity-data analysis\Project 2\intro to data science\aadhaar_data.csv')

    # Write a query that will select from the aadhaar_data table how many men and how 
    # many women over the age of 50 have had aadhaar generated for them in each district.
    # aadhaar_generated is a column in the Aadhaar Data that denotes the number who have had
    # aadhaar generated in each row of the table.
    #
    # Note that in this quiz, the SQL query keywords are case sensitive. 
    # For example, if you want to do a sum make sure you type 'sum' rather than 'SUM'.
    q = '''SELECT 
    gender, district,sum(aadhaar_generated)
    FROM aadhaar_data  
    WHERE age>50
    GROUP BY gender, district
    '''

'''
    This function should run a SQL query on a dataframe of
    weather data.  The SQL query should return one column and
    one row - the average meantempi on days that are a Saturday
    or Sunday (i.e., the the average mean temperature on weekends).
    The dataframe will be titled 'weather_data' and you can access
    the date in the dataframe via the 'date' column.
    
    You'll need to provide  the SQL query.
    
    You might also find that interpreting numbers as integers or floats may not
    work initially.  In order to get around this issue, it may be useful to cast
    these numbers as integers.  This can be done by writing cast(column as integer).
    So for example, if we wanted to cast the maxtempi column as an integer, we would actually
    write something like where cast(maxtempi as integer) = 76, as opposed to simply 
    where maxtempi = 76.
    
    Also, you can convert dates to days of the week via the 'strftime' keyword in SQL.
    For example, cast (strftime('%w', date) as integer) will return 0 if the date
    is a Sunday or 6 if the date is a Saturday.
    
    You can see the weather data that we are passing in below:
    https://www.dropbox.com/s/7sf0yqc9ykpq3w8/weather_underground.csv'''
    
    q = """
    SELECT avg(meantempi)
    FROM weather_data 
    WHERE cast (strftime('%w', date) as integer) = 0 or cast (strftime('%w', date) as integer)=6
    """
    
    #Execute your SQL command against the pandas frame
    mean_temp_weekends = pandasql.sqldf(q.lower(), locals())
    return mean_temp_weekends