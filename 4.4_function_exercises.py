#You're already going to hell about that hippopotamous thing

#1
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the 
# string 2, False otherwise.
def is_two(number):
    return number == 2 or number == '2'

#2
# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(char):
    return len(char) == 1 and char.lower() in 'aeiou' 

#3
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. 
# Use your is_vowel function to accomplish this.
def is_consonant(char):
    return char.lower() not in 'aeiou'

#4
# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if 
# the word starts with a consonant.
def capitalize_if_start_with_cons(word):
    if word[0] not in 'aeiou':
        return word.capitalize()

# The streamlined version
def capitalize_if_start_with_cons(word):
    return word.capitalize() if is_consonant(word[0]) else word

#5
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.
# I added a default value tip of 10 percent
def calculate_tip(bill, percentage = .1):
    return bill * percentage

#6
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price 
# after the discount is applied.
def apply_discount(price, discount):
    return price - price*discount

#7
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and 
# return a number as output.
# def handle_commas_my_way(phrase):
#     commas = [i for i in phrase if i==',']
#     return len(commas)

def handle_commas(s):
    no_commas = [i for i in s if i!=',']
    return float("".join(no_commas))

assert handle_commas('1,000') == 1000

#8
# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that 
# number (A-F).
def numbers_into_grade_letter(number):
    number = int(number)
    if number => 90:
        print('A')
    elif number >80 and number<90:
        print('B')
    elif number >70 and number<80:
        print('C')
    else:
        print('You failed.')

#################
#9
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(phrase):
    no_vowels = [i for i in phrase if i.lower() not in 'aeiou']
    return ''.join(no_vowels)

####################
#10
# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#    anything that is not a valid python identifier should be removed
#    leading and trailing whitespace should be removed
#    everything should be lowercase
#    spaces should be replaced with underscores

def normalize_name(phrase): 
    if phrase[0].isalpha() == False:
        print ("You need the first character to be a letter")
    phrase = phrase.strip() 
    phrase.replace(" ","_") 
    phrase = phrase.lower() 
    return phrase 

#####################
#11
# Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative 
# sum of the numbers in the list.
#This is the cheap version using an import. I get the feeling kwargs or args was what y'all had in mind
#That way the function can take a bunch of integer arguments instead one list

from itertools import accumulate

def cumsum(seq_of_numbers):
    return list(accumulate(seq_of_numbers))

#Now without importing some functions
def makes_a_cumulative_list(*args):
    """ Returns a list that is the cumulative sum of the sequence of intengers passed as arguments """ 
    count = 0 
    cum_list = [] 
    for i in args: 
    #This is the starting condition. The rules change after the first argument is cemented at index 0
        if count == 0: 
            cum_list.append(i) 
            count = i 
    #Add to the list that will be returned the sum of next argument and the last one, stored in count 
    #and becomes the new count for the next round of the iteration
        else:
            cum_list.append(i+count) 
            count = i+count 
    return cum_list





#################
#bonus 1


# convert a hour:min[am|pm] time into 24 hour format
def twelve_to_24hrs(old_time):
    old_time = old_time[0:-2]
    return old_time

#  ^ This is starting to get very clumsy

#good enough for me, but feels not efficient
def twelve_to_24(time): 
    ...:     phase = time[-2:] 
    ...:     hour = time[:2] 
    ...:     mins = time[3:5] 
    ...:     if phase == 'pm': 
    ...:         hour = str(int(hour)+12) 
    ...:         return hour + mins 
    ...:     else: 
    ...:         return hour + mins

#convert military to am/pm time
#gonna use the datetime module to do it cleaner
# make a date time object
# x = datetime.datetime(2020, 5, 17)

def twenty4_to_twelve(time):
#initial test to make sure the time is at least a number
    if time.isdigit() == False:
        return "That is not a valid time."
    else:
        x = datetime.

def right_now_in_24hr():
    import datetime
#make a datetime object and cut out the hour and minutes using the string
#formatting method the object has. Using a %to indicate what to slice
#that method will not take more than 1 argument
    x = datetime.datetime.now()
    hour = x.strftime("%H")
    mins = x.strftime("%M")
#using fstrings to format these non-strings into some string output
    return f"It is {hour}{mins} hours"



######################
#Create a function named col_index. It should accept a spreadsheet 
# column name, and return the index number of the column.

# def col_index(spreadsheet column name):
# command shift is a godsend. i wish i learned it sooner.
#     return index number of he column

# I think i'll do my work on this bonus question somewhere else
# It invovles importing pandas and so far some stuff that takes
# my old mac some time to process. 

# I went with using openpyxl instead as the module for loading excel workboks