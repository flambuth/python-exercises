#Functions to be used in the main checkbook.py

def check_user(user, known_users):
    user_names = [i['name'] for i in known_users]
    return user_name in user_names


def make_deposit(deposit, balance):
    return balance + deposit

def make_withdrawal(withdrawal, balance):
    return balance - withdrawal
