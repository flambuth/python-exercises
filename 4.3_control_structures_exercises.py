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

#   2
#   Loop Basics    While
#        Create an integer variable i with a value of 5.
#        Create a while loop that runs so long as i is less than or equal to 15
i = 5
print(i)
while i <= 14:
    i += 1
    print(i)
# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.
x = 0 
while x < 100: 
    x += 2 
    print(str(x)+"\n")

# Alter your loop to count backwards by 5's from 100 to -10.
x = 100 
while x > -10: 
    x -= 5 
    print(str(x)+"\n")

# Create a while loop that starts at 2, and displays the number squared on each line while the number is 
# less than 1,000,000. 
x = 2 
while x < 1000000: 
    x = x ** 2 
    print(str(x)+"\n")

# Write a loop that uses print to create the output shown below.
x = 100
print(x)
while x > 5:
    x -= 5
    print(x)

# 3 FOR LOOPS
# Write some code that prompts the user for a number, then shows a multiplication table up through 10 for that number.
z = int(input('Please enter a number: '))
count = 1
for i in range(1,11):
    print(str(z) + ' x ' + str(count) + ' = ' + str(z*count))
    count += 1

# Create a for loop that uses print to create the output shown below.
#1
#22
#333
q = input('Please input a number: ')
count = 1
for i in range(1,int(q)+1):
    print(str(count)*count)
    count += 1

# 4         BREAK and CONTINUE
#    Prompt the user for an odd number between 1 and 50. Use a loop and a break statement to continue prompting 
#    the user if they enter invalid input. (Hint: use the isdigit method on strings to determine this). 
#    Use a loop and the continue statement to output all the odd numbers between 1 and 50, except for the number 
#    the user entered.

ready2play = input("Do you want to play? ") 
     ...: if ready2play == "y" or ready2play == "Y": 
     ...:     user_odd_number=int(input("Please enter an odd number between 1 and 50: ")) 
     ...:     print(f"Number being skiped is: {user_odd_number}" ) 
     ...:     for i in range(1,50,2): 
     ...:         if i==user_odd_number: 
     ...:             print("this got skipped") 
     ...:             continue 
     ...:         print(f"Here is an odd number: {i}")

#The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, also note that the 
# input function returns a string, so you'll need to convert this to a numeric type.)

good_to_go = True
while good_to_go:
    player_number = input('Please enter a number: ')
    if player_number.isdigit() == False:
        print("That is not a number. ")
        good_to_go = False
    else:
        for i in range(int(player_number)+1):
            print(i)
        break

# Write a program that prompts the user for a positive integer. Next write a loop that prints out 
# the numbers from the number the user entered down to 1.
player_number = input('Please enter a number: ')
if player_number.isdigit() == False:
    print("Not a number")
elif int(player_number) < 0:
    print("Thats not a positive number")
else:
    for i in range(int(player_number),1):
        print(i)    

# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

while good2go == True:
    for i in range(100)
        if i 