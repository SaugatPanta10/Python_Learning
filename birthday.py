from datetime import datetime
from dateutil import relativedelta

birthdate = input("Enter your birthday (yyyy-mm-dd): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
today = datetime.today().date()
diff = relativedelta.relativedelta(today, birthdate)
print(f"Your age is {diff.years} years, {diff.months} months, {diff.days} days")