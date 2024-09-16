# Check Character Case
# Write a Python program that takes a single character input and checks if it is an uppercase letter, a lowercase letter, or neither (e.g., a digit or a special character).




user_entered_character = input("Enter a character :")  # 'a'
if user_entered_character.isupper():
    print(f"{user_entered_character} is in Uppercase")
elif user_entered_character.islower():
    print(f"{user_entered_character} is in lowercase")
else:
    print(f"{user_entered_character} is neither Uppercase or Lowercase (Digit or Special Character)")
