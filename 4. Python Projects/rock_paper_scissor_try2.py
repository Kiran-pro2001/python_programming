options = {"stone", "paper", "scissor"}




while True:
    option = input("Do you wanna play game? (yes/no) ").lower()  # yes  # yes 
    if option == "yes":
        print("Let's play the game! ")
    else: 
        print("Game Over ")
        quit()

    choose = input("What you wanna choose - stone, paper, scissor ? ")  # stone  # stone
    computer_options = options.pop()  #remove randomly and return that element   # paper # stone
    options.add(computer_options)  # so that the options should not get ended  # {"stone","paper","scissor"}
    
    if computer_options == choose:    # paper == stone    - False  # stone == stone
        print("You are right.") 
    else:
        print(f"You are wrong, The right answer was {computer_options}.")  # Executed 