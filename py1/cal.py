from math import *
def calculator():
    print("********SCIENTIFIC CALCULATOR********")
    print("Enter two numbers:")
    while True:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
    
    print("Enter the operation you want to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")

    while True:
        try:
            choice = int(input("Enter your choice (1-10): "))
            if choice < 1 or choice > 10:
                print("Invalid choice. Please enter a number between 1 and 10.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    if choice == 1:
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    elif choice == 2:
        result = num1 - num2
        print(f"The difference of {num1} and {num2} is {result}")
    elif choice == 3:
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}")
    elif choice == 4:
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The quotient of {num1} and {num2} is {result}")
    elif choice == 5:
        result = pow(num1, num2)
        print(f"{num1} raised to the power of {num2} is {result}")
    elif choice == 6:
        if num1 < 0 or num2 < 0:
            print("Error: Square root of negative number is not allowed.")
        else:
            result = sqrt(num1)
            print(f"The square root of {num1} is {result}")
    elif choice == 7:
        result = sin(radians(num1))
        print(f"The sine of {num1} degrees is {result}")
    elif choice == 8:
        result = cos(radians(num1))
        print(f"The cosine of {num1} degrees is {result}")
    elif choice == 9:
        result = tan(radians(num1))
        print(f"The tangent of {num1} degrees is {result}")
    elif choice == 10:
        if num1 <= 0 or num2 <= 0:
            print("Error: Logarithm of non-positive number is not allowed.")
        else:
            result = log(num1, num2)
            print(f"The logarithm of {num1} with base {num2} is {result}")
    elif choice=='exit':
        print("Exiting the calculator. Goodbye!")
        return
    else:
        print("Invalid choice. Please select a valid operation.")
calculator()