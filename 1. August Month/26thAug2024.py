string = "20"
print(int(string))

string = '20.0'
print(float(string))

string = "2+4j"  #If you give space 2 +4j  (it will give error)
print(complex(string))

string = "False"
print(bool(string))  #True (it checks for the default value)

string = "kiran"
print(list(string))  # ['k', 'i', 'r', 'a', 'n']  
print(tuple(string)) # ('k', 'i', 'r', 'a', 'n') 
print(set(string))  # {'i', 'r', 'a', 'n', 'k'}
# print(dict(string))  ValueError: dictionary update sequence element #0 has length 1; 2 is required

items = [10,20,30]
# print(int(items))
# print(float(items))
# print(complex(items))

print(bool(items))  # True
print(list(items))  # [10, 20, 30]
print(tuple(items))  # (10, 20, 30)
print(set(items))  # {10, 20, 30
print(str(items)) #   
print(dict(items))