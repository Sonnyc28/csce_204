print("Color Party!")
while True:
    guess = input("Guess my favorite color: ").lower().strip()
    if guess == "blue":
        print("YAY!!!")
        break #Kicks you out of the loop

    print("Wrong!")
    again = input("Do you want to guess again (Y)es or (N)o: ").lower().strip()
    if again == "n":
        break

print("Goodbye")