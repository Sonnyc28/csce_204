def display_letters(phrase):
    for i in range(len(phrase)):
        print(phrase[i])
def display_star_phrase(phrase):
    for i in range(len(phrase)):
        if phrase[i] == " ":
            print(" ", end="")
        else:
            print("*", end= "")
    print()
def in_phrase(phrase, letter):
    for let in phrase:
        if let.lower() == letter.lower():
            return True 
    return False
display_letters("Happy Thanksgiving")
display_star_phrase("Happy Thanksgiving")
if in_phrase("I love juice", "J"):
    print("W")
else:
    print("L")