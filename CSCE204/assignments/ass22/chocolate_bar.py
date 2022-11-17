class ChocolateBar:
    def __init__(self, title, calories, fat, saturatedFat, protein, carbs, sodium, calcium, nuts):
        self.title = title
        self.calories = calories
        self.fat = fat
        self.saturatedFat = saturatedFat
        self.protein = protein
        self.carbs = carbs
        self.sodium = sodium
        self.calcium = calcium
        self.nuts = nuts

    def theTitle(self):
        print(f"- {self.title}")
    
    def display(self):
        print(f"*** {self.title} ***\n- calories: {self.calories}\n- fat: {self.fat}\n- saturated fat: {self.saturatedFat}\n- protein: {self.protein}\n- carbohydrates: {self.carbs}\n- sodium: {self.sodium}\n- calcium: {self.calcium}\n- nuts: {self.nuts}")

    def is_match(self, title):
        if self.title == title:
            return True
        else:
            return False