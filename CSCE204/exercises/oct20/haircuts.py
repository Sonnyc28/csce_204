def get_cut_cost(length, thickness):
    cost = 15

    if length > 4:
        cost += 10
    
    if thickness == "thick":
        cost += 10
    
    return 

print("Welcome to our salon")
length = int(input("Enter number of inches to remove: "))
thickness = input("Enter (Thick) or (Thin): ").lower().strip()

cost = get_cut_cost(length, thickness)
cost *= 1.07

print(f"your haircut costs ${round(cost,2)}")