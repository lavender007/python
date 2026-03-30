# Functions with parameters
# parameters=> they are values that get passed as arguments given to a function inside of the parenthesis.



def greeting(name):
    print(f"{name} How are you? Hope everything is fine.")

greeting("samantha")
greeting("Matthew")
greeting("John")

print("=======================")

def message(names):
    print(f"Hello{names} We shall be having a general meeting on date..... please avail Yourself")

message("Joy")
message("Branice")
message("Hope")

print('==============')

# create a function that accepts parameters to add two numbers
def addition (x , y):
    sum= x+y
    print("The sum of the numbers is:", sum)

addition( 45, 65)
addition(78, 92)