from datetime import datetime
from dateutil import relativedelta

birthdate = input("Enter your birthday (yyyy-mm-dd): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
today = datetime.today().date()
diff = relativedelta(today, birthdate)
age = birthdate-today
print(age)