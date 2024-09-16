# Age Validator -
# Write a Python program that asks the user to input their age and checks if they are eligible to vote (age 18 and above).

age = int(input("Enter your age :"))
if age >= 18:
    print("You are eligible for Vote. ")
else:
    print("You are not eligible for Vote. ")