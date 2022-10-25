import random
toys = {
    "doll": 19.89,
    "car": 1.99,
    "truck": 7.85,
    "puzzle": 14.98,
    "stinky": 2
}
a = random.choice(toys)
print(a)
print(f"A truck costs: ${toys['truck']}")

#add an item to the dictionary
toys["yo-yo"] = 4.5

#Loop through and siplay all the toys in the dictionary
for toy_name in toys:
    print(f"{toy_name} costs ${toys[toy_name]}")