#numpy is fast, from what they tell me

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1
# How many negative numbers are there?
is_negative_mask = a < 0
a[is_negative_mask]

# 2
# How many positive numbers are there?
is_positive_mask = a > 0 
a[is_positive_mask]

# 3
# How many even positive numbers are there?
a[is_even_mask & is_positive_mask]

# 4
# If you were to add 3 to each data point, how many positive numbers would there be?
b = a+3
b[b>0]

# 5
# If you squared each number, what would the new mean and standard deviation be?
c = a**2
c.mean()
c.std()

# 6
# A common statistical operation on a dataset is centering. This means to adjust the 
# data such that the center of the data is at 0. This is done by subtracting the mean 
# from each data point. Center the data set.
# subtracting the mean from each data point
a - a.mean()

# 7
# Calculate the z-score for each data point. Recall that the z-score is given by:
a-a.mean()/a.std() 