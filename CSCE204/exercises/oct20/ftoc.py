def f_to_c(fahrenheit):
    celcius = (fahrenheit -32) * 5/9
    return celcius

def c_to_f(celcius):
    fahrenheit = celcius * 9/5 + 32
    return fahrenheit

def miles_to_kilo(miles):
    kilo = miles * 1.60934
    return kilo

def kilo_to_miles(kilo):
    return kilo * 0.621371

print("Conversion Program")
while (True):
    choice = input("Enter type of conversion, or (Q)uit\n 1. Fahrenheit to Celcius\n 2. Celcius to Fahrenheit\n 3. Miles to Kilometers\n 4. Kilometers to Miles\n")
    if choice == "Q" or choice == "q":
        break
    if int(choice) == 1:
        num = int(input("Enter Fahrenheit: "))
        c = f_to_c(num)
        print(f"{num} F = {c} C")
    elif int(choice) == 2:
        num = int(input("Enter Celcius: "))
        f = c_to_f(num)
        print(f"{num} C = {f} F")
    elif int(choice) == 3:
        num = int(input("Enter Miles: "))
        k = miles_to_kilo(num)
        print(f"{num} miles = {k} kilometers")
    elif int(choice) == 4:
        num = int(input("Enter Kilometers: "))
        m = kilo_to_miles(num)
        print(f"{num} kilometers = {m} miles")