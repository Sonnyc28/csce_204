def get_friends():
    friends = []
    with open("exercises/oct25/friends.txt") as file:
        for line in file:
            friend = line.strip()
            friends.append(friend)

    return friends

people = get_friends()
for person in people:
    print(f"- {person}")