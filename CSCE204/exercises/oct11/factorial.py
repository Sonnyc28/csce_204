def factorial(num):
    answer = 1
    for i in range(1, num+1):
        answer *= i
    print(f"{num}! = {answer}")

#call the function
user_num = int(input("Enter number:"))
factorial(user_num)
