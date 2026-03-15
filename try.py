while True: 
    try:
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        result = a//b
        print(f"When divided {a} by {b}, The result is: {result}")
        break
    except ZeroDivisionError:
        print("cannot divide by 0. Please enter another value.")
    except ValueError:
        print("Invalid input. Please enter integers only. ")
