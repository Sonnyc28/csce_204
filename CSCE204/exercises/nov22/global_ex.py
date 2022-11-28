# Use global only when you need
def replace_stars():
    global phrase
    temp = ""
    for let in phrase:
        if let == "*":
            temp += "."
        else:
            temp += let
    return temp
phrase = "*a*b*c*d"
new_sentence = replace_stars()
print(new_sentence)