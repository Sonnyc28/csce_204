from datetime import date, time, datetime

todays_date = date.today()
#print(todays_date)
print(todays_date.strftime("%B: %d - %A, %Y"))
#Thursday October 06

#Halloween
halloween = date(2022, 10, 31)
print("Halloween", end = " ")
print(halloween.strftime("%m/%d/%Y"))

class_time = time(11,40)
print("Class Time is ", end="")
print(class_time.strftime("%I:%M %p"))

pie_day = datetime(2023, 3, 14, 13, 59)
print("Pie Day is ", end="")
print(pie_day.strftime("%m.%d.%I.%M"))

birthday_text = input("Enter Birthdat (MM/DD/YYYY): ").strip()
birthday = datetime.strptime(birthday_text, "%m/%d/%Y")
print("My birthday is ", end="")
print(birthday.strftime("%b %d"))


#How long til pie day
days = pie_day - datetime.now().days
print(f"You have {days} till pie day")

