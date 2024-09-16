set1 = {1,2,3}
set2 = {1,2,3,4,5}
print(set1 < set2)   # set1 is a subset of set2   - yes -- True
print(set2 < set1)   # set2 is a subset of set1 - no --- False




# Palindrome of a number 

num = input("Enter a number : ")
reversed_num = num[::-1]
if num == reversed_num:
    print("It's a palindrome number ")
else:
    print("It's not a palindrome number")