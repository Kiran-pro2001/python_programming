# User entered character is lowercase or uppercase -- I need to tell without using inbuild functions

character = input("Enter a character :")
if 'a' <= character <= "z":
    print("Lowercase")
else:
    print("Uppercase")