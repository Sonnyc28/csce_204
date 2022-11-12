#from (fileName) import (ClassName)
from person import Person
"""
friend1 = Person("Ashley", "Sims", "803-566-4545")
friend2 = Person("Tim", "Tracey", "803-433-7676")

friend1.display()
friend2.display()
"""

def display_people(people):
    for friend in people:
        friend.display()

people = []
people.append(Person("Ashley", "Sims", "803-566-4545"))
people.append(Person("Tim", "Tracey", "803-433-7676"))
people.append(Person("Eric", "Hart", "803-438-3957"))

display_people(people)

first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()

for person in people:
    if person.first_name.lower() == first_name.lower():
        print(person.get_phone_number())