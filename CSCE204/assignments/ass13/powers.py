# Author: Sonny Chen
def displayPowers(num):
    for i in range(0,11):
        math = (num ** i)
        print(f"{num}^{i} = {math}")

while (True):
    choice = input("(L)ist Powers, or (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "l":
        num = int(input("Enter Number: "))
        displayPowers(num)
    else:
        break

print("Goodbye")
        