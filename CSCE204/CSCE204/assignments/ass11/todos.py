#Author: Sonny Chen
print("Tasks")
todo = []
#find a way to get rid of break
while True:
    choice = input("Do you want to (V)iew, (A)dd, (R)emove, or (Q)uit:").lower().strip()

    if choice == "q":
        break

    elif choice == "v":
        print("Todo list: ")
        if len(todo) == 0:
            print("Yay! you have nothing todo!")
        for i in range(len(todo)):
            print(f"- {todo[i]}")

    elif choice == "a":
        new = input("Enter todo name: ")
        todo.append(new)

    elif choice == "r":
        option = input("Enter todo name: ")
        if option in todo:
            todo.remove(option)
            print(f"{option} was removed")
        else:
            print(f"{option} isn't in your list")

    else:
        print("Invalid input")