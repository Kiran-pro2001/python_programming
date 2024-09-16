# Write a program to check an entered number is positive or not ?

num = eval(input("Enter a number :")) # 2  , 2.0, -3, -30.0, 6+5j, True
if num > 0:
    print(f"{num} is a positve number")
else:
    print(f"{num} is a negative number")

# 2 - Positive
# 2.0 - Positive
# True -- positive   (Doubt)  -- It means, it is taking True as a 1.--- so 1>0 -- Therefore Positive.
# False -- Negative   (Doubt) -- It means, it is taking False as a 0.---- 0>0 -- no -- Therefore Negative. 
 
# None -- Error
# kiran -- Error
# (2+7j)  -- Error 
# [2,3]  -- Error
# {1,2,3}  -- Error


# To validate only number should enter, we should use int function 


num1 = int(input("Enter a number :"))
if num1 > 0:
    print(f"{num1} is a positive number ")
else:
    print(f"{num1} is a negative number")

# other than int value, it will give error to all types. 


# 10 - Positive Number
# 10.0 - Error
# kiran - Error
# True - Error


# So you have to use....eval function...so that number can be entered with different data type, and it just removed the outer quotes. 