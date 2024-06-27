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

while True:          # Infinite loop to keep the program running until the user choodes to exit.

        #   Display menu option
    print("\n(((( Calculator Menu ))))\n -------------------------------")
    print("0.Exit ")
    print("1.Addition ") 
    print("2.Subtraction") 
    print("3.Multiplication ") 
    print("4.Division") 
    print("--------------------------------")

    