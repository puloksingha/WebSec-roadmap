print("----BASIC CALCULATOR----")


num1 = input("Enter the first value: ")
num2 = input("Enter the second value: ")

operator = input("Select the operation (+, -, *, /): ")

try:
    first_value = int(num1)
    second_value = int(num2)
except ValueError:
    print("ERROR: Please enter valid integers.")
else:
    if operator == "+":
        print(f"Result: {first_value + second_value}")
    elif operator == "-":
        print(f"Result: {first_value - second_value}")
    elif operator == "*":
        print(f"Result: {first_value * second_value}")
    elif operator == "/":
        if second_value == 0:
            print("ERROR: Cannot divide by zero.")
        else:
            print(f"Result: {first_value / second_value}")
    else:
        print("ERROR: Unsupported operation.")


    