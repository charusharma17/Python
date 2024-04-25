#calculator
while True:
    print("\n===== Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # User input
    choice = input("Enter your choice (1/2/3/4/5): ")

    # Addition
    if choice == '1':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)

    # Subtraction
    elif choice == '2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 - num2)

    # Multiplication
    elif choice == '3':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 * num2)

    # Division
    elif choice == '4':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error! Division by zero.")

    # Exit the program
    elif choice == '5':
        print("Exiting...")
        break

    # Invalid input
    else:
        print("Invalid input! Please enter a valid option.")
