# Entered number is a three digit number

number = int(input("Enter a number ")) # '23.0' -- 23.0 
# 234,   -192, 34.3 , -78.2
if (number > 99 and number < 1000) or (number < -99 and number > -1000):
    print("It's a three digit number ")
else:
    print("It's not a three digit number")
    
    
# 234 -- three digit number 
#  -124 -- three digit number 

    
# 23.3 -- give error 
# since only allows to put integer value . no float value 

