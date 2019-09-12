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
def get_letter_grade(score):
    

#9
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.