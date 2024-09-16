'''
elif -

If we have multiple conditions to check, and for each condition if there is a separate statement block, then we use elif statements. 

- It first checks if condition,if 'if' condition is True, it executes True statement block 1
- If 'if' condition is False, it goes to elif block, and checks the condition there.
- If elif condition is Ture, it enters to True Statement Block and if elif condition is False, it checks the next elif condition 
- If all the conditions are False, only then else block will be executed. 

Note -
- We can have any number of elif blocks. But it should start with a if block.
- Else BLock is optional. 



Syntax -
if condition1:
    True Statement Block 1
elif condition2:
    True Statement Block 2
.
.
elif conditionn:
    True Statement Block n
else:                           [Optional]
    False Statement Block  

'''

# Enter a number from 1 to 5, number is matching ..check is 1, 2,3,4,5

# number = int(input("Enter a number Between 1 to 5 :"))
# idea is comparing multiple times   




# take some time, even a microseconds is also important.
# checks if true, checks for other also.
# checks if ture, true statment block

# unnecessary checking of conditions
# separate else block we can have for multiple if
# but for if elif elif -- only else will be there 


'''

num = int(input("Enter a number between 1 to 5 :"))
if num == 1:
    print('1')
if num == 2:
    print('2')
if num == 3:
    print('3')
if num == 4:
    print('4')
if num == 5:
    print('5')




CASE - 2 : Using if elif else


num = int(input("Enter a number between 1 to 5 :"))
if num == 1:
    print('1')
elif num == 2:
    print('2')
elif num == 3:
    print('3')
elif num == 4:
    print('4')
elif num == 5:
    print('5')





- When we use only if block to check multiple conditions, no matter the conditions is true or false, it will check all if blocks. 
- When we use elif for multiple conditions, the moment the conditions become true, the respective true statement block will be executed, and python stops checking for other conditions. 


- The advantage of multiple if is, we can use multiple else here for each if. But for the case of multiple elif, we can only use else once. We can't use more than that.
- But the disadvantage of multiple if is, as the condition got True, it still checks for other conditions, here a lot of time will be gone, and in programming, a mili seconds are also important. So multiple ifs are not time efficient. 

'''