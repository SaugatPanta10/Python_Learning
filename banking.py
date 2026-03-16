print("Welcome to Nabil Bank")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

balance = 1000

choice = (input("Enter the option above 1/2/3/4 : "))
if choice == "1":
    print(f" Your current balance is {balance}.")

if choice == "2":
    dep = int(input("Enter how much of money you would like to deposit: "))
    balance = balance + dep
    print(f" Your current balance is {balance}.")
    
if choice == "3":
    wit = int(input("Enter the amount that you want to withdraw: "))
    balance = balance - wit
    print(f" Your current balance is {balance}.")

if choice == "4":
    print("Thank you for using our bank. Bye")
    exit()


