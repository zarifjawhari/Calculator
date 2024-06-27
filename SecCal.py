print("Hello, weccome to CALCULATOR")
# Define function for arithmetic operation
def add(x,y): 
    return x + y; 
def subtract(x,y): 
    return x - y; 
def multiply(x,y): 
    return x * y; 
def divide(x,y):
    if y==0:
        print("Division by 0 is not defined.")
    else:    
        return x / y