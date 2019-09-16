#When run, the application should welcome the user, and prompt them for 
# an action to take:
#   view current balance
#   add a debit (withdrawal)
#   add a credit (deposit)
#   exit

#gonna need to make persistent saves to disk
import os
import checkbook_functions

#Will save to a file per each user
known_users = [
{'name':'aone', 'balance':1000}    
]
user = input("Please enter your username: ")
check_user(user,known_users)


print(f"Welcome to your checkbook application, {user}!")

choice = 0

while choice != 4:
    print("1) View Current Balance")
    print("2) Make New Debit (withdraw)")
    print("3) Make New Credit (deposit)")
    print("4) Exit")

    choice = input("What would you like to do? ")
    if choice == '4':
        break
        # if choice == '4':
        # print("good bye")



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