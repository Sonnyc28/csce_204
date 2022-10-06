#Author: Sonny Chen
import math

#These are the constants
textbooks = 64.99
dorm = 184.99
breakfast = 3.85
lunch = 8.95
dinner = 12.79

#Getting information from user
days = int(input("How many days are you budgetting for: "))
books = int(input("How many books do you need: "))

#Calculatng the price per week
weeks = math.ceil(days/7)
dormCost = 184.99 * weeks
texbooksNeeded = textbooks * books
breakfastCost = breakfast * days
lunchCost = lunch * days
dinnerCost = dinner * days

totalCost = (dormCost + texbooksNeeded + breakfastCost + lunchCost + dinnerCost) * 1.07
print(f"Total Expenses: ${round(totalCost,2)}")