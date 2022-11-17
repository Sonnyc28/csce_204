from product import Product

shoppingList = []
shoppingList.append(Product("Converse Shoes", "Tan and black walking shoes", 29.99))
shoppingList.append(Product("Baby Doll", "Walking and talking doll", 19.99))
shoppingList.append(Product("Gym Bag", "Blue duffle bag", 45.99))

total = 0

print("Your shopping list: ")
for item in shoppingList:
    item.display()
    total += item.get_cost()

print(f"Total Cost: ${round(total,2)}")