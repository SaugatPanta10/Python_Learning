balance = 1000
while True:
    print("Welcome to Nabil Bank")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    while True:
        choice = (input("Enter the option above 1/2/3/4 : "))
        if choice not in ("1", "2", "3", "4"):
            print("Invalid input! Please enter either 1 or 2 or 3 or 4.")
            continue

        if choice in ("1", "2", "3", "4"):
            if choice == "1":
                print(f" Your current balance is {balance}.")
                break

            elif choice == "2":
                dep = int(input("Enter how much of money you would like to deposit: "))
                balance = balance + dep
                print(f"{dep} successfully deposited.")
                print(f" Your current balance is {balance}.")
                break
                
            elif choice == "3":
                wit = int(input("Enter the amount that you want to withdraw: "))
                balance = balance - wit
                print(f"{wit} successfully withdrawn.")
                print(f"Your current balance is {balance}.")
                break

            elif choice == "4":
                print("Thank you for using our bank. Bye")
                exit()

    while True:
        ask = input("Do you want to continue our banking service? Yes/No: ").strip().lower()
        if ask == "yes":
            break

        elif ask == "no":
            print("Thank you for using our bank. Bye!")
            exit()

        else:
            print("Invalid input! Please enter either yes or no. ")            