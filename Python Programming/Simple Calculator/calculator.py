def calculator():
    print("Simple Calculator")
    
    # Taking user input
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Choose operation (+, -, *, /): ")
        
        # Performing logical operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please choose +, -, *, or /.")
            return
        
       
       
        print(f"Result: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Invalid input! Please enter numeric values.")


calculator()
