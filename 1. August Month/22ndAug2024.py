
# Special Operators 
# 1. Identity - is, is not
# 2 Membership - in, not in 



list1 = [10,20,30]
list2 = [10,20,30]

print(id(list1))
print(id(list2))

print(list1 == list2)  #True  (Just check values index by index)
print(list1 in list2 )  #False (Since it checks the addresses)

print((10,20) is (20,10))  #False   --- Index wise the elements are different, though the elements are same)

print((20,10,20) is (20,10,20))  #True
# immutable -- so no new block will be given, index wise same.

print({1,True} is {1.0, 1})   # Mutable means always false (Their addresses are different, so false...)

print({1, True} == {1.0, 1})  #True  - duplicate values we can store, it removes the duplicate values while storing

print((1, True) is (1.0, 1))  #False   (Tuple is immutable --addresses will be different)

#for the respexgive keys the values are different



print("mis" in "misunderstandings")
# print(10 in 100)  #for integers value we can't do in operations 

print((10,20) in (10,20,30,40))  #

