# Formatted strings (f-strings) in Python are used to embed expressions within string literals, making it easier to create dynamic and formatted strings in a readable and efficient manner.

# F-strings (formatted string literals) in Python are a way to embed expressions inside string literals, using curly braces `{}`. They were introduced in Python 3.6 and offer a concise and readable way to include variables and expressions inside strings.

name = "Kiran"
age = 23
# print("Hi, My Name is {name}")  #Hi, My Name is {name}
print(f"Hi, My Name is {name}, I am {age} years old.")  # Using fsting  - make it easy
print("Hi, My Name is " + name+ ", " + "I am " + str(age) + " years old.")  #Using Concatenation


num1 = 10
num2 = 20
print(f"{num1} + {num2}")
print(f"{num1+num2}")

fruits = ["apple", "mango", "grapes"]
print(f"I like {fruits[1]} and {fruits[2]}")

fname = "Kiran"
lname = " Kumar"
name = fname + lname
print(fname + lname)
print(name)
print("My name is " + name + ". I am the greatest person ever born on this planet.")
print("My name is " + name + ". " + "I am the greatest person ever born on this planet.")




""" All will have the same address """
num1 = 2
print(id(num1))  #Same Address
num1 = 2
print(id(num1))  #Same Address

num1 = 2
print(id(num1))  #Same Address
num2 = 2
print(id(num2))  #Same Address



x = 10
y = 10
z = 10
print(id(x), id(y), id(z))  #Same Address


a,b = 10,10
print(id(a), id(b))  #Same Address



# Odd & Even Program

# num = int(input("Enter a number ? "))
# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")



num1 = 10
print(num1)
print(type(num1))
print(id(num1))




'''
In Python, consistent indentation is crucial within the same block of code. Python uses indentation to define the " scope and structure " of the code, such as determining which lines belong to a particular loop, function, or conditional statement.

Using different indentation styles (e.g., mixing spaces and tabs or varying the number of spaces) within the same block will lead to an IndentationError. For example:

def example_function():
    if True:
        print("This is indented with four spaces")
        print("This is also indented with four spaces")
     print("This line has inconsistent indentation and will cause an error")
     
     
     
     
     
     
     
     
     +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     
     
     
     
     
For Loop Vs While Loop 


In Python, both `for` and `while` loops are used for repeating a block of code, but they work in different ways and are suited for different scenarios.

### **For Loop**
- **Purpose**: The `for` loop is typically used when you know in advance how many times you want to iterate over a sequence (like a list, tuple, string, or range).
- **Structure**: It iterates over each element in a sequence, one by one.

**Example**:
```python
# Iterating over a list with a for loop
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```
**Explanation**:
- The `for` loop here will iterate over each element in the `numbers` list, printing each one.

### **While Loop**
- **Purpose**: The `while` loop is used when you want to repeat a block of code as long as a condition is true. It's more flexible but requires careful handling to avoid infinite loops.
- **Structure**: It continues to execute as long as the condition evaluates to `True`.

**Example**:
```python
# Counting down with a while loop
count = 5
while count > 0:
    print(count)
    count -= 1
```
**Explanation**:
- The `while` loop will continue to execute as long as `count` is greater than 0. After each iteration, the value of `count` is decreased by 1.

### **Key Differences**
- **Iteration Control**:
  - `for` loop: Iteration is controlled by a sequence (e.g., list, range).
  - `while` loop: Iteration is controlled by a condition.
  
- **Use Cases**:
  - Use `for` when the number of iterations is known or you are iterating over a sequence.
  - Use `while` when the number of iterations is unknown and depends on a condition.

- **Risk of Infinite Loops**:
  - `for` loop: Generally safer, as it automatically stops after iterating over the sequence.
  - `while` loop: Requires careful management of the condition to avoid infinite loops.

Both loops are powerful tools in Python, and choosing the right one depends on the specific needs of your code.


'''