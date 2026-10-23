print("----BASIC CLACULATOR----")


num1 = input("Enter the first value: ")
num2 = input("Enter the second value: ")

operator = input("Select the operation(+,-,*,/): ")

if (operator =="+"):
    cal = f" Result: {int(num1)+int(num2)}"
    print(cal)
elif(operator =="-"):
    cal = f" Result: {int(num1)-int(num2)}"
    print(cal)
elif(operator =="/"):
    cal = f" Result: {int(num1)/int(num2)}"
    print(cal)
elif(operator =="*"):
    cal = f" Result: {int(num1)*int(num2)}"
    print(cal)

else:
    print("ERROR")

    