# Check the user entered data is single value data type or a collection

data = eval(input("Enter a data :"))
type_of_data = type(data)
if type_of_data in [int,float,complex,bool]:
    print("Single Value Data Type")
else:
    print("Multivalue Data Type")