
print("Welcome to our calculator")
while True:
    try:
        a = int(input("Enter the first number:"))
        break
    except ValueError:
        print("Invalid Input! Enter the integers only.")

    op = input("Enter the operator (+,-,*,/):")
    b = int(input("Enter the second number:"))

    if op == "+":
        print(f"When added {a} with {b}, the result is {a+b}")

    elif op == "-":
        print(f"When subtracted {a} with {b}, the result is {a-b}")

    elif op == "*":
        print(f"When multiplied {a} with {b}, the result is {a*b}")

    elif op == "/":
        print(f"When divided {a} with {b}, the result is {a/b}")


