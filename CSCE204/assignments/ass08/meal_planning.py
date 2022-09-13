import random
print("Shall we eat?")
while True:
    meal = input("(B)reakfast, (L)unch, (D)inner, or (Q)uit:").lower().strip()
    if meal == "b":
        choice = random.randint(1,3)
        if choice == 1:
            food = "pancake"
        elif choice == 2:
            food = "waffle"
        elif choice == 3:
            food = "cereal"
        print(f"You should have: {food}")
    elif meal == "l":
        choice = random.randint(1,3)
        if choice == 1:
            food = "sandwich"
        elif choice == 2:
            food = "hotdog"
        elif choice == 3:
            food = "leftovers"
        print(f"You should have: {food}")
    elif meal == "d":
        choice = random.randint(1,3)
        if choice == 1:
            food = "steak"
        elif choice == 2:
            food = "pasta"
        elif choice == 3:
            food = "leftovers"
        print(f"You should have: {food}")
    elif meal == "q":
        break
print("Goodbye")