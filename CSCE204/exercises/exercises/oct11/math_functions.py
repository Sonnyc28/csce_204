def factorial(num):
    answer = 1
    for i in range(1, num+1):
        answer *= i
    print(f"{num}! = {answer}")

def sum(num):
    answer = 0
    for i in range(1, num+1):
        answer += i
    print(f"Sum of 1 to {num} = {answer}")

def sum_range(start, finish):
    answer = 0
    for i in range(start, finish+1):
        answer += i
    print(f"Sum of {start} to {finish} = {answer}")

print("Playing With Numbers")

while (True):
    choice = input("(F)actorial, (S)um, sum or (R)ange, or (Q)uit: ").strip().lower()

    if choice == "q":
        break

    elif choice == "f":
        num = int(input("Enter Number: "))
        factorial(num)

    elif choice == "s":
        num = int(input("Enter Number: "))
        sum(num)

    elif choice == "r":
        start = int(input("Enter Starting Number:"))
        end = int(input("Enter Ending Numbre: "))
        sum_range(start, end)
    
    else:
        print("Invalid Input")

print("Goodbye")