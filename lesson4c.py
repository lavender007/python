# A for loop can also be used to iterate through a list a tuple, string or even a dictionary ...

name = " Samantha"

for letter in name:
    if letter=="n":
        print("This is letter n")
    else:
        print(letter)

print('===========================')
#Below is a list of counties

counties = ["Nairobi", "Mombas", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

print('============================')


counties = ["Nairobi", "Mombas", "Kisumu", "Nakuru", "Eldoret", "Kajiado", "Machakos", "Meru", "Embu"]
if "Kajiado" in counties:
    print("Kajiado is in the list of counties")
else:
    print("Kajiado is absent in counties")

print('============')

for county in counties:

    if county =="Nairobi":
        print("The county is part of the list")
    else: 
        print("The county is not part of the list")

print('================')
#The for loop alse can be used ti iterate through a dictionary

player={
    "name": "Mbappe",
    "age" : "25",
    "teams": ["PSG", "Monaco" "France"],
    "nationality": "French"

}

for key in player:
    print(key)

print('==========================')

for values in player:
    print(player[values])

print('=======================')
#loop throughout te teams the player has played for

for team in player["teams"]:
    print(team)



