is = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

x = i for i in fruits if i.count('a') +i.count('e') +i.count('i') +i.count('o') +i.count('u')) > 2
]


######## lets figure out the continue y/n game

good2go == True
while good2go:
    print("we are inside the while loop that happens when good2go is true")
    player_choice = input("Give me some version of no to break out of this loop. If you dont, you'll see these lines again.")
    if player_choice.upper() == 'N' or player_choice.upper() == "NO":
        break
    else:
        continue