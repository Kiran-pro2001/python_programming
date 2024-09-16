# Check is the user entered collection has less than or equalt to 5 elements

collection = eval(input("Enter a collection :"))
length_collection = len(collection)
if length_collection <= 5:
    print("Collection has less than 5 Elements")
else:
    print("Collection has greater than 5 Elements")
