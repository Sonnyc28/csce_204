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

def draw_house(x, y, width, siding_color, roof_color, door_color):
    draw_square(x, y, width, siding_color)
    draw_triangle(x-(width*0.1), y+width, width*1.2, roof_color)
    draw_rect(x + width *0.4, y, width*0.2, width*0.4, door_color)
    draw_circle(x+width*0.55, y+width*0.3, width*0.025, roof_color)

def apple_tree(x, y, width):
    draw_rect(x, y, width, width*4, "brown")
    draw_circle(x+width/2, y+width*3.5, width*2, "green")
    draw_circle(x+width/4, y+width*4.5, width/4, "red")
    draw_circle(x+width*2, y+width*5.5, width/4, "red")
    draw_circle(x+width/6, y+width*5.8, width/4, "red")

x = -turtle.window_width()//2
y = 0
numHouse = 6
grid = turtle.window_width()/numHouse
padding = grid*0.2

for i in range(6):
    draw_house(x+padding, y, grid//3, "pink", "skyblue", "teal")
    apple_tree(x+padding+grid*2/3, y, grid *0.05)
    x += grid

turtle.done()