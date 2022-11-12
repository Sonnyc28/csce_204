# Author: Sonny Chen
import turtle
import random
turtle.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)
turtle.colormode(255)

#draw triangle function
def draw_triangle(x, y, width, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    #pen.begin_fill()
    for i in range(3):
        pen.forward(width)
        pen.left(120)
    #pen.end_fill()

#draw 7 layered triangle function
def draw_layered_triangle(x, y, size):
    width = size # this will be random
    for i in range(7):
        #draw_triangle(x - 10*i, y - 5*i, width + 20*i, "blue")
        r = random.randrange(0, 256)
        g = random.randrange(0, 256)
        b = random.randrange(0, 256)
        thecolor = pen.color(r,g,b)
        draw_triangle(x - width//5*i, y - width//7.5*i, width + width//2.5*i, thecolor)

#draw 20 layered triangles
x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
size = random.randint(15, 50)

for i in range(20):
    draw_layered_triangle(x, y, size)
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    size = random.randint(15, 50)

turtle.done()