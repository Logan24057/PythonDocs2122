#Logan Danner
#creating lists in python

#create a list with 3 items
groceries= ['milk', 'bread', 'eggs']

#print entire list
print(groceries)

#print out each thing individually by index
print(groceries[0])
print(groceries[1])
print(groceries[2])

#print how many things are in this list
print(len(groceries))

#add an item to the list and print new list
groceries.append('hot cocoa')
groceries.append('egg nog')
print(groceries)

#remove item from the list
#remove item with matching value
groceries.remove('egg nog')
print(groceries)
#remove item by index (hot cocoa)
groceries.remove(groceries[3])
print(groceries)

#other index trick
#count index from the end
print(groceries[-2])
#return a list of only the first two utems
print(groceries[:2])
#return a list of only the last two items
print(groceries[2:])
#get the last item of the first two items of the lists
print(groceries[2:] )

#check to see of a value is in a lists
print('Is milk in the list')

if 'milk' in groceries:
    print('yes')
else:
    print('no')


#how to use for loops
print("here is each item in the grocery list")
for food in groceries:
    print(food)
