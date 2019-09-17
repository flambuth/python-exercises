#lets build a menu

# print("There will be a menu")
# print("Below here: ")

# the bank of users for testing. 2 dicts in a list
customers = [
{'name':'aone', 'balance':1000},    
{'name':'btwo', 'balance':500}
]

def check_user(user, user_list):
    user_names = [i['name'] for i in user_list]
    return user in user_names

# scaffolding for using sqlite
# def insert_customer(emp):
#     with conn:
#         c.execute("INSERT INTO customers VALUES (:name, :balance)", {'name': emp.first, 'balance': emp.last})


def see_balance(user, user_list):
    user_balance = [i['balance'] for i in user_list if i['name'] == user]
    return user_balance

def add_to_balance(user, amount):
    for i in customers: 
        if i['name'] == user: 
            i['balance'] += amount 

def subtract_from_balance(user, amount):
    for i in customers: 
        if i['name'] == user: 
            i['balance'] -= amount

def print_menu():
    print( 30 * "-" , "MENU" , 30 * "-")
    print( "1. View Current Balance")
    print( "2. Make A Deposit")
    print( "3. Make A Withdrawal")
    print( "4. Wish there was a fourth option")
    print( "5. Exit")
    print( 67 * "-")
  
loop=True      

current_user = input("What is your user name? ")
if check_user(current_user, known_users):
    print(" welcome back")
else:
    print(" A new user!")

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))
     
    if choice==1:     
        print("Menu 1 has been selected") 
        current_balance = see_balance(current_user, customers)
        print(f"Your current balance is ${str(current_balance)[1:-1]}")
    elif choice==2:
        print("Menu 2 has been selected")
        ## 
    elif choice==3:
        print("Menu 3 has been selected")
        ## 
    elif choice==4:
        print("Menu 4 has been selected")
        print("More features to come!")
        ## The exit choice to break the while loop
    elif choice==5:
        print("Menu 5 has been selected")
        break

        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")