while True:
    try:
        a = int(input("Enter the value of a: "))
        break  
    except ValueError:
        print("Invalid Input ! please enter numbers only.")