#Author: Sonny Chen
from chocolate_bar import ChocolateBar
bars = []
bars.append(ChocolateBar("Almond Joy", "232", "14g", "8.5g", "2.5g", "29g", "67mg", "39.5mg", True))

bars.append(ChocolateBar("Butterfinger", "216", "8.5g", "4.5g", "5.5g", "29.5g", "89mg", "12mg", True))

bars.append(ChocolateBar("Kit Kat", "220.5", "12.5g", "7.5g", "3g", "26.5g", "43.5mg", "77.5mg", False))

bars.append(ChocolateBar("M&M's", "242.5", "12.5g", "5g", "4.5g", "28.5g", "22.5mg", "47.5mg", True))

bars.append(ChocolateBar("Reese's Penut Butter Cups", "222", "14.5g", "6.5g", "5g", "22g", "6130.5mg", "35mg", True))

bars.append(ChocolateBar("Snickers", "273", "14g", "5g", "4.5g", "34g", "151.5mg", "53.5mg", True))

while True:
    choice = input("(L)ist all Chocolate Bars, (D)etails, or (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "l":
        for bar in bars:
            bar.theTitle()
    elif choice == "d":
        user = input("Enter Chocolate Bar name: ")
        for bar in bars:
            if bar.title.lower() == user.lower():
                print(bar.display())
    else:
        print("Invalid input")
print("Goodbye")