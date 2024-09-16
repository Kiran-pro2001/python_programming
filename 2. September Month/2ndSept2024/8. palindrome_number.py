# Palindrome Number 

# Means, if we reverse the word, it would be same.
# Example - 
# mom -- mom
# dad -- dad
# malayalam - malayalam
# wow -- wow
# madam -- madam


# WAP to check if a given number is palindrome or not.

word = input("Enter a word :")
reverse_word = word[::-1]   # can you explain this once (doubt)
if reverse_word == word:
    print("It's a Palindrome Number")
else:
    print("The number is not a Palindrome Number")
    


# How string slicing works 

# for positive set value ---don't know the exact value
print("helloworld"[1:5:1]) #ello  (because it will move from e to 4th index)


print("helloworld"[1:5:-1])  # empty string will be printend 
# it will start from 1st index and move to 4th index....but set value is -1 , it means it has to start from back and move forward....it it moves forward..nothing will come..only empty string gets printed. 
# so whenever yous see, negative step value...it means, you have to start from back side...
# for negative index....the start value becomes end value and end value become start value...it it needs an answer..otherwise we don't get answer...
# to print the above thing...just change the starting value to ending value and ending value to start value 


print("helloworld"[5:1:-1])
# it means, now the thing start from back side, from index -1, and starting point is 5th index..it means character -- w and and ending point is 1, but that is not excluding..so index value to be 2... ..so charcter is "l"
# so it will move from w to l, and move from backward to forward...with step value is -1
# Therefore the answer is --   woll


print("kiran"[: :1])  # kiran
# here positive step value is there...so start point will be 0, and end point will be lenghth-1 and step value is 1, so keep moving forward
# henc it will move from 0th index to lenght-1 index, by 1 step value...so complete string get printed 

print("helloworld"[::-1])  # dlrowolleh
# here the step value is negative, what it means is, it will move from backward to forward..
# now the start value is ...How to get it?
# so for that..firstly imagine like....the step value is positive...if that is positive..then how works?
# if positive index value is there...then start point will be 0 and ending point will be lenght-1 (because it start from 0)
# but for negative step value...it will start from -1 and ends to -length-1 (no length-1   -- since it starts from 1)
# so it will move from -1 index (which is d) to  -length-1    (which is -10-1 = -11)   [[[ Doubt -- Is this line is True ]]]
# hence it will move from backward, from d word to h word. and Hence we get the complte string. 

