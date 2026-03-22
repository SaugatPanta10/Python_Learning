from dateutil.relativedelta import relativedelta
from datetime import datetime

birthdate = input("Enter your birthday in (yyyy/mm/dd): ")
birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
today = datetime.today().date()

diff = relativedelta(today, birthdate)

print(f"Age: {diff.years} years, {diff.months} months, {diff.days} days")