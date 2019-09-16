#When run, the application should welcome the user, and prompt them for 
# an action to take:
#   view current balance
#   add a debit (withdrawal)
#   add a credit (deposit)
#   exit

#gonna need to make persistent saves to disk
import os

user = input("Please enter your username: ")

print(f"Welcome {user}!")




##########
# Once you have finished the basic application (in no particular order),

# add a menu item that allows the user to view all historical transactions
# assign categories to each transaction
# add a menu item to allow the user to view all the transactions in a given category
# provide the user with summary statistics about the transactions in each category
# keep track of the date and time that each transaction happened
# allow the user to view all the transactions for a given day
# make sure your list of previous transactions includes the timestamp for each
# allow the user to optionally provide a description for each transaction
# allow the user to search for keywords in the transaction descriptions, and show all the transactions that match the user's search term
# allow the user to modify past transactions