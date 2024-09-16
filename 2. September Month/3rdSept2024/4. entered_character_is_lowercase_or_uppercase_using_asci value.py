# User entered character is in lowercase or uppercase -- using ASCI Value


# ord function is used to fetch the asci value corresponding to a character
# ord function takes character as an input and returns the asci value

# Uppercase

ord('A')  # 65
ord('Z')  # 90

# Lowercase
ord('a')  # 97
ord('z')  # 122


user_enter = input("Enter a character :")
ascii_value = ord(user_enter)
if 97 <=ascii_value <= 122:
    print('Lowercase')
else:
    print("Uppercase")