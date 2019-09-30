import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

#what is pylint? did'nt I alraedy have that?
#I messwed with that 'base':conda when I was working with the flask stuff over the weekend


# Use the iris database to answer the following quesitons:

iris = sns.load_dataset('iris')


# What does the distribution of petal lengths look like?
sns.boxplot(data=iris, y = 'petal_length')
sns.distplot(tips.total_bill)

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