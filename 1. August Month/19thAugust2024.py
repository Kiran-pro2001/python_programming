print(True and True)  # True (Since and is looking for default values or false values)
# (If and got the default values, it returns the values 
# and if got the false values, it returns that)


print(False and 0.0 and 1.0)  #False  (Because in the first one only it get the false value)

print(1.0 or 0.0 or 0)  #1.0  - Because or sees for the non default values, if it gets it then returns that value, if it doesn't get it till the end, it will returns the last value.

print( [] or {} or 1.0 )  #1.0  - since or will go for non default values. [] or {} are the deafault values 

print( True or 12.0)  #True

# Bitwise Operator  - We perform operation bit by bit. 

print(bin(10))   #0b1010
print(bin(20))  #0b10100

print(20 & 10)  #Bitwise AND   -  0
print(20 | 10)  #Bitwise OR -   30
print(~10)  #Bitwise NOT  ( -(10+ 1) )  =   - 11
print(20 << 1)  #Bitwise Left Shift, first convert the 20 to it's binary form, and then add this much zero as second operator to the right of the  binary form for 20.
# 10100  0  (you addede one zero at here) 

print(int(20) >> int(1))  #Bitwise OR , first convert the 20 to binary form, then as much the second operator is that is 1, cut the binary form from right side.
# 10100  now second operator is 1, therefore cut one timce from the right side
# 1010 is left. Which is equal to 10. 



#Logical Operators - and, or, not.

print((2>4) and (5<9))
print( [1,24,3] <= [24.0, 3.0, 1])  #False - since in list, order is important. 

print({1,2} <= {1,24,3,4})



print(not False)

