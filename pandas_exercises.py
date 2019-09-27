#A ver quien leia estos chingaderas

import pandas as pd
import numpy as np 
from pydataset import data
from env import host, user, password

#3 is gonna ask for the employees database, so I'll hardcode that here.
db = 'employees'

def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return url
######################
#####the main script!

mpg = data('mpg')

# 1
# On average, which manufacturer has the best miles per gallon?

# This groups the manufacturers by their hwy mileage.
mpg.groupby('manufacturer').hwy.agg(['min', 'mean', 'max'])
# I'm gonna have to make a new column that is the average of city and highway mileage.
mpg['mileage'] = (mpg['cty'] + mpg['hwy']) / 2
#Let's group the on this new column
mpg.groupby('manufacturer').mileage.agg(['min', 'mean', 'max'])
#Now sort them and see who's at the bottom
mpg.groupby('manufacturer').mileage.agg(['min', 'mean', 'max']).sort_values(by='mean').tail(1)
#Looks like Honda is the winner


#######
# 1
# How many different manufacturers are there?

#This groups them by model so that only one column is displayed.
#The count for each group is the same for each column. mpg.groupby('manufacturer').count()
#would show all the columns, where I saw they all had the same count values.
mpg.groupby('manufacturer').model.count()


##########
# 1
# How many different models are there?

# I went with hwy as the field to measure because it was only 3 characters of typing.
mpg.groupby('model').hwy.count()


##########
# 1
# Do automatic or manual cars have better miles per gallon?

#gonna group up the manual cars over on to the rows section. See there values in the mileage
#column
x= mpg.groupby('trans').mileage.agg(['min','mean','max'])

#Apparently there are more than one type of automatic and manual transmissions.
#Gonna try to glob them into two groups. Auto and Manual

#this is just the automatics, sliced by their explicit index.
auto_trans = x.loc[:"auto(s6)"]
#This is the manuals, slicing the other way
man_trans = x.loc["manual(m5)":]

#the mileage average for all transmission types
x['mean'].agg('mean')
#mileage for the autos
auto_trans['mean'].agg('mean')
#mileage for the manuals
man_trans['mean'].agg('mean')

#Lets put out a nice string 
print(f"Automatics get {auto_trans['mean'].agg('mean')} mpg and manuals get {man_trans['mean'].agg('mean')} mpg.")
print(f"{abs(auto_trans['mean'].agg('mean') - man_trans['mean'].agg('mean'))} does not seem statistically significant. I'd go with the convenience of the auto.")



###########################################
#                       Joining and Merging
# 2
# Copy the users and roles dataframes from the examples above. 
# What do you think a right join would look like? 
# An outer join? 
# What happens if you drop the foreign keys from the dataframes and try to merge them?


###########################################
#                       Getting data from SQL data 
# 3
# Create a function named get_db_url. It should accept a username, hostname, password, and 
# database name and return a url formatted like in the examples in this lesson.

# Use your function to obtain a connection to the employees database.
# Once you have successfully run a query:
#   Intentionally make a typo in the database url. What kind of error message do you see?

#   Intentionally make an error in your SQL query. What does the error message look like?

# Read the employees and titles tables into two separate dataframes

# Visualize the number of employees with each title.

# Join the employees and titles dataframes together.

# Visualize how frequently employees change titles.

# For each title, find the hire date of the employee that was hired most recently with that 
# title.

# Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL and python/pandas code)


#Don't forget to change your db. 
df = pd.read_sql('SELECT * FROM employees , url)
print(df)