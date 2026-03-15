import random 
while True:
    print("Welcome to the Number Guessing Game!")
    sn = random.randint(1,20)
    print("I have choosen a number between 1 and 20. Lets see if you can guess.")
    attempt = 0
    while True:
        try:
            guess = int(input("Try to guess a number: "))
        except ValueError:
            print("Invalid Input! Please enter numbers only.")
            continue
        attempt += 1
        if guess<sn:
            print("The number you guess is lower. Try guessing higher number.")
            continue
        elif guess>sn:
            print("The number you guess is higher. Try guessing lower number.")
            continue
        else:
            print(f"Congratulations. Your guess is correct in {attempt} attempts.")
            break

    while True:
        choice = input("Do you want to continue playing our game? Yes/No: ")
        if choice.lower() == "yes":
            break
        elif choice.lower()== "no":
            print("Thank you for playing our game. Please come back soon.")
            exit()
        else:
            print("Please enter either yes or no!")
            continue

