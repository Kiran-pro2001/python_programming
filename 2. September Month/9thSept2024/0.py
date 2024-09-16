

# Write a program to ask marks from the user, print pass type accordingly.

marks = int(input("Enter your marks :"))
# multiple conditions I understand -- therefor if elif elif
if marks >= 85:
    print("Distinction")
elif marks >= 70:
    print("First Class") 
elif marks >= 60:
    print("Second Class")
elif marks >= 35:
    print("Just Passed!")
else:
    print("You have not passed!")
    
# if we change the order of condtitions -- always true. 
    
    
## one more approach 

marks = int(input("Enter your marks :"))

if marks >= 85 and marks<= 100:
    print("Distinction")
elif marks > 70 and marks < 85:
    print("First Class")
elif marks >40 and marks <= 70:
    print("Second Class")
elif marks > 35 and marks <= 40:
    print("Just Pass")
elif marks >0 and marks <= 35:
    print("Not Pass")
else:
    print("Invalid Marks")



# Write a progrom to print the type of character (in string) entered by the user  - uppercase, lowercase,numbers, special characters

character = input("Enter a character :")  # 'a'
# if character.isupper() 
# 

# This can be solved using by two ways - without method and with method. 
# without method 
if 'A' <= character <= 'Z':
    print("Uppercase")
elif 'a' <= character <= 'z':
    print("Lowercase")
elif '0' <= character <= '9':     ## don't do elif 0 <= character <= 9  -- since, you can't compare integer value with string value
    print("Numbers")
else:
    print("Special Characters")
    
    
# with method 
    
character = input("Enter a character :")
if character.isupper():     # character.isupper() == True:
    print("Uppercase")
elif character.islower():
    print("Lowercase")
elif character.isnumeric():   # isdigit()
    print("Numeric")
else:
    print("Special Characters")
    
# k - lowercase
# K - uppercase 
# @1   - special characters   (since it will check for all the uppercase, not there...then it will check for all the lowercase...but not, then all the numeric...no, then it is special characters )
# Kiran   - special characters 




# two set -- set1 is a subset of setb, set2 is a subse of setb, disjoint


set1 = eval(input("Enter a set 1 :"))
set2 = eval (input("Enter a set2 :"))

if set1 < set2:   # it is not checking individual elements in one set to another set...it will check for subset or not
    print("Set1 is a subset of Set2")
elif set2 < set1:
    print("Set2 is a subset of Set1")
elif set1 == set2:
    print("Equal Sets")
elif set1 & set2 == set():   #  & - intersection , set() -default value of set data type, what is Nul it means  
    print("Disjoint Set")
else:
    print("Nor Relation")
    
# {1,2,3}  &  {1,4,5}




## with method


set1 = eval(input("Enter a set 1 :"))
set2 = eval (input("Enter a set2 :"))

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
elif set2.issubset(set2):
    print("Set2 is a subet of Set1")
elif set1 == set2:     # there is no built in method to check the equal to
    print("Equal set")
elif set1.isdisjoint(set2):
    print("Disjoint Set")
else:
    print("No Relation")
    
    
    

    
    
    # when multiple conditions....always write that condition that has higher chanes of getting true -- more optimize code





# relation between two numbers

num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter a number 2 :"))
if num1 > num2 :
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
# elif num1 == num2:
#     print(f"{num1} & {num2} is equal.")
# I don't need this..since already understood  (code more optimized)
else:
    print("They are equal")
