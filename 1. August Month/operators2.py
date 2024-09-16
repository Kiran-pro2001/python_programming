num1 = 2 
num2 = 5
#Arithmetic Operator
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1**num2)
print(num1//num2)
print(num1/num2)

#Assignment Operator
name = "Kiran"
name += "Kumar"
print(name)

result = "Kiran"  + " " + "Kumar"  #Concatenation
print(result)

num1 = 10
num1 += 20
print(num1)

num2 = 20
num2 -= 10
print(num2)

num3 = 30
num3 *= 2
print(num3)

num4 = 40
num4 /= 2  # num = num / 2 ---  40/2 --- 20.0 (Float Value)
print(num4)

num5 = 40
num5 //= 4  #num5 = num5 // 4 -- 40//4 -- 10 (Integer Value)
print(num5)


num6 = 3
num6 **= 2  # num6 = num6 ** 2 -- 3 to the power 2
print(num6)



#Comparison Operator / Relational Operator
# (==, !=, >, <, >=, <=)
print(10 == 10)
print(10 == 10.0)
print(10 > 2)
print(5>= 3)
print(20 <-10)


# Operations performed on Collections 

list1 = [1,2,3,5]
list1 += [1,2,3]  #Addition will be there on the smae order.
# list1 -= [1,2]   - We can't perform substraction on list
print(list1)

list2 = [21,"kiran", 4+5j, 5.6]
list2 += ["kumar", 45, 6+45j ,True] #additions will be on the same order. 
print(list2)
# List also supports homogenous & hetrogenous


tuple1 = (1,4,5,8)
tuple1 += (3,5,2)
print(tuple1)



tuple2 = (1,[3,4],"kiran") #We can put homogenous & hetrogenous.
tuple2 += (2, 4, "kumar")
print(tuple2)



#Opeations on Dictionary 
dict1 = {"name": "Kiran",
         "rollno": 34,
         "class": "BTech CSE"}
print(dict1["name"])
print(dict1["rollno"])
print(dict1["class"])
#if that key is not present, it will give error.

#if you are 100% sure that, that key is presnt, then use directly the key.
#if youa re not 100% sure wether the key is present or not. Then go for get function (get())

result = dict1.get("name") #if that key is present, then it will return the value corresponding to it. If that key is not present, then won't give error.
print("####")
print(result)
#if that key is not present, then it won't give you error.
result = dict1.get("adddress") #address key is not present, hence won't give you error. It will give you None.
print(result)  #None


new_dict = dict1.copy()
print(new_dict)

new_dict.clear()
print(new_dict)

result = dict1.keys()  #returs the list of keys
print(result)

result = dict1.values() #returs the list of values corresponding to that key
print(result)

result = dict1.items() #list of all tuples, and the element of list will be key value format.
print(result)

#I want to add other key value pair, I want to take another dictionary as an argument. 
# Use  update() function

print("Update Function ")

dict01 ={"name": "Kiran"}
dict02 = {"address": "Bangalore"}
# result = dict01.update(dict02) - Give None, since return type of update() is none.
dict01.update(dict02)
print(dict01)


# pop() function 
dict03 = {"name": "Kiran", "status": "In Relationship"}
print("pop pop pop")
dict03.pop("name")  #atleast one argument is needed.
print(dict03)



#popitem() function
dict04 = {"hobbies": "Knowledge", 
          "pasion": "Knowledge"}
# dict04.popitem()  #remove it from the last
print(dict04.popitem())
print(dict04)

dict05 = {"school": "KVS",
          "class": "12th"}
#Now I want to remove a key value from the last
# popitem() will be use - it will remove it from the end, and there is not need to assign to some variable. 
# directly print it

print(dict05.popitem())  #This will automatically remove the key value pair form the end. 
print(dict05)  #Last key value will be removed, only the first key value will be left



# But what about, if I need to remove the element at particular key, then use pop() function, atleat one agrument is needed.

dict06 = {"name": "Kiran Kumar"
          , "networth": "50000 Crores"}

# Now I want to remove the key value pair at particular address 
# Use pop() function, and atleast one argument we need to pass.  No need to print it. Just use pop() function

dict06.pop("networth")  #networth key value pair is removed, now to see, print the dict06
print(dict06)

dict06.pop("name")  # That name key value pair is removed, to see print the main dictionary
print(dict06)



#The default value of dictionary is {} - Empty flower brackets