#You're already going to hell about that hippopotamous thing

#1
# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the 
# string 2, False otherwise.
def is_two(number):
    return number == 2 or number == '2'

#2
# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(char):
    return char.lower() in 'aeiou'

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

#5
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.
def calculate_tip(bill, percentage):
    return bill * percentage

#6
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price 
# after the discount is applied.
def apply_discount(price, discount):
    return price - price*discount

#7
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and 
# return a number as output.
def handle_commas(phrase):
    commas = [i for i in phrase if i==',']
    return len(commas)

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


#9
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(phrase):
    no_vowels = [i for i in phrase if i.lower() not in 'aeiou']
    return ''.join(no_vowels)

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
        if count == 0: 
            cum_list.append(i) 
            count = i 
        else:
            cum_list.append(i+count) 
            count = i+count 
    return cum_list

#bonus
# convert a hour:min[am|pm] time into 24 hour format
def twelve_to_24hrs(old_time):
    old_time = old_time[0:-2]
    return old_time

#This is starting to get very clumsy

#good enough for me
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
