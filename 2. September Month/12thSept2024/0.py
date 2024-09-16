# Greatest among three numbers -
# Write a progam to find greatest among 3 user entered numbers using nested if. 


num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
num3 = int(input("Enter a number 3 :"))

# if num1 > num2 and num2 > num3
# method 2 -- use nested concept

if num1 > num2:
    if num1 > num3:
        print("The num 1 is greatest")
    else:
        print("The num3 is greatest.")
else:
    if num2 > num3:
        print('The num2 is greatest.')
    else:
        print("The num3 is greatest")



# what if we have 15 numbers, what we can do ? Any optimize way we have. 




# smallest among 3

num1 = int(input("Enter a number 1 :"))
num2 = int(input("Enter a number 2 :"))
num3 = int(input("Enter a number 3 :"))

if num1 < num2 :
    if num1 < num3:
        print("num1 is smallest")
    else:
        print("num3 is smallest")
else:
    if num2 < num3:
        print("num2 is smallest")
    else:
        print("num3 is smallest.")
        
        
        



# list is given, and the do the same stuff

list1 = [1,2,3]   #list1 not the list, so that no clash
num1 = list[0]
num2 = list[1]
num3 = list[2]

# if list of 8 numbers, the complicated 
# separate false statement for each


# min & max -- build in function -- to find the maximum & minimum
# - collection as an argument 
# - it works in homogenous elements   - integer & float works,   integer string value not work.
print(min(list1))
print(max(list1))


'''


# min()
- It is a build in function used to get the minimum value from the homogenous collection. (set, tuple, list, tuple)


# max()
- It is a build in function used to get the maximum value from the homogenous collection. 

what if I give hetrogenous..what will happen...experiment it






# Match Case - Here we mention a parameter, next to match keyword. 
- For the specified parameter, we will be having case blocks which some pattern. 
- That case block whose pattern matches the parameter, will be executed. 
- If none of the case block pattern is matching a parameter, we can have a default case block (_) - underscore. Which will be executed at the end. 



Syntax -    


var = valu1
match var:
    case pattern1:
        case statement block
    case pattern2:
        case statement block
    case pattern3:
        case
    .
    .
    case _:
        Default Statement Block







IN C -- Switch Case, 
But in Python, We have Match Case.
general programming, we wont' use.
for building a game, samll program -- it is helpful.

match is a keyword 
take only parameter, it won't take condition.
when match is used, you need to use case..... and guess what user can enter
What he enter A, what to do, what if he enter B, what to do.
We can also take integer as well, for that I will put Case 1, Case 2, Case 3..........


'''




option = input("""Enter the option from below :  \n 
            A - Pizza
            B - Burger
            C - Vadapav
            D - Golgappa""")
match option:
    case "A":    # case 1 :    (if integer)
        print("You have ordered Pizza")
    case "B":
        print("You have orderd Burger")
    case "C":
        print("You have ordered Vadapav")
    case "D":
        print("You have ordered Golgappa")
    case _ :  # by default (only be executed if not entered A, B, C)
        print("Invalid Option")
        
        
# to write default case, use underscore.
# no need to put like string.

# Kon Baena Corepati Game we can build this game with the help of Match Case. -- use random module. 




# 
qualification = int(input("Enter your Qualification :  \n  1. BE/BTech \n 2. BCA / BSc.  "))
match qualification:
    case 1:
        print("Lots of Opportunities")
    case 2:
        print("Fair Opportunities")
    case _:
        print("Very Difficult")
        





