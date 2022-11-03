import turtle
import random
turtle.bgcolor("sky blue")
turtle.setup(1000,500)

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

#get candies func
def get_candies():
    candies = []
    try:
        with open("assignments/ass18/scene.txt") as file:
            for line in file:
                if line.strip() != "":
                    candies.append(line.strip())
    except FileNotFoundError:
        print("Invalid file name.")

    return candies
    
#draw mint func
def draw_mint(x, y, size):
    pen.up()
    pen.setpos(x, y)
    pen.down()
    pen.color("white")
    pen.begin_fill()
    pen.setheading(150)
    for i in range(3):
        pen.forward(size * 5)
        pen.left(120)
    pen.setheading(30)
    for i in range(3):
        pen.forward(size * 5)
        pen.right(120)
    pen.end_fill()

    cirSize = size//2
    pen.color("white")
    pen.fillcolor("red")
    pen.begin_fill()
    pen.setheading(0)
    for i in range(5):
        pen.up()
        pen.setpos(x, y - cirSize)
        pen.down()
        pen.circle(cirSize)
        cirSize += size//2
        y -= size//20
    pen.end_fill()

#draw lollipop func
def draw_lollipop(x,y,size):
    pen.up()
    pen.setpos(x-size//6,y - size*3)
    pen.down()
    pen.color("brown")
    pen.begin_fill()
    for i in range(2):
        pen.forward(size//3)
        pen.left(90)
        pen.forward(size*8)
        pen.left(90)
    pen.end_fill()

    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color("white")
    pen.fillcolor("misty rose")
    pen.begin_fill()
    cirSize = size//2
    pen.setheading(0)
    for i in range(5):
        pen.up()
        pen.setpos(x, y+size*3)
        pen.down()
        pen.circle(cirSize)
        cirSize += size//2
        y -= size//2
    pen.end_fill()

spacing = turtle.window_width()//6
x = -turtle.window_width()//2 + spacing//2
"""
for i in range(3):
    draw_mint(x, 0, 10)
    x += spacing
    draw_lollipop(x, 0, 10)
    x += spacing
"""
candies = get_candies()
for candie in candies:
    if candie == "lollipop":
        draw_lollipop(x, 0, 10)
    elif candie == "mint":
        draw_mint(x, 0, 10)
    x+= spacing

turtle.done()