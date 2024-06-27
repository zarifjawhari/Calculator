

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
    
        # Get user choice
    choice = input("\nEnter your Choice (0 - 4) : ") 
    if choice in ('0','1','2','3','4'): 
        if choice == '0':
            print("\n>>>> Good Bye <<<<\n")
            break       # Exit the program

            # Get user inputs
        num1 = int(input("Enter First Number = ")) 
        num2 = int(input("Enter 2nd Number = ")) 
     
        if choice == '1': 
            print("\nResult: ",num1, "+", num2, "=", add(num1,num2)) 
        elif choice == '2': 
            print("\nResult: ",num1, "-", num2, "=", subtract(num1,num2)) 
        elif choice == '3': 
            print("\nResult: ",num1, "*", num2, "=", multiply(num1,num2)) 
        elif choice == '4': 
            print("\nResult: ",num1, "/", num2, "=", divide(num1,num2)) 

    