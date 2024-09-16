# Entered character is a special character or not 

character = input("Enter a character :")
if character.isalnum():  #it will check for alphanumeric -- alphabets or numbers
    print("It is not a Special Character")
else:
    print("It is a Special Character")
    