print("You just got pulled over!")
speed = int(input("Enter your speed: "))

if speed >= 90:
    print("Jail Time")
elif speed >= 80:
    print("Ticket Time")
elif speed >= 70:
    print("Warning")
elif speed <= 25:
    print("Jail-Drugs?")
elif speed <= 45:
    print("Ticket Too Slow")
else:
    print("I like you")
print("Have a good day!")