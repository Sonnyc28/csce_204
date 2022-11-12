from webbrowser import get


def get_mood(color):
    mood_chart = {
        "red":"angry",
        "yellow":"mellow",
        "blue":"sad",
        "green":"happy",
        "black":"scared",
        "purple":"royal",
        "pink":"fun"
    }

    color = color.lower().strip()
    if color not in mood_chart:
        return "not moody"
    else:
        return mood_chart[color]

ans = input("Let's find out your mood\nEnter Color: ")
print("You are feeling", get_mood(ans))