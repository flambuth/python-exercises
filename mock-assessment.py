def normalize_name(phrase): 
    if phrase[0].isalpha() == False:
        phrase = phrase[1:]
    phrase = phrase.strip() 
    phrase = phrase.replace(" ","_") 
    phrase = phrase.lower() 
    return phrase 

# python -m´ doctest mock-assessment.txt

def cumsum(*args):
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