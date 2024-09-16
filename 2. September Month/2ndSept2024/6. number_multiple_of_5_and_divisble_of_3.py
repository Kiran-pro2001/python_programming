#  number is multiple of 5 and divisible by 3 

# number multiple of 5 means, it should be divisble with 5.
# number is divisible by 3

number = int(input("Enter a number :"))

if (number % 5 == 0)  and (number % 3 == 0):
    print("The number is multiple of 5 and divisible of 3")
else: 
    print("The number is not multiple of 5 and nor divisbile of 3") 