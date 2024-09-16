# #strip() - remove
# #split()



# name = "Shadab"
# result = name.strip()
# print(result)

# name23 = "Shadab_"
# result = name23.strip()
# print(result)

# name3 = "__Shadab__"
# result = name3.strip("_")
# print(result)

name4 = "__Shadab__arsh ad__ "
result1 = name4.strip()
result2 = name4.strip("_")
result3 = name4.lstrip("_")  #3
result4 = name4.rstrip("_")  #4

print(result1)
print(result2)
print(result3)
print(result3)




# __Shadab__arsh ad__
# Shadab__arsh ad__
#RESULT=__Shadab__arsh ad__
#Result2=Shadab__arsh ad__




#split - divide


name = "_I_am a boy"
result = name.split("_")
# print(result)
# print(type(name))
#["I","am a boy"]

name = "@I@am a boy"
result = name.split("@")
# print(result)

name = " Iam a boy"
result1 = name.split(" ")  #space
result2 = name.split() #empty places between two characters
# print(result1)
# print(result2)




name = " I am a G _irl_ nb_ 1 "
result = name.split(" ")
print(result)

#["I","am","a","G","_irl_","nb_","1"]
#[" ","I","am","a","G","_irl_","nb_","1"," "]

#['I', 'am', 'a', 'G', '_irl_', 'nb_', '1']





name = "spi der"
result = name.split()
print(result)

name = " sp __d_ i_r"
result = name.split()
print(result)



#Pattern Printing - center

name = "kiran"
result = name.center(10)
print(result)
result = name.center(10,"_")
print(result)

dish = "dosa"
result = dish.center(2)
print(result)

result = dish.ljust(10)
print(result)

result = dish.rjust(10)
print(result)


hero_name = "Kiran Kumar"
result = hero_name.endswith("r")
print(result)

result = hero_name.startswith("h")
print(result)




#strip() and strip("_")
#lstrip
#rstrip
#split() and split("_")
#center(10), center(10,"_")
#endswith("a")
#startssith("b")






