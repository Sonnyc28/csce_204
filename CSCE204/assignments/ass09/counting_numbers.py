#Author: Sonny Chen
print("Let's Count!")
start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

count = 0
for i in range(start,end+1):
    if i == end:
        print(i)
    else:
        print(f"{i}, ", end='')
    count += 1
print(f"There are {count} numbers.")
