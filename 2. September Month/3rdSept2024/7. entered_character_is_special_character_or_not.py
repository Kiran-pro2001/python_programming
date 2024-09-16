# Entered character is special character or not 
# Special Character - other than number & alphabets

character = input("Enter a character :")  # a
if "a" <= character <= "z"  or  "A" <= character <= "Z"  or "0" <=character <= "9":
    print("Not a Special Character")
else:
    print("It's a Special Character")
    
# @ - special character
# k - not a special character
# ki -- not a special character (it checks the first letter)

# [10,20]  - It is a special character
# {10,20}  - It is a special character

# @ - Special Character  
# k@ - not a special character

# Hence it means, it is checking for the first character, if the first character is special character (@,+,[10,20] -- here  [ is considere as first letter--that is special,  {10,20} -- here { is first character--cnosidered as special ) - it will print the -- special character....if first character is not the special character (k, ki) --then print not a special character 


