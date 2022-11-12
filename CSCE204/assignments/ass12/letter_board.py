# Author: Sonny Chen
import turtle
import random
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("black")
pen.hideturtle()    #This hides the cursor
pen.speed(0)
turtle.colormode(255)
letList = []

sides = turtle.window_width()//8
space = sides//4
x = -turtle.window_width()//2 + space
y = 0
letx = x // 2

#gets letters i nlist
num = int(turtle.numinput("Letters", "Enter Number of Letters: ", 5))
for i in range(num):
    letters = turtle.textinput("Letters", "Enter Letter: ").strip().upper()
    letList.append(letters)

#draw the squares
for i in range(num):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    pen.begin_fill()
    for j in range(4):
        pen.forward(sides)
        pen.left(90)
    pen.end_fill()

    #letter
    pen.up()
    pen.setpos(x + sides//2, y + sides//2)
    pen.down()
    pen.color("black")
    pen.write(letList[i],  )

    x += sides + space

turtle.done()