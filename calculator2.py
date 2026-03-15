print("Welcome to our calculator")
a = int(input("Enter the first number: "))
op = input("Enter the operator:(+ or - or * or /)")
b = int(input("Enter the second number: "))

if op == "+":
    print("The result is: ", a+b)

elif op == "-":
    print("The result is: ", a-b)

elif op == "*":
    print("The result is: ", a*b)

elif op == "/":
    if b==0:
        print("Cannot divide by zero. Please give the value of b other than 0.")
    else:
        print("The result is: ", a/b)