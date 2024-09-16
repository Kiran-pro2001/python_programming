#Python - It's a proramming language. 

# Datatypes - Single value & Multi Value (Collections)
# Single Value is further converterd to two parts - 1. Numeric Data Type   2. Boolean Data Type
# Numeric Data Type - Integers, Float, Complex.
# Boolean Data Type - True , False
# Multivalue Data Type - Strings, List, Tuple, Set & Dictionary.

# Integers  - Which store only the whole numbers (including negative numbers)
# Combination of +ve, -ve, 0 numbers is called Integers (excluding float values)

num1 = 34
print(num1)

num2 = 34343
print(num2)

#Single Value Data Type means - One Variable stores only the one value.
#Multi Value Data Type means - For a single variable, it can store multi values.

num1, num2 = 2,4
print(num1, num2)
print(id(num1), id(num2))  #both will be having different address.

num3, num4 = 2, 2
print(id(num3), id(num4))  #Both will be having the same address

num5 = 3
num6 = 3
print(id(num5), id(num6))   #Both will be having the same address (Since Python will work in such a way that, it can use effective way of memory)


num7 = 10
num8 = 343
print(id(num7), id(num8))  #Now it will be having a different address


# num1, num2, num3 = 1, 2
# Gives error  - since LHS has to be equal to RHS



# Float 
num1 = 3.4
print(num1)

num1 = 3.4 + 1.6
print(num1)  #5.0

num2 = 5.0
print(num2)  #5.0

print(2 == 2.0)  #True

print(3 == 2.9999999999999999)  #After one limit, it gives True.  Output is - True

print(3 ==  2.9999 )  #False



# Python Set - Questions Practice 

print("Practice Practice Practice")

set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}

# A) Is set1 a subset of set2   
print(set1.issubset(set2))  #False

# B) Is the intersection of set1 and set3 is empty?
print(set1.intersection(set3))  # No

# C) What is the result of performing set union on set1 and set2?
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 8}

# D) What is the result of performing set intersection on set2 and set3?
print(set2.intersection(set3))  #set()  - Null set

# E) What is the result of performing set intersection on all three sets?
print(set1.intersection(set2).intersection(set3))     #Is that is fine #######################

# F) What is the result of performing the set difference on set1 and set2  (set1 - set2)?
print(set1.difference(set2))

# G) What is the result of the instruction set1.discard(5)?

print("To seee............")
# print(set1.discard(5))  #returns that element and the remove it from the set
# set1.discard(5)  #
print(set1.discard(5))


# H) What is the result of the instruction  set2.discard(5)?
# print(set2.discard(5))  #None
set2.discard(5)



print("#############################################################")


# Tuples - Immutable, homogenours & hetrogenous, Duplicate, Ordered. 
# Same elements that we can store in list, that we can also store in tuple. 
# Tuples are the collection of elements, separated by comma & enclosed in a parenthesis.
# Dekh bhai, List and tuple both are same....jo ham list me store kar sakate hai...wahi same tuple me kar sakte hai...only the difference in list is mutable, it means we can change the original structure, we can add & remove element from the list. But tuple is immutable, we can't change the original structure of the list. Althought we can override it. Overriding is different, it is like you are breaking the bond and connecting a new bond -- to that particular address.

# Properties of tuple - 1. Homogenour & Hetrogenous   2. Ordered   3. Slicing & Indexing   4. Duplicate Values   5 Immutable. 

# There are only two functions in Tuple  - 1. count   2. index 
#Both function we need to store in a variable. 

tuple1 = [1, 2, 4, 5+7j, 4.5, True, [1,24,5.6],1, (1,3), {"name": "Kiran"}, "kiran"]
print(tuple1)

result = tuple1.count(1)
print(result)  # 3 - Because 1, 1 & it is taking True as 1.


result = tuple1.index(2)
print(result)  # it returns the index of element 2, and it should consider only the first occurrence.


# We can't change the tuple
# same as list

tup = (1, 5, 6)
print(type(tup), tup)


tup1 = (1,2,4, 3+5j)
print(tup1, type(tup1))


tup = (1)   # It is not a tuple, it's an integer.
print(tup, type(tup))

# If you want to create a tuple of one element, then comma is necessary.  *****

tup = (1,)
print(tup, type(tup))

set = {1}
print(set, type(set))  # set

list = [1]
print(list, type(list))  #list

