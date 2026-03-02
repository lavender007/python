#Python lists 
#A list in python is a collection of items that are orderd in a certain way.
#A list is introduced by the use of square brackets[]
# The items of a lists are stored inside of indexes. Note: In programming we start counting from index Zero(0). bmw, benz, hiance,...
#A list is mutable i.e The coontents of a lists can be changed.

cars = ["BMW", "Benz", "hyundai", "prado", "probox", "Volvo", "Audi" ]

print(cars)
print(type(cars))

#Accesing items of a list
print(cars[2])
print("The car on index 4", cars[4])


#list slicing- This is creating a list from a given bigger list 
print(cars[4:])

#printing from index 0 to index 3 
print(cars[:4])

#printing from hyundai to probox
print(cars[2:5])

#list mutability
#we use the function append to add an item at the end of a list
cars.append("ferrari")
print(cars)

cars.append("Mercedes")
print(cars)

# We use the pop function to remove an item at the end of the lists
del cars [4]
print(cars)

#We can use an index to add items to a list 
cars[5] = "pajero"
print (cars)

#we can use the sort function to sort out items in alphabeical order
cars.sort(reverse=True)
print(cars)


