# I smell a coma wedding!
# 1A
# prompt the user for a day of the week, print out whether the day is Monday or not
user_day = input('Please enter the day of the week ')
if user_day.lower() == 'monday':
    print('Yeah, it is Monday')
else:
    print('You want it to be Monday?')

# 1B
# prompt the user for a day of the week, print out whether the day is a weekday or a weekend
days_of_the_week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
user_day = input('Please enter the day of the week ')
if days_of_the_week.index(user_day.capitalize()) == 0 or days_of_the_week.index(user_day.capitalize()) == 6:
    print('It is the weekend')
else:
    print('Nest pas the weekend')

# 1C
# create variables and make up values for
#   the number of hours worked in one week
#   the hourly rate
#   how much the week's paycheck will be

#   write the python code that calculates the weekly paycheck. 
#  You get paid time and a half if you work more than 40 hours
hourly_rate = int(input("how much you make an hour? "))
hours_per_day = int(input("how long is your workday? "))
hours_worked = days_of_the_week.index(user_day.capitalize()) * hours_per_day
paycheck = hourly_rate * hours_worked