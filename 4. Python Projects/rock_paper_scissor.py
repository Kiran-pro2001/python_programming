
# Rock Paper Scissor 


while True:
    # print("Do you wanna play Rock-Paper-Scissor Game? ")  # yes, no
    play = input("Do you wanna play Rock-Paper-Scissor Game (yes/no)? ").lower()

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
        print("You are right.")
        
    else:
        print("You are wrong,", "The right answer was",set1[0],".")
        
        
    # set1 = {1,2,3,4}
    # list1 = list(set1)
    # print(list1[0])
        
    
# options = {"rock", "paper", "scissor"}
# computer_option = options.pop()
# options.add(computer_option)
    
