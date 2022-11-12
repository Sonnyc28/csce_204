def get_count():
    try:
        with open("exercises/nov3/count.txt") as file:
            for line in file:
                num = int(line.strip())
                return num
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")
        return 0
    except ValueError:
        print("Sorry, there is not a number in this file")

def save_count(num):
    try:
        #w for overwrite
        #a for append
        with open("exercises/nov3/count.txt", "w") as file:
            file.write(f"{num}\n")
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")

print("Let's drink Water")
num_glasses = get_count()
while True:
    choice = input("(E)nter drinks, (V)iew total, (Q)uit: ").strip().lower()
    if choice == "q":
        break
    elif choice == "e":
        drinks = int(input("How many drinks: "))
        num_glasses += drinks
    elif choice == "v":
        print(f"You have drank {num_glasses} total glasses.")

save_count(num_glasses)