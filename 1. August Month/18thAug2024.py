
# var = input("Enter the data : ")  #input function always returns string value  - this can take any type of value
# print(var)
# print(type(var))


# var = int(input("Enter a number :"))  #Type conversion  - If we put float value, gives error (Value Error).
# print(var)
# print(type(var))

#To accept float values

# var = float(input("Enter a number :"))  #if put string value, gives error (Value Error)
# print(var)
# print(type(var))


# we have to change function for all type of data 
# So, in Python there is an all rounder function, that can take any types of data.
# That is  eval() function 

# var = eval(input("Enter any type of data : ")) # 5.6, 67,  "kiran",  True
# print(var)
# print(type(var))

# If we want to take any type of data, then go for eval() function

# But this is not recommended, as eval() function can execute any string as Python code. It's a security risk. So, always use type conversion functions when possible.



# We can use print function, and put values be separting by comma. And automatically when it gets printed, it take one space between them. 
print("Hello", "Kiran", "Krishna")  # Hello Kiran Krishna
# comma deke aapka jitna man ho utni value de sakte hai

#enke beech space nahi hai, mera psanadita separator ho -- (-) hiven
print("Hello","Kiran",sep='-')   # Jo bhi aapko separator dena hai, give in    sep='-'

# print function me kuch space nahi hai, mera psanadita separator ho -- (-) hiven

#default nature of print function is, it gets printed on the new line.

print("Hello")
print("World")

#Now,if I want ki....Hello World ...dono ek hi line me print ho....use one attribute called (end=' ') - ek space me end hoga fir

print("Hello", end=' ')   #Be default World ab new line me aata, but because of end=' ' , ab space deke World print hoga
print("World")


#If you want ki doo teen line baad print ho...to use \n 
print("Hello", end="\n \n \n")  #Teen line ka gape lekar print hoga
print("World")




# Comments - For good readability. Ignored by the interpreter.


print("Kiran Kumar")   #print() function is used to display something on the console

'''
Multi
Line
Comment'''


"""
Multi
Line
Comment """


# show keyword list ?

#Keywords are the reserved words whose meaning is already defined by the devlopers. We can't use keywords as an identifier name. Keywords are case sensitive. There are 35 Keywords according to Python 3.12.5  . You can't use keywords as your personal use. You can't use keyword as variable name, class name, function name. 

#To check the Python version 
# Open the cmd -   phython --version 

import keyword    #first import the keyword module
print(keyword.kwlist)   #call the kwlist function from the keyword module - that displays all keyword in list 

#This will print all python keywords.


# Practice  

import keyword
print(keyword.kwlist)


import keyword
print(keyword.kwlist)




print("Kiran")

name = "Kiran"
print(name)
print(type(name))


#Data Type - What type of value we are storing at particular memory location.
# single value - integers, float, complex, boolean
# multi value - strings, list, tuple, set, dictionary  (All Methods)
# operators - arithmetic, assignment, relational, logical, bitwise.


a = 10
print(a)
print(type(a))

a = 34.4
print(a)
print(type(a))

a = "Kiran"
print(a)
print(type(a))

a = 1+4J
print(a)
print(type(a))

a = 45+5j
print(a)
print(type(a))

a = True
print(a)
print(type(a))

# List 

# square bracket
a = [10, "kiran", 4+9j, 34.0]   #we can store any type of values into list
print(a)
print(type(a))


#Tuple
tup = (10, 234.0, "Kiran", False) # parenthesis
print(tup)
print(type(tup))



# Set

set = {1,2.4, True, "Kiran"}  # curly braces
print(set)
print(type(set))

# Dictionary - Key Value Pair, enclosed in curly brackets

dict1 = {"Name": "Kiran",
         "age": 23,
         "city": "Delhi"}
print(dict1)
print(type(dict1))

# To access the value corresponding to the key   - Use get() method

print(dict1.get("Name"))

# List, Tuple -- allow duplicate value
# set - no duplicate value allow (consider only one time that value)
# dictionary - no duplicate use of key , we can use same value, but no same key. Key should be unique always. 
# Latest key value will be considered, if same key will be there 

list1 = [1,1,1]
print(list1)

tup1 = (1,1,1)
print(tup1)

set1 = {1,1,1} #Output -  {1}
print(set1)

dict1 = {"name": "Kiran", "name": "Krishna"} #Can't duplicate keys, therfore latest key value will be considerd
print(dict1)
#Output -  {'name': 'Krishna'}


# List - ordered collection of items, changeable, allows duplicate values
# Tuple - ordered collection of items, unchangeable, allows duplicate values
# Set - unordered collection of items, changeable, does not allow duplicate values
# Dictionary - unordered collection of key-value pairs, changeable, does not allow duplicate keys




# List Data Structure 
print("List....")

list1 = []  #Empty list 
print(type(list1))

list2 = [10, "Kiran", True, 10.6, "Krishna"]  #All types of values we can put in list  #Duplicate values are allowed in list
print(list2)

#create list using list fucntion  list()

list3 = list()
print(type(list3))

list4 = list( (10, "Kiran", True, 10.6, "Krishna") )
print(list4)
print(type(list4))


list2 = [10, "Kiran", True, 10.6, "Krishna",10]  
print(list2[1])
#Output -  Kiran

# List slicing 
print(list2[1:3])

#List Methods 
# count()  - total number of occurence

print(list2.count(10))

# 9:40 