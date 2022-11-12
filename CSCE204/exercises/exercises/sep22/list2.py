from hashlib import new


colors = ["pink", "purple", "blue", "red", "orange"]
print("Welcome to our color fun program!")

while True:
    option = input("(V)iew, (A)dd, (R)emove, or (Q)uit:").lower().strip()

    if option == "q":
        break
    elif option == "v":
        for i in range(len(colors)):
            print(f"- {colors[i]}")
    elif option == "a":
        new_color = input("Enter Color: ")
        colors.append(new_color)
    elif option == "r":
        color = input("Enter Color: ")
        colors.remove(color)
        print(f"{color} was removed")
    else:
        print("Invalid input")
    
print("Goodbye")