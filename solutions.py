#Python Assessment

#1 
# Write a function named isnegative. It should accept a number and return a boolean value 
# based on whether the input is negative.

def isnegative(number):
    return number < 0

#2
# Write a function named count_evens. It should accept a list and return the number of odd 
# numbers in the list.

def count_evens(number_list):
    even_count = len([i for i in number_list if i%2==0])
    return even_count

#3
# Write a function named increment_odds. It should accept a list of numbers and return a 
# new list with the odd numbers from the original list incremented.

def increment_odds(number_list):
    new_list = []
    for i in number_list:
        if i%2 != 0:
            i = i+1
            new_list.append(i)
        else:
            new_list.append(i)
    return new_list

#4
#Write a function named average. It should accept a list of numbers and return the mean 
# of the numbers.

def average(number_list):
    number_list = [float(i) for i in number_list]
    return sum(number_list)/len(number_list)

#5
# Create a function named name_to_dict. It should accept a string that is a first name 
# and last name separated by a space, and return a dictionary with first_name and 
# last_name keys.

def name_to_dict(full_name):
    first_name, last_name = full_name.split()
    name_dict = {'first_name':first_name, 'last_name':last_name}
    return name_dict
#6
# Write a function named capitalize_names. It should accept a list of dictionaries where 
# each dictionary represents a person and has keys first_name and last_name. It should 
# return a list of dictionaries with each person's name capitalized.

def capitalize_names(listo):
    capital_list = []                                                                                          
    for i in listo:  
        capital_list.append({'first_name':i['first_name'].capitalize(), 'last_name':i['last_name'].capitalize()}) 
    return capital_list

#7
#Write a function named count_vowels. It should accept a word and return a number that is 
# the number of vowels in the given word. "y" should not count as a vowel.
def count_vowels(wordo):
#    from collections import Counter
    vowels = 'aeiou'
    wordo = wordo.lower()
    vowel_count = len([i for i in wordo if i in vowels])
    return vowel_count


#8
# Write a function named analyze_word. It should accept a string that is a word and return 
# a dictionary with information about the word, the total number of characters in the word, 
# the original word, and the number of vowels in the word.

def analyze_word(wordo):
    word_length = len(wordo)
    vowel_count = count_vowels(wordo)
    word_info = {
        'word':wordo,
        'n_letters':word_length,
        'n_vowels':vowel_count
    }
    return word_info
