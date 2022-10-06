print("Color Party!")
color = input("Guess my favorite color: ").lower().strip()
while color != "blue":
    print("Wrong!")
    color = input("Guess again: ").lower().strip()

print("Yay!\nGoodbye")