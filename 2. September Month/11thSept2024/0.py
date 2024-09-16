# Nested if

'''
When there is if statement inside another if statement, we called it a nested if. 



'''


''''

Syntax -

if condition1:

    [True Statement Block 1]
    
    if condition2:
        True Statement Block 2
    else:
        False Statement Block 2
else:

    False Statement Block 1
    
    
    
# Flow diagram



# 
1. True statement Block 2 will only be executed, when condition 1 is and condition 2 are both true.
2. With the nested if, we can have a separte false statement block for each condition used in a program. 




'''





# Write a progam to check if the user entered is a vowels or not, only if the character is an alphabet. 

# enter an alphabet, first check if it is alphabet, then check it is vowels or consonants


char = int(input("Enter a  character :").lower())
length = char.len()
print(length)
if length == 1
if char.isalpha():
    if char in "aeiou":  # or char in "aeiouAEIOU"
        print("Vowels")
    else:
        print("Consonants")
else:
    print("Not an alphabet")
    
    
# a - vowels
# ki -- consonants
# ai -- consonants




char = input("Enter a  character :").lower()
if char.islalpha() and char in 'aeiouAEIOU':
    print("Vowels")

# no more options for the user, not clear







# write a program to check if the user enterd integer is a multiple of 5 only if it is an even number .

# We will check for multiple of 5, only if the user entered number is an even number. 


number = int(input("Enter a number "))
if number%2 == 0:
    if number%5 == 0:
        print("The number is multiple of 5 and it's even number ")
    else:
        print("The number is even, but it is not multiple of 5")
else:
    print("The number is not an even number ")
    
    
    
# you can not have separate false block, if i will use if else. Not the nested if else.








### Next level program 
## instagram login
## while login -- proper login credentials we need to give

# login scenario mimic it 



username = input("Enter your username :")
password = input("Enter your password :")
# Already registered - we assume that. 
database = {username: 'kiran',
            password: '1234'}

if username == "kiran" and password == '1234':
    print("Login Successful")
else:
    print("Wrong Credentials")
    
    
    
# Write a program to validate the username & password enterd by the user to login to an application.
    
    
database = {"kiran": "1234", "kunal":"23$5"}
username = input("Enter your username :")
password = input("Ente your password :")

if username in database:
    actual_password = database[username]
    if password == actual_password:
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Username not found")

    
    



# Register one also do it