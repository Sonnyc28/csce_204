#Author: Sonny Chen

month = input("Enter your Birth Month: ").lower().strip()
day = int(input("Enter your Birth Day: "))

if (month == "december" and day >= 22) or (month == "january" and day <= 21):
    starRock = "Capricorn: Ruby"

elif (month == "january" and day >= 22) or (month == "february" and day <= 21):
    starRock = "Aquarius: Garnet"

elif (month == "february" and day >= 22) or (month == "march" and day <= 21):
    starRock = "Pisces: Amethyst"

elif (month == "march" and day >= 21) or (month == "april" and day <= 20):
    starRock = "Aries: Bloodstone"

elif (month == "april" and day >= 21) or (month == "may" and day <= 21):
    starRock = "Taurus: Sapphire"

elif (month == "may" and day >= 22) or (month == "june" and day <= 21):
    starRock = "Gemini: Agate"

elif (month == "june" and day >= 22) or (month == "july" and day <= 22):
    starRock = "Cancer: Emerald"

elif (month == "july" and day >= 23) or (month == "august" and day <= 22):
    starRock = "Leo: Onyx"

elif (month == "august" and day >= 23) or (month == "september" and day <= 22):
    starRock = "Virgo: Carnelian"

elif (month == "september" and day >= 23) or (month == "october" and day <= 23):
    starRock = "Libra: Peridot"

elif (month == "october" and day >= 24) or (month == "november" and day <= 21):
    starRock = "Scorpio: Emerald or Aquamarine"

elif (month == "november" and day >= 22) or (month == "december" and day <= 21):
    starRock = "Sagittarius: Topaz"

print(starRock + "\nHave a nice day")