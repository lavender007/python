# On the try and except block : You can run some codes/ statements and if it is successful the try block will get exhausted other the except block will be executed when there is an anticipated error.


import math


try:
    number = 100
    answer = number / 0
    print("The answer is:", answer)
except Exception as e:
    print("There is an error:",e)

try:
    age= int(input("Enter your age:"))
    print ("Next year you will be:", age + 1)
except Exception as e:
    print("There is an error:",e)
    
    

try:
    numbers =[10,20,30]
    print("The number is:", numbers[6])
except Exception as e:
    print("There is an error:",e)

try:
    marks= int(input("Enter your marks:"))
    print("Your marks are:", marks)
except ValueError as e:
    print("Invalid input! Please enter a number.",e)

try:
    result= math.sqrt(9)
    print("result:",result)
except ValueError as e:
    print("There is a ValueError:",e)

