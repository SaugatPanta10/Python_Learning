balance = 1000
while True:
    print("-----------------------")
    print("Welcome to Nabil Bank")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("-----------------------")

    while True:
        choice = input("Enter the option above 1/2/3/4 : ")
        if choice not in ("1", "2", "3", "4"):
            print("Invalid input! Please enter either 1 or 2 or 3 or 4.")
            continue

        if choice in ("1", "2", "3", "4"):
            if choice == "1":
                print(f"Your current balance is {balance}.")
                break

            elif choice == "2":
                while True:
                    dep = int(input("Enter the amount that you want to deposit: "))
                    if dep>=0:
                        balance = balance + dep
                        print(f"{dep} successfully deposited.")
                        print(f"Your current balance is {balance}.")
                        break
                    else:
                        print("Invalid Input! Please enter positive amount.")
                        continue

                
            elif choice == "3":
                while True:
                    wit = int(input("Enter the amount that you want to withdraw: "))
                    if balance>0:
                        if balance>=wit:
                            balance = balance - wit
                            print(f"{wit} successfully withdrawn.")
                            print(f"Your current balance is {balance}.")
                            break
                        else:
                            print("Insufficient amount. Please check the balance and try again.")
                            continue
                    
                    else:
                        print("Invalid Input! Please enter positive amount.")

            elif choice == "4":
                print("Thank you for using our bank. Bye")
                exit()       