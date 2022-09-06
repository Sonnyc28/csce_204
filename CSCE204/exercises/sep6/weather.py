print("What to wear")
temp = float(input("Enter Temp: "))
wet = input("Enter Percipitation (r), (s), (n): ").strip().lower()
if temp <= 32 and wet == "s":
    print("waer a snowsuit")
elif temp <= 70 and wet == "r":
    print("waer a rain jacket")
elif temp >= 80 and wet == "r":
    print("waer a swimsuit")
else:
    print("You Choose")