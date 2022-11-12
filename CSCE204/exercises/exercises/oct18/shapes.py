import turtle
import random
turtle.bgcolor("black")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

def draw_square(x, y, width, color):
    pen.up()
    pen.setpos(x, y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(width)
        pen.left(90)
    pen.end_fill()

def draw_triangle(x, y, width, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    pen.end_fill()

def draw_circle(x, y, radius, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_rect(x, y, width, height, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

draw_square(-50, -50, 100, "yellow")
draw_triangle(-60, 50, 120, "sky blue")
draw_rect(-10, -50, 20, 40, "forest green")
draw_circle(5, -30, 3, "purple")

turtle.done()