list = ["1"]
print(list, type(list)) #list

# Tuples are unchangeable, meaning we can not alter them after creation. 


tup1 = (1, 4, 3)
# Now, I want replace 4 by 2. Or I want to put 2 at the index number 1.
# tup1[1] = 2
# print(tup1)  #Gives Error - TypeError: 'tuple' object does not support item assignment

#What if that is a list, then we can do it.

list = [1,2,3]
list[0] = 23  # I am adding element 23 at 0th index.
print(list) # [1,23,3]

#When we want ki ham ek list bane but usme change nahi karna chahte ...then go for tuple


tup = (1, 2, True, 3+9j, 3.4)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
# print(tup[90]) # - comes error, because that index is notj present
print(tup[-1]) 

print(len(tup))

if 2 in tup:
    print('True')
    
    
    
# We can do slicing in Tuple, uplon slicing new tuple is returned.
# tup remains the same, new tuple is created 

print("Tuple Slicing")

tup = (2,3,45,53,343)
# tup2 = tup[2,4]    Tuple   - wrong syntax  It should be,     tup2 = tup[2:4]  - colon will be there
tup2 = tup[2:4]  #index 2 to 4, excluding 4th index.
print(tup2)       #(45,53)

print(tup[:])  # Oth index to lenght of index  - Therefore full tuple gets printed.
print(tup[:3])  # 0th index to 5th index, excluding 5th index.

# Ek bar aapne tuple bana diya to uski length ko change nahi kar sakte, us existing tuple me change nahi kar sakte. New tuple create kar sakte hai. 

# Tuples are immutable.
# Strings are immutable. 
# Lists are mutable. 

#tupleme slicing karne se vo tuple change nahi hota...new tuple return karta hai

# We can't add & remove elements from a tuple. If I want to, then we need to convert tuple to list, and then add elements, and then again convert to lists. 


# count() function & index() function

tup = (1,2,3,2,1,4)
print(tup.count(2)) # 2
print(tup.index(2))


# Tuple methods - count & index
# count() function - returns the number of times an element appears in a tuple.
# index() function - returns the index of the first occurrence of an element in a tuple.

# count function & index function are the only two functions that tuple have 
# Tuple are immutable - we can't change the existing tuple, but we can create new tuple. 
# If we add two tuples, that is fine. Since, we are creating new tuples.

tup1 = (21,32,2323,True)
tup2 = (232, 132413, 5+8j, False, (2,343))
# print(tup1+tup2)  It's a new tuple we created

tup3 = tup1 + tup2  #concatenation of tuples
print(tup3)

#(21, 32, 2323, True, 232, 132413, (5+8j), False, (2, 343))



tup1 = (2,34,3,5+7j, False, (2,3,5), 3.5, "Kiran", [1,2,4], {"name": "Kiran"}, {1,2,4})

set1 = {"a", "b", "c"}  #Put characters into double quotes
print(type(set1)) #set

dict1 = {"name": "Kiran", "rollnu": 23}
print(type(dict1)) #dict




# copy() and clear() , these two functions are in dictionary & set both.
# copy() functions create a shallow copy of the original set or dictionary.
# clear() functions clear the whole set or dictionary, No need to store, For set it give set() and for dictionary it give {}



set1 = {1,2,3}
copy = set1.copy()
print(copy)

copy.clear()
print(copy)  # set()

dict1 = {"name": "Kiran", "rollnom": 23}
copy = dict1.copy()
print(copy)

copy.clear()
print(copy)  #{}

# Lists, Tuples & String are orderd.
# Dictionary 

# print("Kiran Kumar")
# name1 = input("Enter your name?")  # Kiran Kumar
# print("My name is",name1) # My name is Kiran Kumar



# To take input as an integer

# var1 = int(input("Enter the first number?"))
# print("My First number was :",var1)

# var2 = int(input("Enter the second number? "))
# print("My Second number was : ",var2)

# print("Arithmetic Operation - (+,-,*,/ (True Division),// (Floor Division), % (Modulo Operator), )")

# print("Performing Addition Operation")
# print("The sum of var1 & var 2 is ", var1+var2)

# print("Performing Substraction Operation")
# print("The substraction of var1 & var2 is", var1-var2)

# print("Performing Multiplication Operation ")
# print("The substraction of var1 & var2 is ",var1 * var2)

# print("Performing True Division or Division Operation") #True division always returns the float value
# print("The Division of var1 & var2 is", var1 / var2) #True Division

