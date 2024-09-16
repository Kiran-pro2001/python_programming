# Entered set is a subset of another set 


# Logic 1 

set1 = eval(input("Enter a Set 1 :"))
set2 = eval(input("Enter a Set 2 :"))
if (set1 < set2) or (set1 > set2):
    print("One set is a subset of another set")
else:
    print("No subset is there")
    


# Logic 2 -- Using issubset method 


set1 = eval(input("Enter a Set 1 :"))
set2 = eval(input("Enter a Set 2 :"))
if set1.issubset(set2)  or set2.issubset(set1):
    print("One is a subset of another")
else:
    print("No subest is there")