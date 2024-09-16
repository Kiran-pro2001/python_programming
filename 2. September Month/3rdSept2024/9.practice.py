# In the given code, the ‘if‘ block is executed even if the age is 0. Because the precedence of logical ‘and‘ is greater than the logical ‘or‘.


# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:         # DOUBT -- where is the difference?
	print("Hello! Welcome.")
else:
	print("Good Bye!!")

# Hello! Welcome.

    
    
# Hence, To run the ‘else‘ block we can use parenthesis( ) as their precedence is highest among all the operators.

# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if (name == "Alex" or name == "John") and age >= 2:
	print("Hello! Welcome.")
else:
	print("Good Bye!!")
 
# Good Bye!!






# Operator Precendenc - 

# result = 2+3*4 **2 - (5//2)

# 5//2 - floor division - integer value -- 2

# 2+3*4**2-2
# 2+3*16-2
# 2+48-2
# 48
