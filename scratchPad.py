fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

x = [fruit for fruit in fruits if
(fruit.count('a') + fruit.count('e') + fruit.count('i') + fruit.count('o') + fruit.count('u'))> 2
]


