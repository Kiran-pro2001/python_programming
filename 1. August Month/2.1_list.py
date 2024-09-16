watches = ["titan", "sonata", "fossil", "fastrack"]  #homogenous collection
#add casio brand
watches.append("casio")
# print(result) - no need to store
print(watches)

watches_copy = watches.copy()
print(watches_copy)  # their address is not same

watches_copy.clear()
print(watches_copy)  # [] - Empty List - Default Value



shoes = ["Nike", "Puma", "Campus", "Adidas","woodland","bata", "Puma", "puma"]
result = shoes.count("Puma")
print(result)
result = shoes.count("puma")
print(result)  # 1 - since it's a case sensitive
result = shoes.count("kiran")
print(result)  # It gives you 0. 



countries = ["Switzerland", "Canda", "USA", "India", "China"]
#Remove a country
countries.remove("Switzerland")
print(countries)


cartoons = ["Tom and Jerry", "Doraemon","Sinchan","Ninja Hoatoori", "Pink Panther"]
your_cartoons = ["Chota Bheem", "Ben 10"]
# your_cartoons.append()
#append
#extend
#insert


list1 = [34, "kiran", 33.4]
print(list1)

name = "pankaj"
list2 = [22, "kunal", 45.23, 3+4j , [1,2,3,4], name, True,"False"]
print(list2)

#Nested List
bikes = ["BMW","Kawasaki",["Scotty","Activa"],"BMW"]
print(bikes)
print(bikes[0])
print(bikes[2])
bikes.append("23")  #append will add at the end, and return type is none.
print(bikes)


#copy function - copy the original list - we need to store in a variable
bikes_copy = bikes.copy()
print(bikes_copy)

#clear - removes all the element? - is removes permanenet? It has return type is None
bikes_copy.clear()
print(bikes_copy)   #Empty list will be there


#Default value of list is?

#count - how many times an occurence of an element. It has a return type
count_of_element = bikes_copy.count("BMW")
print(count_of_element)  #It will return interger value


# remove - it removes an item from a particular index - return type is None.
