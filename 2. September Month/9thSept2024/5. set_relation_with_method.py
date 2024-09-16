# set realtion with method



set1 = eval(input("Enter a Set 1 :"))
set2 = eval(input("Enter a Set 2 :"))

if set1.issubset(set2):  # Returns true or false
    print("set1 is a subset of set2")
elif set2.issubset(set2):
    print("set2 is a subset of set1")
elif set1 == set2:
    print("Equal Sets")
elif set1 & set2 == set():
    print("Disjoint Sets")
else:
    print("No Relation")
    
# {1} & {1,2,3}   - set1 is a subset of set2
# {1,2,3} & {1}  - set2 is a subset of set1
# {1,2} & {1,2}   - Equal Sets.

