import turtle
import random
turtle.bgcolor("black")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

color = ["white", "gold", "cyan", "khaki", "orange red", "orchid"]

for i in range(10):
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    width = random.randint(25,100)

    pen.up()
    pen.setpos(x-width//2, y-width//2)
    pen.down()
    star_color = random.choice(color)
    pen.color(star_color)

#draw right side up triangle
    pen.begin_fill()
    for j in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

#draw upside down triangle
    pen.setheading(0)
    pen.up()
    pen.setpos(x-width//2, y)
    pen.down()

    pen.begin_fill()
    for j in range(3):
        pen.forward(width)
        pen.right(120)
    pen.end_fill()
    pen.end_fill()

turtle.done()