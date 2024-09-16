'''LIST'''

watches = ["rolex", "fastract", "fossil", "titan", "casio"]
watches.append("sonata")
# print(watches)

watches_copy = watches.copy()
# print(watches_copy)

watches_copy.clear()
# print(watches_copy)

shoes = ["nike", "Puma", "adidas", "woodland", "puma"]
result = shoes.count("bata")
# print(result)

countries = ["switzerland", "pakistan", "india", "usa", "russia", "pakistan"]
countries.remove("pakistan")
# print(countries)


my_cartoons = ["tom and jerry", "doraemon", "ninja hattori", "spongebob", "pink panther"]

my_cartoons.insert(0, "noddy")
print(my_cartoons)


# your_cartoons = ["ben 10", "shinchan", "chota bheem", "motupatlu", "oggy"]

# my_cartoons.extend(your_cartoons)
# print(my_cartoons)
# my_cartoons.extend("micky")       #char by char
# print(my_cartoons)


superheroes = ["ironman", "jai baalayya", "shaktimaan", "black panther", "deadpool"]
result = superheroes.pop()
# print(result)
# print(superheroes)
result = superheroes.pop(2)
print(result)
print(superheroes)

animes = ["AOT", "one piece", "demon slayer", "death note", "DBZ", "naruto", "tokyo ghoul", "iq"]
# result = animes.index("DBZ", 0, 3)
# print(result)


supervillains = ["thanos", "doctor doom", "hella", "rolex", "homelander","joker"]
supervillains.reverse()
print(supervillains)

bands = ["1D", "bts", "blackpink", "maroon 5", "imagine dragons"]
bands.sort()
print(bands)








##############################################
'''TUPLE'''

drinks = "j&d", "teachers", "old monk", "imperial blue", "blenders pride", "vat69"

result = drinks.count("old monk")
print(result)
print(type(drinks))

companies = ("google", "facebook", "ms", "wipro", "amazon", "ibm", "tata")
result = companies.index("ibm")
print(result)

###############################################
#SET

supercars = {"lambo", "bugatti", "porsche","ferrari", "bujji", "mustang", "ferrari"}
supercars.add("aston martin")
print(supercars)

supercars_copy = supercars.copy()
print(supercars_copy)
supercars_copy.clear()
print(supercars_copy)

games1 = {"gta", "far cry", "god of war", "assassins creed"}
games2 = {"fifa", "cricket 2007", "mario", "gta", "free fire"}

result = games1.union(games2)
print(result)

result = games1.intersection(games2)
print(result)

result = games1.difference(games2)
print(result)

result = games1.symmetric_difference(games2)
print(result)

fruits = {"mango", "strawberry", "apple", "pomogranate", "orange", "grapes"}
# fruits.remove("dragon fruit")     #error
# print(fruits)
fruits.discard("dragon fruit")
print(fruits)
print("tata")

junkfoodchains = {"kfc", "mcd", "dominoes", "bk", "pizzahut", "tacobell"}
result = junkfoodchains.pop()
print(result)
print(junkfoodchains)



set1 = {10, 20, 30}
set2 = {30, 40, 50}
# set1.update(set2)
# set1.intersection_update(set2)
# set1.difference_update(set2)
# set1.symmetric_difference_update(set2)

# print(set1)



set1 = {1, 2, 3, 4, 5}
set2 = {3, 4}
# result = set1.issubset(set2)      #False
# result = set1.issuperset(set2)

result = set1.isdisjoint(set2)
print(result)