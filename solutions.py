#Python Assessment

#1 
# Write a function named isnegative. It should accept a number and return a boolean value 
# based on whether the input is negative.

def isnegative(number):
    """

    >>> isnegative(4)
    False
    >>> isnegative(0)
    False
    >>> isnegative(-6)
    True
    """
    return number < 0

#2
# Write a function named count_evens. It should accept a list and return the number of odd 
# numbers in the list.

def count_evens(number_list):
    """

    >>> count_evens([1, 2, 3])
    1
    >>> count_evens([4, 6, 8, 10, 12])
    5
    >>> count_evens([1, 3, 5, 7, 9])
    0
    >>> count_evens([])
    0
    >>> count_evens([3, 2])
    1
    """
    even_count = len([i for i in number_list if i%2==0])
    return even_count

#3
# Write a function named increment_odds. It should accept a list of numbers and return a 
# new list with the odd numbers from the original list incremented.

def increment_odds(number_list):
    """
    >>> from solutions import increment_odds
    >>> from solutions import increment_odds

    >>> increment_odds([1, 2, 3])
    [2, 2, 4]
    >>> increment_odds([2, 2, 1, 4, 5])
    [2, 2, 2, 4, 6]
    >>> increment_odds([])
    []
    >>> increment_odds([0, 1])
    [0, 2]
"""
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
    """
    >>> from solutions import average

    >>> average([1, 2, 3])
    2.0
    >>> average([4, 6, 8, 10, 12])
    8.0
    >>> average([1, 2])
    1.5
    """
    number_list = [float(i) for i in number_list]
    return sum(number_list)/len(number_list)

#5
# Create a function named name_to_dict. It should accept a string that is a first name 
# and last name separated by a space, and return a dictionary with first_name and 
# last_name keys.

def name_to_dict(full_name):
    """
    >>> from solutions import name_to_dict

    >>> name_to_dict('Ada Lovelace')
    {'first_name': 'Ada', 'last_name': 'Lovelace'}
    >>> name_to_dict('Marie Curie')
    {'first_name': 'Marie', 'last_name': 'Curie'}
    """
    first_name, last_name = full_name.split()
    name_dict = {'first_name':first_name, 'last_name':last_name}
    return name_dict
#6
# Write a function named capitalize_names. It should accept a list of dictionaries where 
# each dictionary represents a person and has keys first_name and last_name. It should 
# return a list of dictionaries with each person's name capitalized.

def capitalize_names(listo):
    """
    >>> from solutions import capitalize_names
    >>> names = []
    >>> names.append({'first_name': 'ada', 'last_name': 'lovelace'})
    >>> names.append({'first_name': 'marie', 'last_name': 'curie'})
    >>> names
    [{'first_name': 'ada', 'last_name': 'lovelace'}, {'first_name': 'marie', 'last_name': 'curie'}]
    >>> capitalize_names(names)
    [{'first_name': 'Ada', 'last_name': 'Lovelace'}, {'first_name': 'Marie', 'last_name': 'Curie'}]
    """
    capital_list = []                                                                                          
    for i in listo:  
        capital_list.append({'first_name':i['first_name'].capitalize(), 'last_name':i['last_name'].capitalize()}) 
    return capital_list

#7
#Write a function named count_vowels. It should accept a word and return a number that is 
# the number of vowels in the given word. "y" should not count as a vowel.
def count_vowels(wordo):
#    from collections import Counter
    """
    >>> from solutions import count_vowels
    >>> count_vowels('codeup')
    3
    >>> count_vowels('abcde')
    2
    >>> count_vowels('why')
    0
    """
    vowels = 'aeiou'
    wordo = wordo.lower()
    vowel_count = len([i for i in wordo if i in vowels])
    return vowel_count


#8
# Write a function named analyze_word. It should accept a string that is a word and return 
# a dictionary with information about the word, the total number of characters in the word, 
# the original word, and the number of vowels in the word.

#I wrote a custom doctest because i made a change to one of the dictionary keys and 
#I couldn't get teh order back. My custom doctest asserts true if the dictionaries have equality.
def analyze_word(wordo):
    """   
    >>> type(analyze_word('codeup'))
    <class 'dict'>
    >>> analyze_word('codeup')
    {'word': 'codeup', 'n_letters': 6, 'n_vowels': 3}
    >>> analyze_word('abcde')
    {'word': 'abcde', 'n_letters': 5, 'n_vowels': 2}
    >>> analyze_word('why')
    {'word': 'why', 'n_letters': 3, 'n_vowels': 0}
    >>> analyze_word('why') == {'word': 'why', 'n_letters': 3, 'n_vowels': 0}
    True

    """
    word_length = len(wordo)
    vowel_count = count_vowels(wordo)
    word_info = {
        'word':wordo,
        'n_letters':word_length,
        'n_vowels':vowel_count                
    }
    return word_info
