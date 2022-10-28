def get_phone_book():
    phonebook = {}

    #read file and put in phone book
    with open("exercises/oct27/phones.txt") as file:
        for line in file:
            if line.strip() == "":  # if the line is empty do nothing with it
                continue
            friend_digits = line.split(",")
            friend = friend_digits[0].strip().lower()
            digits = friend_digits[1].strip()
            phonebook[friend] = digits

    return phonebook

def display_phonebook(phonebook):
    for name in phonebook:
        print(f"{name} : {phonebook[name]}")

def display_phone_number(phonebook, name):
    name = name.lower()
    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}")
    else:
        print(f"Sorry, {name} isn't in out phonebook")

phonebook = get_phone_book()

print("Phone System")
while True:
    choice = input("(V)iew, (N)umber, or (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "v":
        display_phonebook(phonebook)
    elif choice == "n":
        friend = input("Enter friend name: ").lower().strip()
        display_phone_number(phonebook, friend)