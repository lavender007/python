#python function
#They are a block of code/ statement that performs a different task/action. They can be reused through out the program to perform different tasks.
#Functions sre defined using the def keyword. (define)
#we have two main type of functions i.e
# 1. In- built functions  -> They come pre-installed witht the interprator i.e print(), pop (), range(), append(), etc

#user defined functions=> They are creates by a programmer to solve a given task .
#to define a function you need to give it a name followed by parenthesis.
#For the functions, it is usually indented and to invoke a function we use the function name.

def greetings():
    print("Hello, how are you?")

greetings()


print('======================')
#Addition function
def addition():
    num=40
    num2=50
    sum= num + num2
    print("The sum of the numbers is:", sum)

addition()

print('=====================')

#create a function that is able to multiply three values
def multiplication():
    num1 =10
    num2= 60
    num3= 5 
    product= num1 * num2 * num3
    print("The product of the number is:", product)

multiplication()

print('=========================')
#Below is a division function
def divide():
    number1= int(input("Enter the first number:"))
    number2= int(input("Enter the second number:"))
    quotient= number1/number2
    print("The answer is: ", quotient)

print('==========')

for function in range(3):
    divide()













