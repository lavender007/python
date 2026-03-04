# Create a python programme that is able to determine either a number entered is an even number or an odd number

# number = int(input("enter your number here"))
# if number % 2 == 0:
#     print("even number")
# else:
#     print("odd number")

# Create a python program that is able to determine whether a person can donate blood based on the age and weight of a person. If the weight is above 50kg and age is above 18, then the person can donate, else not possible.

age = int(input("enter age"))
weight= float(input("Enter weight"))
if age >=18 and weight >50 :
    print("can donate")
else :
    print("cant donate")