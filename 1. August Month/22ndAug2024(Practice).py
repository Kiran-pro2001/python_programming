'''
Operators - special symbols or special characters which is used to perform matematical operations.
Operators are the special symbols or special characters which are used to perform some matematical operations.

In Python, there are 6 types of Operators.
1. Arithmetic 2. Assignment  3. Comaprison Operators  4. Logical Operators  5. Bitwise Operators.  6. Special Operators 

1. Arithmetic Operators (+,-,*,/ (True Division), // (Floor Division), ** (Exponent Of), % (Modulus Operator))
2. Assignment Operators (=, +=, -=, *=, /=, //= , %=, **=)
3. Comparison Operators. (==, !=, >, >=, <, <=)
4. Logical Operators. (and, on, not)
5. Bitwise Operators. (&, |, )
6. Special Operators.

'''



# Special Operators 
"""

1. Identity Operator -  Is, Not Is.
2. Membership Operator - In, Not In

"""


list1 = [1,2,4]
list2 = [1,2,4]

# list is mutable - therefore their addresses will be different
print(type(list1))
print(type(list2))
print(id(list1))
print(id(list2))

#Both lists have difference addreses.

print(list1 is list2)   #Now, is operator sees the value, data type & address.
# hence the list is mutable, therefore the addresses will be differenct. Hence, is operator gives false



tup1 = (1,23,4)
tup2 = (1,23,4)

print(type(tup1))
print(type(tup2))

print(id(tup1))
print(id(tup2))

#Tuple is immutable, hence both will be having the same addresses.


tup3 = (23,24,1)
tup4 = (343,343,23)

print(type(tup3))
print(type(tup4))
print(id(tup3))
print(id(tup4))
# tuples having different values, then already different adreses will be there.

print(True is True)  #True
print(1 is True) #False (Different Data Types)

print(1.0 is 1.0)  #Same data type, same value, float --immutable----therefore same address    #True


#Frozenset -- same as tuple only. ??

'''
Not exactly. While both frozenset and tuple are immutable data structures in Python, they have some key differences:

Unordered vs. Ordered: A frozenset is an unordered collection of unique elements, whereas a tuple is an ordered collection of elements. This means that the order of elements in a frozenset is not preserved, whereas the order of elements in a tuple is preserved.

Set Operations: A frozenset supports set operations like union, intersection, and difference, whereas a tuple does not.

Membership Testing: A frozenset has fast membership testing, meaning you can quickly check if an element is in the set or not. A tuple also has membership testing, but it's slower because it has to iterate over the entire tuple.

Hashability: A frozenset is hashable, meaning it can be used as a key in a dictionary or as an element in another set. A tuple is also hashable, but only if its elements are hashable.

Here's an example to illustrate the differences:

python
Edit
Copy code
# Create a frozenset and a tuple
fs = frozenset([1, 2, 3, 2, 1])  # duplicates are removed
t = tuple([1, 2, 3, 2, 1])  # duplicates are preserved

print(fs)  # Output: frozenset({1, 2, 3})
print(t)  # Output: (1, 2, 3, 2, 1)

# Set operations
fs2 = frozenset([3, 4, 5])
print(fs.union(fs2))  # Output: frozenset({1, 2, 3, 4, 5})
print(fs.intersection(fs2))  # Output: frozenset({3})

# Membership testing
print(2 in fs)  # Output: True
print(2 in t)  # Output: True

# Hashability
d = {fs: "hello"}  # works because fs is hashable
# d = {t: "hello"}  # would work if t's elements were hashable
In summary, while both frozenset and tuple are immutable, they have different use cases and characteristics. frozenset is suitable when you need an unordered collection of unique elements with fast membership testing and set operations, whereas tuple is suitable when you need an ordered collection of elements.





'''


print("Hello"*8)

breakfast = "idli"
breakfast += "dosa"
print(breakfast)  # idlidosa