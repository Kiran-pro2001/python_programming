
num1 = 10
print(type(num1))  #int

print(float(num1))      #10.0
print(complex(num1))  #10+0j
print(bool(num1))  #True

# print(list(num1))  #Error
# print(tuple(num1)) #Error
# print(dict(num1)) #Error
# print(set(num1)) #Error


num2 = 10.0
print(type(num2))  #float
print(int(num2))  #10
print(complex(num2))  #10 + 0j 

# print(list(num2))
# print(tuple(num1))
# print(set(num1))
# print(dict(num1))

num3 = 15.5
print(complex(num3))  #15.5 + 0j
print(bool(num3))  #True

num4 = 0.0
print(bool(num4))  #False (Because for default value, it returns False )

num5 = 23
print(type(num5))
print(int(num5))  #23
print(bool(num5)) #True
print(complex(num5)) #23+0j
print(float(num5))  # 23.0


num4 = True
print(type(num4))
print(int(num4))  # 1
print(complex(num4)) #1 + 0j
print(float(num4))  # 1.0
# print(list(num4))   - It gives error 


list = [1,2,3,4]
print(type(list))  #<class 'list'>
print(bool(list))  #True
print(str(list))  # "[1,2,3,4]"
print(set(list)) # {1,2,3,4}