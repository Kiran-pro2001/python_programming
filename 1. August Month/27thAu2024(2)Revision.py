x = 5.6789
y = round(x, 2)  # y will be 5.68


str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # result will be "Hello World"


s = "Python"
first_char = s[0]  # 'P'
last_char = s[-1]  # 'n'

# Slicing: Accessing a substring

s = "Python"
first_char = s[0]  # 'P'
last_char = s[-1]  # 'n'

substring = s[1:4]  # 'yth'


s = "Python"
upper_s = s.upper()  # 'PYTHON'
lower_s = s.lower()  # 'python'


# Strings in Python are immutable, meaning once a string is created, it cannot be changed:

s = "Hello"
# s[0] = 'h'  # This will raise an error
# You need to create a new string instead
s = 'h' + s[1:]  # s becomes 'hello'


#A list is an ordered, mutable collection of elements:

my_list = [1, 2, 3]
first_item = my_list[0]  # 1
last_item = my_list[-1]  # 3

my_list.append(4)  # Adds 4 to the end
my_list.insert(1, "Python")  # Inserts "Python" at index 1

my_list.remove(2)  # Removes the first occurrence of 2
last_item = my_list.pop()  # Removes and returns the last item

# append() adds a single element to the end of the list:
my_list = [1, 2, 3]
my_list.append([4, 5])  # [1, 2, 3, [4, 5]]

#extend() adds all elements from an iterable (e.g., list, tuple) to the end of the list:
my_list.extend([4, 5])  # [1, 2, 3, 4, 5]

# How can you reverse a list in Python?
# Use the reverse() method or slicing:
my_list = [1, 2, 3]
my_list.reverse()  # [3, 2, 1]

# or using slicing
reversed_list = my_list[::-1]  # [3, 2, 1]



# How do you unpack a tuple into variables?

# You can assign each element of a tuple to a variable:
my_tuple = (1, 2, 3)
a, b, c = my_tuple
# a = 1, b = 2, c = 3


# Dictionary 
# A dictionary is an unordered collection of key-value pairs:

# How can you access a value in a dictionary using its key?
# Use the key inside square brackets or the get() method:
my_dict = {'name': 'Alice', 'age': 25}

name = my_dict['name']  # 'Alice'
age = my_dict.get('age')  # 25





# What happens if you try to access a key that doesn't exist in a dictionary?

# Using square brackets will raise a KeyError, while get() will return None (or a default value if provided):
# value = my_dict['non_existing_key']  # KeyError
value = my_dict.get('non_existing_key', 'default_value')  # 'default_value'



# How can you get a list of all keys or values in a dictionary?

# Use the keys() and values() methods:
keys = my_dict.keys()  # dict_keys(['name', 'age', 'city'])
values = my_dict.values()  # dict_values(['Alice', 25, 'New York'])



# == is a comparison operator. It checks if the values of two variables are equal. For example:
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True (because the values are the same)

# The "is" operator checks whether two variables point to the same object in memory 
# (i.e., it checks if they have the same identity). It does not check the data type explicitly but checks if both variables refer to the same memory location. For example:
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # Output: False (because they are different objects in memory)

print("Printing id")
print(id(a))  #differenet id
print(id(b))    #differenet id

c = a
print(a is c)  # Output: True (because both refer to the same object in memory)


# == checks if the values of two objects are equal. They are called Comparison Operator
# is checks if two variables refer to the same object in memory.





# Question 2 
# What will be the output of the following code, and why?


x = [1, 2, 3]
y = x
y.append(4)

print(x)  # [1, 2, 3, 4]
print(y)  # [1, 2, 3, 4]


# x and y are both referencing the same list object in memory because y = x creates a reference, not a copy.
# When you append 4 to y, it also affects x because x and y are pointing to the same list.




# Question 3:
# What is the difference between a shallow copy and a deep copy in Python? How do you create each one?
