'''
# What is Typecating?
Typecasting is a method to convert one type of data type to another data type.

as we know, we have many types of data types
single value data type - int, float, complex, boolean
multivalue data type - list, tuple, set & dictionary

now, to convert int to float - we use float() function.
now, to convert float to int - we use int() function.
to convert any data type to boolean, we use bool()



'''

num1 = 10
print(bool(num1))  #True
print(float(num1))  #10.0
print(complex(num1))  #10 + 0j
# print(list(num1))  #it gives error, since we can't convert int to list. We can't convert single value to multivalue

list1 = [1,2,4]
list2 = [2,3,5] 
print(list1 + list2)
# print(list1 - list2)  #it will give error 

# print(list1 * list2)  #it will give error  - can't multiply
# print(list1 / list2)  #it will give error
# print(list1 // list2)  # it will give error 
# print(list1 % list2) #it will give error


# So the conclusion is, On lists we can only perform addition operator. Other then addition, we can't perform any operation. 


set1 = {1,2,3}
set2 = {2,3,5}
# print(set1 + set2)   - It gives error. 
print(set1 - set2)  #It gives error.  (It do set difference - A- B)
# print(set1 * set2)  It gives error. 
# print(set1 % set2)  #It gives error. 
# print(set1 / set2)  It gives error.
# print(set1 // set2 )  It gives error 
# print(set1 ** set2) It gives error


dict1 = {"name": "Kiran"}
dict2 = {"name": "Kunal"}
# print(dict1 + dict2)  - It gives error 
# print(dict1 - dict2)  - It gives error
# print(dict1 * dict2) - It gives error 
# print(dict1 / dict2)  - It gives error
