from datetime import datetime

birthdate = input("Enter your birthday (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()

today = datetime.today().date()

next_birthday = birthdate.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days

print(f"Days until your next birthday: {days_left}")