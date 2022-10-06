from datetime import date, datetime
birthdays = {
    "Amy": date(2022, 12, 30),
    "Bobby": date(2023, 1, 12),
    "Carl": date(2023, 4, 23),
    "Dave": date(2023, 6, 12),
    "Eric": date(2023, 9, 18)
}

for friends in birthdays:
    print(f"{friends} - ", end="")
    print(birthdays[friends].strftime("%m/%d"), end="")
    num_days = (date.today() - birthdays[friends]).days
    print(f"- {num_days} days")