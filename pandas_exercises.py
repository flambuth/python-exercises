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
# 



#Don't forget to change your db. 
df = pd.read_sql('SELECT * FROM employees , url)
print(df)