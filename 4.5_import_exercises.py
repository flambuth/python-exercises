# 1
# Import and test 3 of the functions from your functions exercise file.

# Your functions exercise are not currently in a file with a name that can be easily imported. Copy your functions exercise file and name the copy functions_exercises.py.

# Import each function in a different way:

# import the module and refer to the function with the . syntax
# use from to import the function directly
# use from and give the function a different name

import functions_exercise

import functions_exercise as fe

from functions_exercise import cumsum

from itertools import combinations

numbers = [1,2,3]
letters = 'abc'

#makes a list of every 2 character combo from abc and 123.
combos = list(combinations(list(letters) + numbers, 2))

#gets rid of double letters or double numbers
x = [i for i in combos if type(i[0]) != type(i[1])] 

double_letter_combo = list(combinations(letters, 2))

##The JSON stuff
import json

with open("profiles.json", "r") as read_file:
    data = json.load(read_file)

#find Total number of users
def find_total_users(data):
    total_users = len(i for i in data)
    return total_users

# Number of active users


# Number of inactive users
# Grand total of balances for all users
# Average balance per user
# User with the lowest balance
# User with the highest balance
# Most common favorite fruit
# Least most common favorite fruit
# Total number of unread messages for all users