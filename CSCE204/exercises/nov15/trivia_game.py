from question import Question
import random

questions = []
questions.append(Question("What type of animal is a seahorse?", "Crustacean", "Arachnid", "Fish", "Shell", 2))
questions.append(Question("Which of the following dog breeds is the smallest?", "Dachshund", "Poodle","Pomeranian","Chicuahua", 3))
questions.append(Question("What color are zebras?","White with black stripes","Black with white stripes", "Both of the above", "None of the above", 1))
questions.append(Question("What existing bird has the longest wingspan?","Stork", "Swan","Condor","Albatross", 3))

print("Welcome to our trivia game")
score = 0
while True:
    choice = input("Would you like to (P)lay or (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "p":
        question = random.choice(questions)
        print(question.prompt)
        question.display_answers()
        ans = int(input("Enter answer number: "))
        if question.is_correct(ans):
            print("Yay, you are correct!")
            score += 1
        else:
            print("Incorrect")

print(f"Your score is {score}\nGoodbye")