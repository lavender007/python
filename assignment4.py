# 1. a function that uses operators to calculate the area of a triangle
def multiplication():
    num1= 14
    num2= 12
    product= num1*num2
    print("The area of the rectangle is:",product)
multiplication()

print('==============================')
# 2. function that accepts two numbers as parameters adddition
def addition(x , y):
    sum = x+y
    print("The sum of the number is:",sum)
addition(45, 50)

print('=====================')

#product
def multiplication(a, b):
    product = a * b
    print("The product is:",product)
multiplication(45, 50)

print('===============')

#division
def divide(c, d):
    quotient = c / d
    print("the quotient is:",quotient)

divide(45, 9)

print('================')
# subtraction

def subtraction( e , f):
    difference = e-f
    print("The difference is:", difference)
subtraction(50, 45)

print('=================')

# 3. control satatement

num = int(input("Enter number here:"))
if num == 0:
    print("zero")
elif num > 0 :
    print("Positive number")
elif num < 0:
    print("Negative number")
else: 
    print("not a number")

print('==================')

#4. loop with arthimetic
for num in range( 1,16, 1):
   print(num)

print('=============')

#5. while loop
num=int(input("Enter number here:"))
while num<= 16:
    num= num*num
    print (num)






