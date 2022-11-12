number = -2
while True:
    try:
        number = int(input("Enter a whole number:"))
        break
    except ValueError:
        print("Sorry, not a valid number.")

print(f"Your number is {number}")