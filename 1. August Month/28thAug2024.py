# Input & Output in Python 

# user_input = input("Prompt : ")  # input() is a function call, it gets first priority
# print(user_input)
# print(type(user_input))  # <class 'str'>


# age = input("Enter you age? ")  #input() is an inbuilt function 
# print(age)
# print(type(age))

# to convert to number, we will use typecasting
# print(int(age))
# print(type(int(age)))

# int_age = int(age)  #it is integer now
# print(int_age)

# Doubt --- Data type chages permanently or temporary ?

# not optimize code 

# age = int(input("Enter you age ? "))
# print(age)
# # print(type(age))



# user_height =float(input("Enter height in feet ?"))
# print(user_height)  # 5.6
# print(type(user_height))  # float 


# user_complex = complex(input("Enter a complex value ?"))
# print(type(user_complex))
# print(user_complex)


# user_list = list(input("Enter a list: "))
# print(type(user_list))
# print(user_list)  # ['[', '1', ',', '2', ',', '4', ']']  # each charactes is treated as a single element of a list 


# Built in fucntion - eval  -- to evaluate the proper data type what user enter it 
# it is used to get intended collection data type from the user 

# user_list = eval(input("Enter a list: "))
# print(type(user_list))
# print(user_list) 


# How eva works?

# int()
# eval ('10.5')  # it is just removing the double quotes..... and whatever is left inside the quote, that will be your data type  

# eval can be used for sinle & collection value.

eval('10')  #simply remove the quotes, integer


# eval('Hello') # remove double quotes.... Hello --- it is nothing in data type  ( Name Error )
# you can't used on string 

# eval("Hello")

eval("bool")
eval("True")

eval(" 'hello' ")

# user_list = eval(int("Enter a list"))
# print(user_list)
# print(type(user_list))



# Output Function  - To show something on terminal 

# The syntax for print function 

# print(value1, valu2, value3......valun, sept=" ", end= )
# sep -- separator, defaule value is space ( " " )
# end --- be default value is \n  (new line character )  - end ="\n"
# print(value1, valu2, sep="", end="\n")


value1 = 10
value2 = 20
print(value1, value2, sep="", end="\n")   # end="\n" -- It will start from new line 
# 1020
print(value1, value2, sep="@", end="--")
print("bye")
# 10@20--bye




# Formatted String - any string prefixed by the letter with the small f. 

name = input("Enter your name? ")
print(name)
# I want to beautify above print thing
print("Buddy, your name is name ")  # here name is a string
print(f"Buddy, your name is {name} ")  # put f, to make name (string) to a variable.

# To use variable inside a string, use formatted string. 

# Copy Operator