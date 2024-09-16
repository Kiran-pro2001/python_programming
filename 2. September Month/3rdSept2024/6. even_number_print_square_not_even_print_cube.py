# If entered number is even, print the square of it. If not even, print the cube of it.


number = int(input("Enter a number :"))
if number % 2 == 0:
    print(f"Square of a number is {number ** 2}")
else:
    print(f"Cube of a number is {number ** 3}")