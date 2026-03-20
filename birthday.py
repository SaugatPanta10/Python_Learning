from datetime import datetime

birthdate = input("Enter your birthday (yyyy-mm-dd): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
today = datetime.today().date()
age = birthdate-today
print(age)