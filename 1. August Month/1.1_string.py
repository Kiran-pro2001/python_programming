print("Hi")

name = "Kiran Kumar"

result = name.upper()
print(result)

result = name.isupper()
print(result)

result = name.lower()
print(result)

result = name.islower()
print(result)


result = name.capitalize()   #Only First character become capital. If number, then no effect.
print(result)

name2 = "123kiran"
result = name2.capitalize()
print(result)

print("***************")
name3 = 'kiran kumar'
result = name3.title()   #First character of Each word of a sentence become capital, Rest make it lowercase.
print(result)

name4 = '123 kiran Kiran kUnal Kunal'
result = name4.title()
print(result)
# 123 Kiran Kiran Kunal Kunal


name5 = "kiran Kumar KUMar"
result = name5.swapcase()   #lower to upper for each characters in a word & upper to lower for each characters in a word. 
print(result)
# KIRAN kUMAR kumAR

name5 = "kiran123"
result = name5.isalnum()   #Either numeric or alphaber   (No special characters p)
print(result)


result= name.replace("Kiran","Kunal")
print(result)

result = name.replace("kiran","kajal")   #Not replaced, because small case "kiran" is not there in the original string
print(result)


movie1 = "  three idiots  "
result = movie1.strip()
print(result)

movie2 = "____three idiots___"
result = movie2.strip("_")
print(result)

hero1 = "____kir___ran____"
result = hero1.strip("_")
print(result)

hero2 = "kiran"
result = hero2.strip("k")
print(result)



hero3 = "___kiran kumar___"
result=hero3.lstrip("_")
print(result)

result = hero3.rstrip("_")
print(result)

#split - sentence to word

sentence = "I am the greatest person ever born on this planet"
result = sentence.split()    #not passed anything, it split at space
print(result)

sentence = "I_am_the_greatest_person_ever_born_on_this planet"
result = sentence.split("_")
print(result)


# center - use for pattern printing 
dish = "dosa"
result = dish.center(10)
print(result)

result = dish.center(10,"_")
print(result)

result = dish.center(2)
print(result)

result = dish.ljust(10,"_")
print(result)

result =  dish.rjust(10,"_")
print(result)

name = "kiran kumar"
result = name.startswith("k")   #It returns boolean value
print(result)

result = name.endswith("ra")
print(result)

#It's a doc string - We can use for multi line string or We can also use for comment.
about_me = '''I am the greatest person ever
born on this planet'''
print(about_me)

#multi line comment
'''Hi
It's a demo example of 
multi line comment'''

word = "hello"     #here "l" is repeating - so get the same address
print(id(word[2]))  #get the same address
print(id(word[3]))  #get the same address
print(id(word[0]))

print(word)


# strip function - removes from beginning and at end. 
name = "  Kiran  " 
result = name.strip()
print(result)

name = "____ Kiran ___"
result = name.lstrip()  #If not pass, only remove the space
print(result)

result = name.lstrip("_")