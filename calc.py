def add(x, y):
    return x + y
def subract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else: 
        return x / y
    
num1 = 1990
num2 = 10

print (f"addition: {add(num1, num2)}")
print (f"subraction: {subract(num1, num2)}")
print (f"multiplicatuion: {multiply(num1, num2)}")
print (f"division: {divide(num1, num2)}")