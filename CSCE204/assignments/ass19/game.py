# Author: Sonny Chen
import random

def get_score():
    scores = []
    try:
        with open("assignments/ass19/scores.txt") as file:
            for line in file:
                num = int(line.strip())
                scores.append(num)
        return scores
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")
        return 0
    except ValueError:
        print("Sorry, there is not a number in this file")

def save_scores(scores):
    try:
        #w for overwrite
        #a for append
        with open("assignments/ass19/scores.txt", "w") as file:
            for i in scores:
                file.write(f"{i}\n")
    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")

def play_round():
    hands = ['rock', 'paper', 'scissors']
    com = random.choice(hands)
    user = input("Enter rock, paper, scissors: ").lower().strip()
    print(f"You picked {user} and the computer picked {com}")
    if com == user:
        print("It was a tie!")
        return 0
    elif user == "rock":
        if com == "paper":
            print("Paper covers rock!")
            return -1
        else:
            print("Rock smashes scissors!")
            return 1

    elif user == "paper":
        if com == "rock":
            print("Paper covers rock!")
            return 1
        else:
            print("Scissor cuts paper!")
            return -1

    elif user == "scissors":
        if com == "paper":
            print("Scissor cuts paper!")
            return 1
        else:
            print("Rock smashes scissors!")
            return -1
    


score = get_score()
while True:
    choice = input("(P)lay pr (Q)uit: ").lower().strip()
    if choice == 'p':
        point = play_round()
        if point == 1:
            score[0] += 1
        elif point == -1:
            score[1] += 1
    elif choice == 'q':
        break

save_scores(score)
print(f"Your score: {score[0]}\nComputer score: {score[1]}")