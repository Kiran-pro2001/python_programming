# Entered value is mutable or immutable

data = eval(input("Enter any value :"))  # '2'  -- 2
type_of_data = type(data) # int 
if type_of_data in [list,set,dict]:
    print("It's a Mutable Data")
else:
    print("It's an Immutable Data")







# Dry Run is damn important..then only you can be a good programmer 
   