dict1 = {"name": "Kiran", "rollno": 34, "add": "Bangalore"}
print(dict1["name"])

#copy() - It creates a shallow copy of the dictionary.
copydict1 = dict1.copy()
print(copydict1)
print(copydict1["name"])

#clear() - It clears the dictionary. Empty flower bracket will be left. 
copydict1.clear()
print(copydict1)   #{}

#keys() - It returns the list of keys. 
result = dict1.keys()
print(result)

#values() - It returns the list of values. 
result = dict1.values()
print(result)

# items() - It returns a list of tuple. Where each element of tuple will be key value pair. 
result = dict1.items()
print(result)



#New Dictionary
dict2 = {"EmpId": 34, "EmpName": "Kiran Kumar"}

# Creating a shallow copy 
copy_dict2 = dict2.copy()
print(copy_dict2)

#Clearing the Dictionary
copy_dict2.clear()
print(copy_dict2)

#Find the list of keys 
result = dict2.keys()
print(result)

#Find the list of values of keys
result = dict2.values()
print(result)

#Find the list of tuples in key value pair
result = dict2.items()
print(result)

#value at that key
print(dict2["EmpId"])

# print(dict2["Rollnu"])  #This key is not present
#Therefor give key error

print(dict2.get("Ename"))  #This key is not present, but still it will returns a None


print(dict2.get("EmpId")) #This key is present, therefore it returns the value correspondin to it.


