while True:
    try:
        mpin = int(input("Create your 4 digit mpin: "))
        break
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

balance = 0
dep = int(input("Enter the amount that you want to deposit: "))
if dep>0:
    balance += dep
    print(f"{dep} deposited successfully.")
    print(f"Your new balance is {balance}")

else:
    print("Invalid Input! Please enter positive amount")

print("Your transaction for this product is pending.")
 
ask = input("Enter if you want to make payment for this transaction? Yes/No: ").strip().lower()
if ask == "yes":
    while True:
        askk = int(input("Enter the amount to be paid: "))
        if askk>0:
            while True: 
                mpinn = int(input("Enter your mpin: "))
                if mpinn == mpin:
                    balance = balance-askk
                    print(f"{askk} paid successsfully.")
                    print(f"Your new balance is {balance}")
                    print(f"Remaining dues cleared thank you.")
                    break
                else: 
                    print("Incorrect pin. Please try again.")
                    continue
            break
            
        
        else:
            print("Invalid input! Please enter positive amount.")
            continue

elif ask == "no":
    print("Thank you for using esewa.")
    exit()

else:
    print("Invalid input! Please enter either yes or no.")