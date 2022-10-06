from datetime import date, datetime
birthdays = [date(2022, 12, 30),
             date(2022, 10, 21),
             date(2023, 2, 5),
             date(2023, 8, 6),
             date(2023, 5, 28)]

#loop through and display birthdays
for bday in birthdays:
    #print(bday.strftime(" - %a %b %d"))
    num_days = (bday - date.today()).days
    print(bday.strftime("%b %d"), end="")
    print(f" - is in {num_days} days")