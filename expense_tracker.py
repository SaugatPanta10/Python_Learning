expenses = []

while True:
    amount = float(input("Enter your expense: "))
    expenses.append(amount)

    while True:
        choice = input("Do you still have more expenses? (Yes/No): ")
        if choice == "yes":
            break
        elif choice == "no":
            print("Thank you for using our program.")
            break
        else:
            print("Please enter either yes or no.")
            continue

    if choice == "no":
        break


print("Total spending: Rs", sum(expenses))