import random
def deal():
    pCards = []
    cCards = []
    for i in range(2):
        d1 = random.randint(1,13)
        d2 = random.randint(1,13)
        if d1 or d2 == "1":
            value1 = "ace"
        if d1 or d2 == "11":
            value1 = "jack"
            d1,d2 = 10
        if d1 or d2 == "12":
            value1 = "queen"
            d1,d2 = 10
        if d1 or d2 == "13":
            value1 = "king"
            d1,d2 = 10
        value1 = d1
        value2 = d2
        pCards.append(value1)
        cCards.append(value2)
        d1 += d1
        d2 += d2
    sums = [d1, d2]
    pScore = 0
    cScore = 0
    print(f"Computer deals 2 cards: {cCards[1]} and {cCards[2]}")
    print(f"You deal 2 cards: {pCards[1]} and {pCards[2]}")
    if sums[0] > sums[1]:
        print("You won this round!")
        pScore += 1
    if sums[0] < sums[1]:
        print("Computer won this round!")
        cScore += 1
    return pScore, cScore
def scores(pScore,cScore):
    print(f"Your points: {pScore}\nComputer points: {pScore}")

print("Welcome to our Awesome Card Game")
while (True):
    choice = input("Would you like to play a round (Y)es or (N)o? ").lower().strip()
    if choice == "no":
        deal(scores())
        break
    if choice == "yes":
        break