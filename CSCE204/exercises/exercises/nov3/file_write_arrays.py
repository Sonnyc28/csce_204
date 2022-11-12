def save_pets(pets):
    try:
        with open("exercises/nov3/pets.txt", "w") as file:
            for pet in pets:
                file.write(f"{pet}\n")
    except FileNotFoundError:
        ("Sorry, we could not save your pets")

def get_pets():
    pets = []
    try:
        with open("exercises/nov3/pets.txt") as file:
            for line in file:
                pet = line.strip()
                pets.append(pet)
    except FileNotFoundError:
        ("Sorry, we could not save your pets")
    return pets

my_pets = get_pets()

while True:
    choice = input("(V)iew pets, (A)dd pet, (D)elete pet, (Q)uit: ").lower().strip()
    if choice == "v":
        for pet in my_pets:
            print(pet)
    elif choice == "a":
        pet = input("Enter pet: ").strip()
        my_pets.append(pet)
    elif choice == "d":
        pet = input("Enter pet: ").strip()
        for p in my_pets:
            if p.lower() == pet:
                my_pets.remove(p)
    elif choice == "q":
        break
save_pets(my_pets)