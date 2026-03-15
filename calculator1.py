def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide (a,b):
    return a/b

print("Simple calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
while True:
    choice = int(input("Enter what you want to do 1-4: "))
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))

    if choice == 1:
        print("The result is:", add(a,b))
            
    elif choice == 2: 
        print("The result is:", subtract(a,b))

    elif choice == 3:
        print("The result is:", multiply(a,b))

    elif choice == 4:
        print("The result is:", divide(a,b))

    while True:
        ask = input("Do you want to continue using my calculator? Yes/No: ")
        if ask.lower() == "yes":
            break
        elif ask.lower() == "no":
            print("Thank you for using our calculator. Bye!")
            exit()
        else:
            print("Please enter either yes or no.")
            continue

        

        






