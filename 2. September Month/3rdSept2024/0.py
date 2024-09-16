# If else Block 

'''
if conditio is true, execute true statement block...if not, then implement false statement block 


if condition:
    True Statement Block
else:
    False Statement Block


    
Don't mention conditionin in else block. 


if -- keyword -- reserved word to python 


'''


# Check a number is positive -- if number > 0, it is positive, if condition is false, then negative number 

num = int(input("Enter a number :"))   # for simplicity, let's take for int 
if num >= 0:
    print(f"{num} is a Positive Number ")  # True Statement Block
else:
    print(f"{num} is a Negative Number ")  # False Statement Block 
    
    
    
# enter a character -- alphabet --- it is lowercase or uppercase
# The below is my code..which is wrong  ! ! 

# user_enter_character = eval(input("Enter a character "))  # a
# if user_enter_character.lowercase():
#     print(f"The entered character is in lowercase")
# else:
#     print(f"The entered character is in uppercase")

# wrong -- eval no need, isupper()   -- mistakes I have done

user_enter_character = input("Enter a character ")  # a
if user_enter_character.islower():
    print(f"The entered character is in lowercase")
else:
    print(f"The entered character is in uppercase")


# Interviewer want the faster answer....so learn with build in functions and without build in fucntions
# faster answer - they want.......   with build i & without build in

# Logic 2 - Without Build In

user_enter_character = input("Enter a character ") 
if  'A'<= user_enter_character <=' a':
    print("Uppercase")
else:
    print("Lowercase")
    
    
# Logic 3 - char in 'ABCD .....Z"  

# A - 65
# Z = 90

# a - 97
# z - 122

# char 
# convert to asci   -  ord(char)  -- ord function takes character as an argument, returns the asci value 
# check the asci value is in between the range  - 65 to 90 range         65 <= asci <= 90


# enter anything...check the value is mutable or immutable
# mutable - list, dict, set
# immutable - single value, string, tuple
# a = 145 -- we can't convert to 146  -- immutable





user_input = eval("Enter any value :")
data_type_of_user_input = type(user_input)
if data_type_of_user_input in [list, set,dict]:    # I can use tuple also, list also...anything is good to go  -- mind it, don't put in quotes -- it is a class
    print("Mutable")
else:
    print("Immutable")
    


# enter a numer - if even number -- print square of a number ..... if not even -- print the cube of a number 

number = int(input("Enter a number  :"))
if number%2 == 0:
    print("Even Number ")
    print("The square of a number is", number ** 2)
else:
    print("Not a even number")
    print("The cube of a number is ", number ** 3)


# logic 2 -- storing in a variable the square & cube...and then check either is even or odd 


number = int(input("Enter a number :"))
square = number ** 2
cube = number ** 3
if number % 2 == 0:
    print(square)
else:
    print(cube)




# Special Characters -- other then numbers & alphabets

# enter a number -- check special character or not 


user_input= input("Enter a character :")
if  not ('a' <= user_input <= "z"  or  'A' <= user_input <= "Z"  or '0'<= user_input <= '9'):
    print("It is a special character")
else:
    print("It is not a special character")
    
# ai  - not a special character 


# char.isalnum()






# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Notes By Sir

'''

if else - 
When there is two statements block for a single condition we make use of if else keywords. 

Syntax - 
if condition:
    True Statement Block
else:
    Flase Statement Block 
    
---
one tab


If the condition is True, True statement block will be executed and the control will not enter else block. 

If the condition is False, Flase statement block will be executed. Which is mention in Else Block. 




WAP to check if the user entered number is a positive or not & print accordingly 

user_input = int(input("Enter a number :))
if user_input >= 0:
     print("Positive Number")
else:
    print("Negative Number ")




WAP to check if the user entered alphabet is uppercase or lowercase
alphabet = input("Enter an alphabet")
if alphabet.islowercase():
    print("Lowercase")
else:
    print("Uppercase")





wAP to check if the user entered character is special character or not, and print accordingly

char = input(input("Enter a character :"))
if 'a'<= char <= 'z'  or 'A' <= char <= 'Z' or '0' <= char '9':
    print("Not a Special Character")
else:
    print("Special Character")


Method 2 - 

if char.isalnum():
    print("Not a Special Character")
else:
    print("Speical Character")





WAP to check, if the user enterd data is mutable or immutable

data = eval(input("Enter any data :"))
if type(data) in [list, set, dict]:
    print("Mutable Data")
else:
    print("Immutable Data")
    
    


WAP to print, square of a number if the user entered number is even, else print cube of the number 

number = int(input("Enter a number :"))
if number % 2 == 0:+
    print(f"Square of a number {num**2}")
else:
    print(f"Cube of a number: {num ** 3}")




'''