#A ver quien leia estos chingaderas

import pandas as pd
import numpy as np 
from pydataset import data
from env import host, user, password

#2 is gonna want these two little DFs
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})

#3 is gonna ask for the employees database, so I'll hardcode that here.
db = 'employees'

def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
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
pd.merge( 
    users.rename(columns={'id': 'user_id', 'name': 'username'}), 
    roles.rename(columns={'name': 'role_name'}), 
    left_on='role_id', right_on='id', how='left') 

# What do you think a right join would look like? 
#If there is a role that has no users, then there's gonna be row with NaNs on the left
#Cuz all of the right is getting displayed
pd.merge( 
    users.rename(columns={'id': 'user_id', 'name': 'username'}), 
    roles.rename(columns={'name': 'role_name'}), 
    left_on='role_id', right_on='id', how='right') 

# An outer join? 
#There will be NaN
pd.merge( 
    users.rename(columns={'id': 'user_id', 'name': 'username'}), 
    roles.rename(columns={'name': 'role_name'}), 
    left_on='role_id', right_on='id', how='right')

# What happens if you drop the foreign keys from the dataframes and try to merge them?
#This gets rid of the role_id in users. 
no_user_id = users.drop(columns=['role_id'])
#merge them with roles
pd.merge(no_user_id, roles, left_on='id', right_on='id', how='outer')
#Pandas is confused and is assiging the wrong role to adam.
#Or I don't know how to let Pandas take a guess at merging these two without explicitly
#naming the join_on rules

###########################################
#                       Getting data from SQL data 
# 3
# Create a function named get_db_url. It should accept a username, hostname, password, and 
# database name and return a url formatted like in the examples in this lesson.
print("The function is defined at the top of this script. ")

# 3
# Use your function to obtain a connection to the employees database.
url = get_db_url(user, host, password, db)
emps_df = pd.read_sql('SELECT * FROM employees', url)

# 3
# Once you have successfully run a query:
# Intentionally make a typo in the database url. What kind of error message do you see?
bad_url = "8.8.8.8"
url = get_db_url(user, bad_url, password, db)
emps_df = pd.read_sql('SELECT * FROM employees', url)
#   "Can't connect to MySQL server on '8.8.8.8' (timed out)")

# 3
# Intentionally make an error in your SQL query. What does the error message look like?
url = get_db_url(user, host, password, db)
emps_df = pd.read_sql('SELECT zebras FROM employees', url)
#(pymysql.err.InternalError) (1054, "Unknown column 'zebras' in 'field list'")

# 3
# Read the employees and titles tables into two separate dataframes
titles_df = pd.read_sql('SELECT * FROM titles', url)

###############
# 3
# Visualize the number of employees with each title.

#this is the count of unique emp_no's with each group found in the title column
emp_titles_count = titles_df.groupby('title').emp_no.count()
#Managers are so few that I ought to change the Y axis so it can not look like a zero count.
emp_titles_count.plot.bar()

# 3
# Join the employees and titles dataframes together.
emps_and_titles = pd.merge(emps_df, titles_df, left_on='emp_no', right_on='emp_no', how='inner')

# 3
# Visualize how frequently employees change titles.

#This is the count of current employees. So this minus the total is the records of 
#former employee positions that are also in this value down here.
emps_and_titles.groupby('to_date').emp_no.count().tail(1)

#Minused the to_date from the from_date. Pandas turned them into datetime objects
#so the answer is in days. Gonna skim out the onces that equal -2922337.
title_duration = emps_and_titles['from_date'] - emps_and_titles['to_date']  
#title_duration is a Series and each element is a datetime.timedelta
#I'm gonna ask about each ones .days atrribute
title_duration[0].days
#list comp of all the values that arenet around 29000
z = [i.days for i in title_duration if i.days > -2900000]
z = np.asarray(z)
z.mean()
#This was more roundabout then I hoped. That datetime part threw a wrench in my pandas chi.


# 3
# For each title, find the hire date of the employee that was hired most recently with that 
# title.

#Grouped the title column and showed the max hire_date for each group.
emps_and_titles.groupby('title').hire_date.agg('max')


# 3
# Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL and python/pandas code)
#merged the dept_emp table onto my alrady merged dataframe
big_df = pd.merge(emps_and_titles, dept_emp_df, left_on='emp_no', right_on='emp_no', how='inner')

#crosstab the deptno with the count of titles for each deptno
pd.crosstab(big_df.dept_no, big_df.title, margins=True)

###########################################
# 4
# Use your get_db_url function to help you explore the data from the chipotle database. 

#I used the read table method to just grab the only table in the chipotle db
chipotle = pd.read_sql_table('orders', url)

# Use the data to answer the following questions:

# What is the total price for each order?
chipotle['item_price'] = chipotle['item_price'].apply(remove_commas_and_dollarsign)
chipotle['item_price'] = chipotle['item_price'].apply(float)
chipotle['quantity'] * chipotle['item_price']

# What are the most popular 3 items?
# Which item has produced the most revenue?