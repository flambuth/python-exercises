import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns

#what is pylint? did'nt I alraedy have that?
#I messwed with that 'base':conda when I was working with the flask stuff over the weekend


# Use the iris database to answer the following quesitons:

iris = sns.load_dataset('iris')


# What does the distribution of petal lengths look like?



# Is there a correlation between petal length and petal width?
sns.relplot(x='petal_length', y='petal_width', data=iris)

# Would it be reasonable to predict species based on sepal width and sepal length?
sns.relplot(x='sepal_length', y='sepal_width', columns='species' ,data=iris)

# Which features would be best used to predict species?
