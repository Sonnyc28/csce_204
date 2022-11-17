class Product:
    def __init__(self, title, description, price):
        self.title = title
        self.description = description
        self.price = price
    
    def get_cost(self):
        return self.price * 1.07 #tax
    
    def display(self):
        print(f"""
            *** {self.title} ***
            {self.description}
            Cost: {self.get_cost()}""")