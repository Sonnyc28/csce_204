import random

def roll():
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print(f"You rolled a {d1} and a {d2}")
    ans = d1 + d2
    if ans == 7:
        print("You are lucky")
    else:
        print(f"{ans} is Not 7\nYou are not lucky")

print("Let's Pay Lucky Sevens")
while (True):
    choice = input("(R)oll or (Q)uit: ").strip().lower()
    if choice == "q":
        break
    if choice == "r":
        roll()
    else:
        print("Invalid Command")
        continue #does to the beginning of loop
print("goodbye")