#Author: Sonny Chen
from chocolate_bar import ChocolateBar

def get_bars():
    bars = []
    try:
        with open("assignments/ass22/chocolate_bars.txt") as file:
            for line in file:
                data = line.split(',')
                title = data[0].strip()
                calories = data[1].strip()
                fat = data[2].strip()
                saturatedFat = data[3].strip()
                protein = data[4].strip()
                carbs = data[5].strip()
                sodium = data[6].strip()
                calcium = data[7].strip()
                nut = data[8].strip()
                bar = ChocolateBar(title, calories, fat, saturatedFat, protein, carbs, sodium, calcium, nut)
                bars.append(bar)

    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")
    except ValueError:
        print("Sorry, the file is not formatted properly.")
    return bars

bars = get_bars()

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