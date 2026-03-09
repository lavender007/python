# loops=> sometimes we may need to do a piece of work a piece of work number of times and in such cases we may use loops.
# loop- a loop is a control structure that allows us to execute a block of code repeatedly until a certain condition is met
#there are two types of loop in python i.e The for loop and the while loop
""" 
for variable in range(n):
    # block of code to be executed
"""



for  greeting in range(5):
    print("Hello Moses", greeting)


print('================')

for number in range(10, 20):
    print(number)

print('===================')
#find the even numbers in the range of 50 to 71
for number in range(50, 71, 2):
    print(number)

print('==============')
#create the python programme that prints the odd numbers from 100 to 150
for number in range(101, 150, 2):
    print(number)

print('=============')
#create a programme that prints the multiples of 3 starting from 201 to 150
for number in range(201, 149, -1):
    if number % 3 == 0:
        print(number)

print('===================')
#create a pyton programme that prints the leap years in between 2000 and 2024
for year in range (2000, 2024, 4):
    if year % 4 == 0:
        print(year)