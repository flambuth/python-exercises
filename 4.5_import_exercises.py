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
#the memory efficient thing to do would be to use itertools.chain(list(letters), numbers)
#then make a list of the combinations from that chain object.
combos = list(combinations(list(letters) + numbers, 2))

#gets rid of double letters or double numbers
x = [i for i in combos if type(i[0]) != type(i[1])] 

double_letter_combo = list(combinations(letters, 2))

##The JSON stuff
import json

#the default paramater for the mode is r. The r here is redundant
with open("profiles.json", "r") as read_file:
    data = json.load(read_file)

#find Total number of users
def find_total_users(data):
    total_users = len(i for i in data)
    return total_users

# Number of active users
def find_active_users(data):
    active_users = len([i for i in data if i["isActive"] == True])
    return active_users

# Number of inactive users
def find_inactive_users(data):
    active_users = len([i for i in data if i["isActive"] == False])
    return active_users

# Grand total of balances for all users

#This strips off the commas betweeen 3 digits and gets rid of the $
#Then i can add the floats
def convert_dollar_to_float(dollars):
    s = ''
    new_dollars = [i for i in dollars if i!= ',']
    s = s.join(new_dollars[1:])
    return float(s)

#How the instructor gets rid of $ and ,
def handle_balance(s):
    float(s[1:].replace(',', ''))

def find_sum_of_balances(data):
    x = [i['balance'] for i in data]
    sum_of_balances = sum(list(map(convert_dollar_to_float, x)))
    return sum_of_balances

# Average balance per user
def find_avg_of_balances(data):
    x = [i['balance'] for i in data]
    avg_of_balances = sum(list(map(convert_dollar_to_float, x)))/len(x)
    return avg_of_balances

# User with the lowest balance
#This returns the balance. Which is the min values of a list comprehension that pulled
#from the balance field of each list member of data
def user_with_lowest(data):
    x = [i['balance'] for i in data]
    lowest_balance = min(list(map(convert_dollar_to_float, x)))
    return lowest_balance

def user_with_highest(data):
    x = [i['balance'] for i in data]
    highest_balance = max(list(map(convert_dollar_to_float, x)))
    return highest_balance

#list comprehension that filters out everythign except the lowest balance found in the earlier
#funciton
low_balance_user = [(i['name'],i['balance']) for i in data if convert_dollar_to_float(i['balance']) == user_with_lowest(data)] 

#I pulled this from stack overflow when I was trying to sort by the second element
# of a tuple within a lit of tuples

#sorts that list ot tuples madde in 
def Sort_Tuple(tup):  
      # getting length of list of tuples 
    lst = len(tup)  
    for i in range(0, lst):  
          
        for j in range(0, lst-i-1):  
            if (tup[j][1] > tup[j + 1][1]):  
                temp = tup[j]  
                tup[j]= tup[j + 1]  
                tup[j + 1]= temp  
    return tup

Sort_Tuple(names_with_balances[0])

# User with the highest balance
Sort_Tuple(names_with_balances[-1])
high_balance_user = [(i['name'],i['balance']) for i in data if convert_dollar_to_float(i['balance']) == user_with_highest(data)] 


# Most common favorite fruit
#crude iteration of each value of the favFruit key in each list member of data var
from collections import Counter

fav_fruits = Counter([i['favoriteFruit'] for i in data])
fruit_count = dict(fav_fruits)
fruit_winner = max(fruit_count.items())

# Least most common favorite fruit
fruit_loser = min(fruit_count.items())

#the super elegant way the instructor showed
#Counter(i['favoriteFruit'] for i in data)
#^I did that. How'd i forget? either wway its in line 122. i couldve put 122 and 123 together

# Total number of unread messages for all users
def extract_digits(s): 
    return "".join([c for c in s if c.isdigit()]) 

user_messages = [int(extract_digits(i['greeting'])) for i in data]
sum(user_messages)