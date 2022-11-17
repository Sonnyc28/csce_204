from question import Question
import random

def get_questions():
    questions = []
    try:
        with open("exercises/nov15/questions.txt") as file:
            for line in file:
                data = line.split(',')
                prompt = data[0].strip()
                answer1 = data[1].strip()
                answer2 = data[2].strip()
                answer3 = data[3].strip()
                answer4 = data[4].strip()
                correct_answer = int(data[5].strip())
                question = Question(prompt, answer1, answer2, answer3, answer4, correct_answer)
                questions.append(question)

    except FileNotFoundError:
        print("Sorry, your file doesn't exist.")
    except ValueError:
        print("Sorry, the file is not formatted properly.")
    return questions

print("Welcome to our trivia game")
score = 0
while True:
    choice = input("Would you like to (P)lay or (Q)uit: ").lower().strip()
    if choice == "q":
        break
    elif choice == "p":
        question = random.choice(get_questions())
        print(question.prompt)
        question.display_answers()
        ans = int(input("Enter answer number: "))
        if question.is_correct(ans):
            print("Yay, you are correct!")
            score += 1
        else:
            print("Incorrect")

print(f"Your score is {score}\nGoodbye")