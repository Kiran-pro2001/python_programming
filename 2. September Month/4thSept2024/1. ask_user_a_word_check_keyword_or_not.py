# Ask user a word, check keyword or not

import keyword 

word = input("Enter a word :")
# print(keyword.kwlist)  # a list of keyword come
if word in keyword.kwlist:
    print(f"{word} is a keyword!")
else:
    print(f"{word} is not a keyword!")


