operator = input("Enter the operator (+,-,*,/): ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if operator == "+":
    print(float(num1) + float(num2))
elif operator == "-":
    print(float(num1) - float(num2))
elif operator == "*":
    print(float(num1) * float(num2))
elif operator == "/":
    print(float(num1) / float(num2))
else:
    print("Invalid operator")
