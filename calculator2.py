
print("Welcome to our calculator")
while True:
    while True:
        try:
            a = int(input("Enter the first number:"))
            break
        except ValueError:
            print("Invalid Input! Enter the integers only.")

    while True:
        op = input("Enter the operator (+,-,*,/):")
        if op not in ("+", "-", "*", "/"):
            print("Please enter the operators only.")
            continue
        else:
            break
    while True:
        try:
            b = int(input("Enter the second number:"))
            break
        except ValueError:
            print("Invalid Input! Enter the integers only.")

    if op == "+":
        print(f"{a} {op} {b} gives {a+b}")

    elif op == "-":
        print(f"{a} {op} {b} gives {a-b}")

    elif op == "*":
        print(f"{a} {op} {b} gives {a*b}")

    elif op == "/":
        print(f"{a} {op} {b} gives {a/b}")

    while True:
        choice = input("Enter if you want to continue using our calculator, Yes/No ?: ")
        if choice.lower() == "yes":
            break
        
        elif choice.lower() == "no":
            print("Thank you for using our calculator. Bye!")
            exit()

        else:
            print("Please enter either yes or no.")
            continue