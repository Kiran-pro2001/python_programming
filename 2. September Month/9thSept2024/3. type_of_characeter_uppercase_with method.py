# Type of character - uppercase, lowercase, number, special symbol  [using method]

character = input("Enter a character :")
if character.isupper():
    print("Uppercase")
elif character.islower():
    print("Lowercase")
elif character.isnumeric():  #isdigit() can also be used
    print("Numeric")
else:
    print("Special Characters")
    
    
# kra -- lowercase
# Kiran -- Special Characters (Since isupper(), islower(), isdigit(), isnumeric() checks for all the characters to be uppercase/lowercase/numeric)