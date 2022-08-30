#Author: Sonny Chen
import math

"""
# Incrementing Age
age = int(input("Enter Age: "))
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
future_age = age + 10
print(f"{first_name} {last_name}, next decade you will be {future_age}!")

#Pizza Party
print("We're having a Pizza Party")
guest = int(input("Enter the number of guests: "))
slice = float(input("Enter average slices per guest: "))
totalSlices = guest * slice
pizzas = math.ceil(totalSlices/8)
print(f"you should order {pizzas} pizzas")

#Eggs
eggs = int(input("How many eggs: "))
cartons = eggs//12
leftOver = eggs%12
print(f"You need {cartons} cartons\nYou have {leftOver} eggs left over.")
"""

#Overtime Wage
hourly = float(input("How much do you get paid per hour: "))
overtime = hourly * 1.5
print(f"You should make ${round(overtime,2)} in overtime.")