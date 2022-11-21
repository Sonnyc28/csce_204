from monster import Monster
import turtle
import random
turtle.bgcolor("skyblue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("black")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "green yellow", "gold", "coral", "violet", "silver", "spring green", "crimson", "chocolate", "khaki", "slate blue", "medium purple"]

monsters = []
for i in range(10):
    thecolor  = random.choice(colors)
    thesize = random.randint(80,120)
    x = random.randint(-turtle.window_width()//2+200, turtle.window_width()//2-200)
    y = random.randint(-turtle.window_height()//2+200, turtle.window_height()//2- 200)
    monsters.append(Monster(x,y,thesize, thecolor))

for monster in monsters:
    monster.draw(pen)

turtle.done()