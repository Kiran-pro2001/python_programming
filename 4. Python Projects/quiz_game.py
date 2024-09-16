print("Welcome to my Quiz Game")

playing = input("Do you want to play? (yes, no)  ")
# print(playing)   #For checking!


#Concept is, make it lower. so that (yes, YEs, YES) all will be same.
# name = "Kiran"
# name = name.lower()   #using string's lower function. 
# print(name)

if playing.lower() != "yes":
    print("Game Over!")
    quit()

print("Ok, Let's Play!")
score = 0

answer = input("What does CPU Stands for? ").lower()
if answer == "central processing unit":
    print("Correct Answer")
    score += 1
else: 
    print("Wrong Answer.")
    
    
answer = input("What does GPU Stands for? ").lower()
if answer == "graphical processing unit":
    print("Correct Answer")
    score += 1
else: 
    print("Wrong Answer.")


answer = input("What does RAM Stands for? ").lower()
if answer == "random access memory":
    print("Correct Answer")
    score += 1
else: 
    print("Wrong Answer.")


answer = input("What does ROM Stands for? ").lower()
if answer == "read only memory":
    print("Correct Answer")
    score += 1
else: 
    print("Wrong Answer.")
    
print("You got " + str(score) + " questions correct!")  
print("You got "+ str( (score / 4) * 100) + "%.") 




