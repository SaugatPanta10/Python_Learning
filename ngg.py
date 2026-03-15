import random 
while True:
    print("Welcome to my game")
    sn = random.randint(1,10)
    attempt = 0
    print("I have choosen a number from 1 to 10. Let's see if you can guess.")
    while True:
        try:
            guess = int (input("Guess a number: "))
        except ValueError:
            print("Invalid Input! Please enter numbers only.")
            continue
        attempt += 1
        if guess > sn:
            print("Your guess is bigger than the actual number. Please guess smaller number.")
            continue
        if guess < sn: 
            print("Your guess is smaller than the actual number. Please guess higher number.")
            continue
        else:
            print(f"{guess} is correct. You guessed in {attempt} attempts.")
            break
    while True:
        choice = input("Do you want to continue playing the game ? Yes/No: ").strip().lower()
        if choice == "yes":
            break

        elif choice == "no":
            print("Thank you for playing our game. Please come back soon.")
            exit()
        
        else:
            print("Please enter either yes or no.")
            continue