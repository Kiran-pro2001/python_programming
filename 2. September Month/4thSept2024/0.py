# Ask user a word - keyword or not 

import keyword # build in module 
print(keyword.kwlist)  # print all the list of keywords 

word = input("Enter a word :")
if word in keyword.kwlist:
    print('Valid Keyword ')
else:
    print("Not a valid keyword ")
    
    
    
# enter a collection -- user entered collection has less than of qual to 5 elements  -- 1,2,3,4,5    -- if more than 5, then go to else
# WAP to check is the user enterd collection has less than 5 or more than 5 elemnts 

enter_collection = eval(input("Enter a Collection :"))
length_collection = len(enter_collection)
if length_collection <= 5:
    print("The length is less than 5")
else:
    print("The lenght is greater than 5")

# len() - total elements in a collection! 





# Revising String Functions -

string = "kirankumar"
print(string.islower())  # True (Returns  )  # (Returns True, if all the charactes in the string is in lowercase, else False)
print(string.isupper()) # False (Returns True, if all the characters in the string in uppercase, else False)
print(string.isalnum()) # False    (Returns True if all the characters in the string are alphanumeric, else False)




# check single value data type or a collection 
# WAP to check if the user eneterd data is a sinlge value data type or a collection 

data = eval(input("Enter a  Data :"))
if type(data) in [int,float,complex,bool]:
    print("Single Value Data Type")
else:
    print("Multivalue Data type")
    
    


# enter alphabet --- if vowel - print vowel, if not print consonant

alphabet = input("Enter an alphabet :")   # 'a'
if alphabet in ['a','e','i','o','u']:  # 'a' in ['a','e','i','o','u']
    print("It's an Vowel")
else:
    print("It's a Consonant")
    


# two statements for single condition
# one statement for single condition



# multiple condition -- separate statement block 
# if elif 





# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



# elif
# if elif else Block 


# user enter two numbers, you need to find relation between the numbers.  (<,=,>)

# for different condition..separate block will be there
# never use elif directly, start with if first. 
# elif is a short form of else if
# never write condition in else block
# you can any number of elif, and else is optional.  Else at end.
# for else block to be executed, all the above conditions should be false.

num1 = int(input("Enter a num :"))
num2 = int(input("Enter a num2 "))
if num1 == num2:
    print("Both are equal")
elif num1>num2:
    print(f"{num1} is greateer than {num2}")
else:
    print(f"{num1} is less than {num2}")
    
    
    
# if condition 1
# elif condition 2
# elif condition 3
# elif condiition 4
# else

# if condition 1 is True, then print it's true statement block, and come outside.
# if condition 1 if False, it will go to elif condition 2, and execute it's true statement block, and come outside. 
# if anyone condition is true, execute it's statement block.
# let's all conditions are false, only the else block gets executed. 