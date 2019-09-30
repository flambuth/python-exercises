import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

from env import host, user, password

def get_db_url(username, hostname, password, database):
    url = f'mysql+pymysql://{username}:{password}@{hostname}/{database}'
    return url


def remove_commas_and_dollarsign(string_num):  
    """ 
    Cleans off a starting $ and commas where-ever they are. Takes a string, returns a string 
    """ 
    
    x = string_num.replace(',','')  
    x = x.strip("$")  
    return x  

#what is pylint? did'nt I alraedy have that?
#I messwed with that 'base':conda when I was working with the flask stuff over the weekend


# Use the iris database to answer the following quesitons:

iris = sns.load_dataset('iris')


# What does the distribution of petal lengths look like?
sns.boxplot(data=iris, y = 'petal_length')
sns.distplot(iris.petal_length)

# Is there a correlation between petal length and petal width?
sns.relplot(x='petal_length', y='petal_width', data=iris)

# Would it be reasonable to predict species based on sepal width and sepal length?
sns.relplot(x='sepal_length', y='sepal_width', columns='species' ,data=iris)

# Which features would be best used to predict species?
sns.relplot(x='petal_length', y='petal_width', col='species' ,
            hue='species', data=iris)
#The data is much more tightly clustered together when plotting the petal measurements.            


# 1
# Using the lesson as an example, use seaborn's load_dataset function to load the anscombe 
# data set. Use pandas to group the data by the dataset column, and calculate summary 
# statistics for each dataset. What do you notice?
anscombe = sns.load_dataset('anscombe')
anscombe.groupby('dataset').x.agg(['min','mean','max'])
anscombe.groupby('dataset').y.agg(['min','mean','max'])
#They have very similar summary statistics. Especially at the mean.
sns.relplot(x='x', y='y', col='dataset',hue='dataset', data=anscombe)


# Load the InsectSprays dataset and read it's documentation. Create a boxplot that 
# shows the effectiveness of the different insect sprays.

#I got the csv in my working directory
sprays = pd.read_csv('InsectSprays.csv')

sns.boxplot(data=sprays, y = 'count', x='spray')



# 2
# Load the swiss dataset and read it's documentation. Create visualizations to answer the 
# following questions:
swiss = pd.read_csv('swiss.csv')

# Create an attribute named is_catholic that holds a boolean value of whether or not 
# the province is Catholic. (Choose a cutoff point for what constitutes catholic)

# Does whether or not a province is Catholic influence fertility?
sns.boxplot(x='is_Catholic', y='Fertility', data=swiss)


# What measure correlates most strongly with fertility?
sns.relplot(x='Education', y='Fertility', data=swiss)

# 3
# Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 
# most popular items and the revenue produced by each.
db = chipotle
url = get_db_url(user, host, password, db)
chipotle = pd.read_sql_table('orders', url)

#converts the string price into a float price
chipotle['item_price'] = chipotle.item_price.apply(remove_commas_and_dollarsign)
#make a new column that multiplies the quantity with each order by the cost of each item
chipotle['total_order'] = chipotle.item_price * chipotle.quantity


#makes a series of each group of item_names and has their id count as the values
item_freq = chipotle.groupby('item_name').id.agg("count")
#sorts and skims off the top5 most frequently ordered items
top5 = item_freq.sort_values(ascending=False).head()

#makes a bar plot
sns.barplot(x=top5.index, y=top5.values)

# 4
# Load the sleepstudy data and read it's documentation. Use seaborn to create a line chart 
# of all the individual subject's reaction times and a more prominant line showing the 
# average change in reaction time.