# print("Performing Floor Division on var1 & var2 ")  #Floor Division always returns the integer value, It returns the quotient. 
# print("The floor division of var1 & var2 is", var1//var2) #Floor Division

# print("Performing Modulo Operation on var1 & var2")
# print("The Modulo Operation on var1 & var2 is", var1 % var2) #It returns the remainder. 

# print("Performing Power of Operation on var1 & var2")
# print("The power of (**) operation on var1 & var2 is  ", var1**var2) #Power of



#Assignment Operator (+=, -+, *=, /=, //=, %=, **=)

num = 10
# print(num += 10)   -Why this is giving error?

num += 10  # + & = dono sath hi sath honge, beech me koi bhi gap nahi hoga.  (+= is right,  + = is wrong)
print(num)

# print( num -= 10)  # invalid synatx  - It means in side the print, the short hand won't work


# print( num = num - 10)  # TypeError: 'num' is an invalid keyword argument for print()
# It means, inside the Python is not able to understand what the num is?



num1 = 10
# num1 += 20
# print(num1)   #num1 = 30

# num1 -= 10
# print(num1)  #num1 = 20


# num1 *= 10
# print(num1)  #num1 = 200

# print("######")
# num1 /= 10  # It returns only the float value, therefor num1 = num1 / 10 --- 10/10 ---- 1.0  (But keep in mind, above all updation (+= & -= comment it, otherwise updated value gonna used for num1))
# print(num1) 

# num1 //= 10  #Always returns the integer value, Therefore  num1 = num1 // 10 = 10//10 = 1
# print(num1)

num1 **= 10
print(num1)




# Arithmetic Operator (+,-,*,/,//,%,**)  - 7
# Assignment Operaotr (+=, -=, *=, /=, //=, **/, %=) - 7

# Comparison Operator (==, !=, >,<, >=, <=, ) - 6  (It always returns the Boolean Values)

print(2==2)  #True
print(2==2.0)  #True
print(2 != 3)  #True
print(2<4)  #True
print(3>1)  #True
print(3>=3)  #True
print(3<=4)  #True



# There are three types of Operators in Python
# Arithmetic Oprator, Assignment Operator, Comparison Operator

#So, the conclusion is....
# There are 3 types of operators in Python
# 1. Arithmetic Operator ( +,-, *,/,//, %, **) (True Division, Floor Division, Exponent Of) - 7 Operators
# 2. Assignment Operator ( +=, -=, *=, /=, //=, %=, **=)  # 7 Operators
# 3. Comparison Operator ( ==, !=, <, >, <=, >=, )  # 6 Operators  - It always returns a Boolean value.


# What are Operators?
# Operators are the special symbol which are used to do arithmetich & mathematical operation. 

tup = (1,24, True, "kiran", 2.45, (34, "kumar"), {"name": "kiran"}, {1,2,"kiran"})
print(tup)


# Tuple is same as list, whatever element we can put into a list, we can also put in tuple. But there is a difference  between that, the difference is that, tuple is immutable, It means once the tuple is created, we can't change the orignal structure of the tuple, we can't change the existing tuple. We can crete a new tuple. 

# tup[4] = "kiran"  # Adding element into a tuple will give error.  #TypeError: 'tuple' object does not support item assignment
# print(tup)

# But if we want to change the tuple, then we need to first convert to list, and then we need to update values into a list, then convert it into a tuple.

tup = (1,2, 3)
# list1 = list(tup)  #type conversion of tuple to list    #Is that is fine!!!?
# print(type(list1))
# # Now append elements into it
# # list1.append(2)
# # print(list1)


for i in range(0,101,2):
    print(i)  # Automatically it gonna print into new line. \
        
        
# Indexing in Lists 

list1 = [1,2,3,4,True, 3+7j, 5.6, "Kiran"]
new_list = list1[0:4]  # It will slice the list, and returns a new list - [1,2,34] - From 0th index to 3rd index.
print(new_list)

tupl1 = (23, True, "Kumar", 34.22)
new_tup = tupl1[1:3]
print(tupl1)


# List & Tuple do slicing & indexing. As well, it also supports orderd, duplicate values. 

tup1 = (1,23,345,1)
print(tup1.count(1))  #2
print(tup1.index(23)) #At 1st index, 23 is there. 

# In tuples only two types of functions - count & index 








