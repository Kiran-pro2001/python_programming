# Entered Number is Two Digit Number of Not ?

number = int(input("Enter a number :"))
print(number)
if (number>9 and number <100) or (number<-9 and number>-100):
    print(f"{number} is a two digit number ")
else:
    print(f"{number} is not a two digit number")
    
# 4.3  -- coming error
# ValueError: invalid literal for int() with base 10: '4.3'

# So use eval function


number = eval(input("Enter a number :"))
print(number)
if (number>9 and number <100) or (number<-9 and number>-100):
    print(f"{number} is a two digit number ")
else:
    print(f"{number} is not a two digit number")

# 233 - is not a two digit number 
# -12.32 is a two digit number 
# 23.2 is a two digit number 
# 233 is not a two digit number

#kiran -- Error
# 3+5j  --- Error
# True -- is not a two digit number    (Doubt) -- It considers as 1. Hence 1 is not a two digit number 
# False -- is not a two digit number (Doubt) -- It considers as 0. Hence 0 is not a two digit number 





# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Logic 2  - By using len Function

number = eval(input("Enter a number :"))
length = len(number)
if length == 2:
    print("Two digit number ")
else:
    print("Not a two digit number ")
    
#
# 23.2 - error
#kiran - error

# The above will give error 


number = input("Enter a number : ")  # '23'
length = len(number)    # len function is the find the length of a string value ---- ** string value is important...it can't find the lenght of a integer value
print(length)
# 23  --- 2
# kiran  --- 5
# 2+7j ----- 4
# True --- 4
# 203.3  ---- 5

if length == 2:
    print("Entered number is a two digit number")
else:
    print("Entered number is not a two digit number")
    
# ki --- two digit number 
# 23.4 ---- not a two digit number 


# Hence logic 2 is not optimized, because it is telling for string value (ki -- two digit number ), it is also telling for float falue...(2.  -- two digit number)