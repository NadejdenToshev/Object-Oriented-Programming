def basic_calculator():
    print("Welcome to the basic Calculator")
    
    # Step 1: Prompt the user to enter two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        return
    
    # Step 2: Ask the user to choose an operation
    print("Choose an operation:")
    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")
    
    operation = input("Enter the number corresponding to the operation: ")
    
    # Step 3: Perform the chosen operation
    if operation == "1":
        result = num1 + num2
        operator = "+"
    elif operation == "2":
        result = num1 - num2
        operator = "-"
    elif operation == "3":
        result = num1 * num2
        operator = "*"
    elif operation == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operator = "/"
    else:
        print("Invalid operation selected.")
        return
    
    # Step 4: Display the result of the operation
    print(f"{num1} {operator} {num2} = {result}")

# Step 5: Run the calculator


basic_calculator()
