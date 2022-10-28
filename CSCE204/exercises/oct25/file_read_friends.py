def get_friends():
    friends = []
    with open("exercises/oct25/friends.txt") as file:
        for line in file:
            friend = line.strip()
            friends.append(friend)

    return friends

people = get_friends()

print("Party Time!")
while True:
    choice = input("(C)heck guests, (L)ist guests, (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "c":
        name = input("Enter Name: ")
        if name not in people:
            print("Sorry you're not invited.")
        else:
            print(f"Welcome {name}!")
    elif choice == "l":       
        for person in people:
            print(f"- {person}")
    
print("Goodbye")