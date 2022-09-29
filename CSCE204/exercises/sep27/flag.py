import turtle
import random
turtle.bgcolor("white")
turtle.setup(1000,500)

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

stripe = turtle.window_height()//13
blue_height = stripe * 7
blue_width = int(turtle.window_width() * 0.4)

y = -turtle.window_height()//2

for i in range(7):
    pen.up()
    pen.setpos(-turtle.window_width()//2, y)
    pen.down()
    pen.begin_fill()
    for j in range(4):
        if j == 0 or j == 2:
            pen.forward(turtle.window_width())
        else:
            pen.forward(stripe)
        pen.left(90)
    pen.end_fill()
    y += stripe * 2

pen.up()
pen.setpos(-turtle.window_width()//2, turtle.window_height()//2 - blue_height)
pen.down()
pen.setheading(0)
pen.color("blue")
pen.begin_fill()
for i in range(4):
    if i % 2 == 0:
        pen.forward(blue_width)
    else:
        pen.forward(blue_height)
    pen.left(90)
pen.end_fill()

#*************************************
star_rect = blue_width // 6
star_width = star_rect //3
padding = star_width
y = turtle.window_height()//2 - blue_height + padding
x = -turtle.window_width()//2 + padding
pen.color("white")
for i in range(6):
    pen.up()
    pen.setpos(x,y)
    pen.down()

    for j in range(5):
        pen.forward(star_width)
        pen.left(144)

    x += star_rect


turtle.done()