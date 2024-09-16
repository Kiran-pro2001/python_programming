character = input("Enter you character :")
if 'A' <= character <= "Z":
    print("Character is Uppercase")
elif 'a' <= character <= 'z':
    print("Character is Lowercase")
elif '0' <= character <= '9':
    print("Character in Numbers")
else:
    print("Special Characters")
