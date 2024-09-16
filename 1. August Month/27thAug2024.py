items = (10,20,30)
#Can't convert to int,float & complex
# print(int(items))
# print(float(items))
# print(complex(items))


print(bool(items))  #Checks for the default value and non default value (True)
print(str(items)) # [10, 20, 30]
print(type(str(items))) #str
print(list(items))
print(set(items)) #not have mutable data types or duplicate value
# print(dict(items)) # nested collection of length 2         m



# To make it dictionary 
items = ({2,3},"cd",("a",23))
print(dict(items))  # {2: 3, 'c': 'd', 'a': 23}

items1 = ("ab", ["ab",23])
print(dict(items1)) # {'a': 'b', 'ab': 23}   

items2 = (10,20,30,40)
# print(dict(items2))  #It gives error - because to convert to dictionary, there has to be nested collection of length 2
# print(int(items2))
print(bool(items2))  #True
# print(complex(items2))  TypeError
# print(float(items2))




set = {1,2,4,5}
# print(int(set))
# print(float(set))
# print(complex(set))
print(bool(set))  #True  (Because it checks for default value & non default value )
print(str(set)) # '{1, 2, 4, 5}'
print(list(set))  # [1, 2, 4, 5]
print(tuple(set))  #  (1, 2, 4, 5)

# print(dict(set)) - Gives Error



items4 = {10,"string",9.5, (10,20)}
print(list(items4))  # [9.5, 10, 'string', (10, 20)]
print(list(items4))  # [9.5, 10, 'string', (10, 20)]
print(list(items4))  # [9.5, 10, 'string', (10, 20)]
print(list(items4))  # [9.5, 10, 'string', (10, 20)]

# [9.5, 10, 'string', (10, 20)]
# [9.5, 10, 'string', (10, 20)]  
# [9.5, 10, 'string', (10, 20)]


# ['string', 10, 9.5, (10, 20)]
# ['string', 10, 9.5, (10, 20)]
# ['string', 10, 9.5, (10, 20)]
# ['string', 10, 9.5, (10, 20)]

#Every time we will get the different outputs 



# Dictionary to other data types 


dict1 = {"name":"Kiran", "age": 23, "Qualification": "BTech CSE"}
# print(int(dict1))
# print(complex(dict1))
# print(float(dict1))  

# str to float 

str1 = "10"  #Inside the string, integer is there 
print(int(str1)) # So, we can convert to integer  - 10
print(float(str1)) # 10.0

str2 = "10.0"
# print(int(str2))  
print(float(str2))  # 10.0
