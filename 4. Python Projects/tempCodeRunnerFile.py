
# Rock Paper Scissor 

# print("Do you wanna play Rock-Paper-Scissor Game? ")  # yes, no
play = input("Do you wanna play Rock-Paper-Scissor Game? ").lower()

if(play == "yes"):
    print("Let's play the Game!")
else:
    print("Game Over!")
    quit()

# choose = {"rock","paper","scissor"}

set1 = {"rock","paper","scissor"}
set1 = list(set1)

choose = input("What you choose - rock, paper, scissor ? ").lower()

# while True:

# while True:

if choose == set1[0]:
    print("You are right")
    