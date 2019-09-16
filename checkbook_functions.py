#Functions to be used in the main checkbook.py

#check to see if this user exists. If it returns false, a new user creation function
#should be called
def check_user(user, user_list):
    user_names = [i['name'] for i in user_list]
    return user in user_names

def create_new_user(name, balance):
    known_users.append(
        {'name':name,
         'balance': balance
        }
    )


def make_deposit(deposit, balance):
    return balance + deposit

def make_withdrawal(withdrawal, balance):
    return balance - withdrawal
