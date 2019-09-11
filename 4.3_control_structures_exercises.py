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
if user_day.lower() == days_of_the_week[0] or user_day.lower() == days_of_the_week[-1]
    print('It is the weekend')
else:
    print('Nest pas the weekend')
