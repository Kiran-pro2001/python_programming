# Tells set1 is a subset of set2, or set2 is a subset of set1, or equal set or disjoint set or no relation
# Tells the realtion between two sets

set1 = eval(input("Enter Set1 :"))
set2 = eval(input("Enter Set2 :"))
if set1 < set2:
    print("Set1 is a subset of Set2")
elif set2 < set1:
    print("Set2 is a subset of Set1 ")
elif set1 == set2:
    print("Set1 is equals to Set2")
elif set1 & set2 == set():   # & - intersection, interection equals to default value of set, that is set of - set(), it means null....
    print("Disjoint Sets")
else:
    print("No Relation")
    
# {1,2} & {1,2,3}  -- set2 is a subset
#{1,2,3} & {1,4,5}  -- No Relation.
# {1,2,3} & {4,5,6} -- Disjoint Sets
