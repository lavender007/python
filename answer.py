county = input("Enter the city to check")

found = False

counties = ["Nairobi", " Kisumu" , "Narok", "Elgyo Marakwet", "Lamu", "Tana River", "Machakos", "Nandi"]

for c in counties:
    if county ==c:
        found=True
        break

if found:
    print("The county entered is part of the list")
else:
    print("The county entered is not part of the list")

