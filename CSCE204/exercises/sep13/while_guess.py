import random
from turtle import numinput
goal = random.randint(1,100)
print(f"The goal is {goal}")
print("Welcome to out guessing game!")
while True:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess > goal:
        print("your guess is too high")
    elif guess < goal:
        print("Your guess is too low")
    else:
        print("Yayy")
        break
    again = input("Do you want to guess again (Y)es or (N)o: ").lower().strip()
    if again == "n":
        break
print("Goodbye")