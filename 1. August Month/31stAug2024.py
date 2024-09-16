# Control Statements 

# 1. Conditional Statements - simple if, if else, if elif, nested if
# 2. Looping Statements - while, for

# Simple if



'''

Synatax -

if condition:
    True Statement Block 
    

'''


# To check if a number is even?

# num = int(input("Enter a number ? :"))
# if num%2==0:
#     print("Even Number ")




# Question 2 - Collect a string from the user, Whatever character he enters...if it is vowels...print vowels..if not, then nothing

# user_input= input("Enter a character ?").lower()
# # Vowel - aeiou (uppercase & lowercase )
# # if user_input == "a" or user_input="e"    - not optimized
# # vowels = ['a','e','i','o','u']  # list of vowels
# # if user_input in vowels:
# #     print("It's a vowels")


# # Method 2
# if user_input in "aeiou":   # write a condition in such a manner that, it should either return True or False 
#     print("It's a vowel ")




# Notes - 

'''
Control Statements 
This are the statements which controls the flow of execution of the program. 

These are of two types - 
1. Decisional or Conditional Statements.
2. Looping Statements  


Conditional Statements -
These are the control statements which checks for the condition. 
If the condition is True, It performs a set of instructions. 

Types of Conditional Statements -
1. Simple if.
2. if else.
3. if elif.
4. Nested if. 


Simple if - 
-----------

Here We check for a certain condition. If the condtion is True, True statement block will be executed. 
If the condition is False, True statement block will not be executed.


Syntax -

if condition:
    True Statement Block  
    
----
one tab space is there


if condition
if the condition is Ture, then only it will execute True Statement Block
if it is False, it will move further. 




'''
# Write a program to check if a number is even 
# number = int(input("Enter a number :"))
# if number%2 == 0:
#     print("Even Number ")
    
    
# Write a progam to check if an alphabet is vowel
# alphabet = input("Enter an alphabet :").lower()
# if alphabet in "aeiou":
#     print("Vowel")


# enters string, store like string...if list, then store in list...... same format we need to store --store in original format
# only if single value data type --then print the type of data type

#Write a program to check, if the user entered value is single value data type --

# value = eval(input("Enter a value :"))
# type_of_value = type(value) # sensible variable name -- choosing a sensible name is an art.

# if type_of_value in [int,float,complex,bool]:   #not write the quotes in int (it's in proper format)    -   type_of_value == int  or type_of_value == float   or type_of_value = complex   # you can use list, tuple or anything
# int is a data type in list 
    # print(f"The {value} belongs to Single Value Data type")  #To beautify


# 2+5j,  (2+5J), True, 34,  -- All are single value data type
# [10,20,30]  - not a single value data type







# +++++++++++++++++++++++++++++++++++++  REVISION ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


# num1 = int(input("Enter a number "))
# if num1%2 == 0:
#     print('Even number ')



#Write a program to check, if the user entered value is single value data type --

user_enter = input("Enter a value: ")
type_of_value = type(user_enter)
