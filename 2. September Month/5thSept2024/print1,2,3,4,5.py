# print 1,2,3,4,5 


num = int(input("Enter a number :"))  # '3' -- 3
if num == 1:   # 3 == 1  (no)
    print("The number is 1")
elif num == 2:  # 3 == 2
    print("The number is 2")
elif num == 3:  # 3 == 3  (true)
    print("The number is 3") # this gets printed 
elif num == 4:
    print("The number is 4")
elif num == 5:
    print("The number is 5")
else:
    print("The num is not 1,2,3,4,5")