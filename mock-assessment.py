def normalize_name(phrase): 
    if phrase[0].isalpha() == False:
        print ("You need the first character to be a letter")
    phrase = phrase.strip() 
    phrase.replace(" ","_") 
    phrase = phrase.lower() 
    return phrase 

# python -m´ doctest mock-assessment.txt