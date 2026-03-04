# Boolean - This is a data type that evaluates either to true or false

isRaining = False
print(isRaining)
print(type(isRaining))

paidLoan = True
print(paidLoan)
print(type(paidLoan))

# Comparision Operators - they are used to compare two or more statements and they usually return a boolean answer

number1 = 2
number2 = 5

print("is number one greater than number 2 ?", number1 > number2)
print("is number one greater than number 2 ?", number1 < number2)
print("is number one greater than or equal to number 2 ?", number1 >= number2)
print("is number one less than or equal to number 2 ?", number1 > number2)
print("is number one equal number 2 ?", number1 == number2)
print("is number one not equal to number 2 ?", number1 != number2)

# Logical Operators 
# logical AND 
# It returns true if and only if the condition / statement evaluates to true 
print((3 > 1) and (7 > 6)) 

# Logical OR 
# It evaluates to true if one of the statements/conditions is true
print((3 > 1) or (7 < 6))

# Logical NOT 
# It is used to Negate a statement/ conditon
print(not(90 > 70))


