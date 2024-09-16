# Coditional  - 10 Questions - if else -- full revision
# This Friday - laptop - test -- Tuesday, Wednesday, Thursday

# Write a program to check the user entered nummber is a single digit, double digit or three digit or more than that.


num = input("Enter a number :") # '23'
if len(num) == 1:  # 2 
    print("One Digit")
elif len(num) == 2:
    print("Two Digit")
elif len(num) == 3:
    print("Three Digit")
else:
    print("More than that digit")
    
'''    
(num>=0 and num<=9) or (num<=-9 and num<=-1)
-9 <= num <= 9
'''

'''

what is necessary, can I cut it down, 
writing a program is not a great thing
but optimize is imporant


do what you do.....then analyze it...remov unnecessary thing 


'''


num = input("Enter a number :")
if -9 <= num <= 9:
    print("Single Digit Number ")
elif -99 <= num <= 99:
    print("Two digit number ")    #it may get the single digit number, but this condition will only checks if it is not single digit...so automatically it gets removed
elif -999 <= num <= 999:
    print("Three Digit")
else:
    print("More than three Digit Numbers")
    
    
    
    
# if you direclty want to check the three digit number of not...
# then -999 <= num <= 999
# can't use it
# then you need to specify



# Use this if directly we need to find the three digit number 
# (num > 99 and num <= 999) or (num<-99 and num>=-99)



# if negative or not, then make it positive, and then typecasete it. 


# Write a program to find the greatest among three numbers enterd by the user.

num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))
if num1 > num2:
    if num1 > num3:
        print("Num1 is Greatest")
    else:
        print("Num3 is Greatest")
elif num2>num3:
    print("Num2 is Greatest")
    
    
    
# logic 2 
    
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
num3 = int(input("Enter the third number :"))
if num1 > num2 and num1 > num3:
    print(f"{num1} is greater. ")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greater.")
elif num1 == num2 and num1 == num3:
    print("Equal Numbers")
else:
    print(f"{num3} is greater. ")
    
    
# max of collection, store in a collection 
    

# Triangles -- three sided polygon is a triangle
# equilateral trianlge -- all sides are eequal
# tow sides are qwual -- 
# any not follow -- scalene
# Write a program to check if the three side of a triangle entered by the user is an equilaternal, isosceles or scalene triangle. 


side1 = int(input("Enter the side1 :"))
side2 = int(input("Enter the side2 :"))
side3 = int(input("Enter the side3 :"))
if side1 == side2 and side1 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:   # any two side can be saved
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
    
    
# in the same order....make priorities in head, give values to check. give your own values. do this work.....being a dealer means you are a tester, create your own test cases.



# Write a program to decide the bonus of an employee based on his experience.
# 0 to 2 - 10% Bonus.
# 3 to 5 - 25
# > 5 - 

sal = int(input("Enter your salary"))
experience = int(input("Enter your experience :"))
if 0 <= experience <= 2:    # experience <= 2  (assume positive values)
    print("10% Bonus", (sal*10)/100)  # just a bonus as ked
elif 3 <= experience <=5:
    print("25% Bonus", (sal*25)/100)
else:
    print("35% Bonus",(sal*35/100))
      





'''
scartch your head
hurt yourself
only you become programmer
without practice you can't get anything




num1
if num1<0:
    num1 = -num1
    len(str(num1))
    lenghth used further 

'''

num1 = int(input("Enter a number :"))
if num1 < 0:
    num1 = -num1
length = len(str(num1))
if 