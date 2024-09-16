a, b = 3.5, 3.5
print(id(a))
print(id(b))
#same address


c, d = 3+7j, 3+7j
print(id(c))
print(id(d))
#same address


c, d = 3+7j, 3+4j
print(id(c))
print(id(d))


num1 = 3
num2 = 3
print(id(num1))
print(id(num2))
#same address


print(bool(0))  #False  (default value of int)
print(bool(0.0)) #False   (default value of float)
