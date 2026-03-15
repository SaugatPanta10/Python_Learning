while True: 
    while True:
        try:
            a = int(input("Enter the value of a: "))
            break
        except ValueError:
            print("Invalid Input ! please enter numbers only.")
       
    print(f"The square of a is {a*a} ")
    choice = input("Please enter if you want to continue the program: Yes/No?: ")
    if choice.lower() == "yes":
        continue
    elif choice.lower() == "no":
        print("Thank you for choosing us. Bye!")
        break
    else:
        print("Please enter either yes or no.")
