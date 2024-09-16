# user for a word, if the check character is in upper case or not 
# user entered a word, now check is the first character of the word is uppercase or not 


# word = input("Enter a word ?")  # by defautl in string 
# if word[0].isupper():  # True or False it should retuns, then it is usef for the printing the logic -
    # print("The first character is in Uppercase")  # this will only get exeute if the above thing is True. Hence no need to put the True thing. 


# one more approach will be --
# if word[0].isupper() == True:     #This is not optimized, since the print will only execute when there is a True condition.
    # print("The first character is in Uppercase")





# Enter a number in original format, then tell it is position number or not

# my_num = eval(input("Enter a number ?"))
# if my_num > 0:
#     print("It's a positive number")





# user enter a number is 2 digit number or not 

# number = eval(input("Enter a number :"))
# if number > 9 or  number < 100  or number < -99 or number != 0:   # 10,11, 99,   annd -11, -23 , -99 
    # print("Two Digit Number ")
# Error 



# number = int(input("Enter a number "))
# if (number>9 and number <99) or (number < -9 and number > -99)



    


# number = input("Enter a number :")
# length = len(number)
# if length == 2:
    # print("It is a two digit number")  # -20 -- the lenght will 3, since string will consider a minus as one length 
    # not optmized 
    
    


# it is a 3 digit number 







# number -- multiple of 5 ....the remainder should be 0 
# num2 = int(input("Enter a number"))
# if num2 % 5 == 0:
#     print()







# number -- if the number is a multiple of 5, and also divided by 3 -- give remainder 0
# multiple of 5 & divisor of 3










# ask the user -- to two set --- one set is a subset of another subset

set1 = eval(input("Enter a set1 :"))
set2 = eval(input("Enter a set 2 :"))
# if set1.issubset():  -- why problem ?
#     print("Set 1 is a subset of Set 2")



if set1 < set2 or set2 < set1:
    print(f"{set1} is a subset of {set2}")
    
    
    
# Method 2 
    # if set1.issubset(set2) or set2.issubset(set1):
    
    
    
    
    
    
# Above are my try 
    
    
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++   By SIR ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
    
    
# write a program to check, if the user entered word start with a uppercase
word = input("Enter a word :")
first_char = word[0]
if first_char.isupper():
    print("Starting with Upper")

# WAP to check if the user entered number is a positive number 
num = eval(input("Enter a number "))
if num > 0:
    print("Positive Number ")



# WAP to check if the user entered number is the multiple of 5 and divisible by 3 (AND)
num2 = int(input("Enter a number :"))
if num2%5 == 0  and num2%3==0:
    print(f"{num2} os a multiple of 5 and divisible of 3")



# WAP to check if the user entered number is a three digit number 
num = int(input("Enter a number "))
if (num>99 and num<1000) or (num<-99 and num>-1000):
    print("It's a three digit number ")
    


# WAP to check is the user entered set is a subset of another set   # Both can be work as a subset -- either of the case 
set1 = eval(input('Enter a set 1 :'))
set2 = eval(input("Enter a set 2"))
if set1 < set2   or   set2 < set1:
    print(f"{set1} is a subset of {set2}")
    print(f"One set is a subset of another")



# method 2
if set1.issubset(set2) or set2.issubset(set1):
    print("")


# Palindrome --- if reverse, then also it is same.   
# Example -     MALAYALAM 
# EXample -   MADAM,  DAD, MOM, WOW


# check if the user entered word is a palidrome or not ?
# WAP to check is the user entered word is palindrome 
# Palindrome Number ---  Important ********** 
word = input("Enter a word")
rever_word = word[::-1]
if word == rever_word:
    print("It's a palindrome")