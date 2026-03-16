pas = input("Create your password: ")
while True:
    password = input("Enter your password you just set: ")
    if pas == password:
        print("Logged in. ")
        break
    else:
        print("Incorrect password. Please try it again.")
        

