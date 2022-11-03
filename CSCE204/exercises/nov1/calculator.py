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

def get_int(prompt):
    while True:
        try:
            num = int(input(prompt))
            break
        except ValueError:
            print("invalid whole number.")
    return num

def get_float(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            print("invalid decimal number.")
    return num

num = get_int("Enter Number: ")
factorial(num)

