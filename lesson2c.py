#A dictionary is a data type that stores data in terms of key - value pair
# It is introduced by the use of curly braces{}
#The values stored of a dictionary can be of any data type
#To access the values in a dictionary we use the keys


phonebook ={
    "Benson": "254723456788",
    "Mary" : "254734567899",
    "stephen" : "25474567890"

}

#showing the entir phonebook
print(phonebook)
print(type(phonebook))

#printing out benson's number
print(phonebook["Benson"])

print('==============')

player = {
    "name" : "messi",
    "Age" : 40 ,
    "teams" : ["PSG", "Barcelona", "Argentina"] ,
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" : (25477345789, 25472034587, 254723456789)

    }
}

#print barcelona
print(player["teams"][1])

print("Messi's second number", player["more"]["phone"][1])