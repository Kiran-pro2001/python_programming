
# Check if a enterd string is a valid keyword or not 

import keyword 

word = input("Enter a word :")
if keyword.iskeyword(word):
    print(f"{word} is a valid Python Keyword")
else:
    print(f"{word} is not a valid Python Keyword")
    



import keyword

word = input("Enter a word :")
if keyword.iskeyword(word):
    print("Valid Keyword")
else:
    print("Not a valid keyword")
