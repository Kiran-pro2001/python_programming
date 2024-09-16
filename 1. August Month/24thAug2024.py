# Typecasting on Multipvalue Variable 


# Tyepcasting on Complex variables

compl1 = 8 + 2j
print(bool(compl1))  #True
print(str(compl1))  # '8+2j
# print(int(compl1))  # Gives Error 
# print(float(compl1))  Gives Error
# print(list(compl1))  Gives Error
# print(tuple(compl1))  Gives Error



string = "2"  # string of integer --therefore we can convert it into integer
print(int(string))  # 2


string = "3.0"  # string of float -- therfore we can conver in into float 
print(float(string)) # 3.0

string = "True"   # Bydefault value of string is "", but here something is there, so it is non default. 
# bool of bydefault value is True
# bool function check for default value & non default value 
print(bool(string))  # True


string = "1+7j"  # complex we can convert , but if there is a gape in between operator, then get error
print(complex(string))  

string = "1 + 7j"  # complex we can convert , but if there is a gape in between operator, then get error

# print(complex(string))


string = "kiran"  # string multi value, therefore  we can convert to multivalue 
print(list(string))
print(tuple(string))
print(set(string))
# print(dict(string)) - not possible 

# num1 = 1.3
num1 = "1.3"
print(list(num1))








# Complex  

complex1 = 2 + 7j    # when store to complex, it removes the space while storing...   2+7j
print(bool(complex1))  # True
print(str(complex1))  # '(2+7j)'


# Following gives Type Error 

# print(int(complex))   #because imaginary part we can't convert

# print(float(complex))

# print(list(complex))  #because complex1 is a single value, we can't convert to multi value.
# print(tuple(complex))
# print(dict(complex))
# print(set(complex))






string = "2 + 7j"   # while storing to string, it considers the space as well. 
# print(complex(string))   # it gives error 

string1 = "1+7j" #no space, it gets stored to string
print(complex(string1))  # (1+7j)







# Practice Match 

