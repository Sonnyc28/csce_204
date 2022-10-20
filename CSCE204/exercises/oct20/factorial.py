def factorial(num):
    ans = 1

    for i in range(1,num+1):
        ans *= i

    return ans #seds the answer to the calling function

result = factorial(5)
print(f"5! = {result}")