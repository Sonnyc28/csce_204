# Author: Sonny Chen
def get_guests():
    guestList = {}

    with open("assignments/ass17/guest_list.txt") as file:
        for line in file:
            if line.strip() == "":
                continue
            name_guess = line.split(":")
            guest = name_guess[0].strip()
            guess = name_guess[1].strip().lower()
            guestList[guest] = guess

    return guestList

def display_guests(guestList):
    for i in guestList:
        print(f" - {i}")

def get_majority_color(guestList):
    boy = 0
    girl = 0
    for name in guestList:
        if guestList[name] == "blue":
            boy += 1
        elif guestList[name] == "pink":
            girl += 1
    if boy > girl:
        print("Blue won! People think you're having a boy!")
    elif boy < girl:
        print("Pink won! People think you're having a girl!")

guestList = get_guests()

print("Baby Shower!")
while True:
    choice = input("(G)uest List, (C)olor Winner, (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "g":
        print("Attending Guest List:")
        display_guests(guestList)
    elif choice == "c":
        get_majority_color(guestList)