import turtle
import random
turtle.bgcolor("black")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

def get_color():
    colors = []
    try:
        with open("exercises/nov1/colors.txt") as file:
            for line in file:
                color = line.strip()
                colors.append(color)
                """
                if line.strip() != "":
                    colors.append(line.strip())
                """
    except FileNotFoundError:
        print("Invalid file name.")

    return colors

def draw_color_strip(y, height, color):
    pen.up()
    pen.setpos(-turtle.window_width()//2, y)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    for i in range(2):
        pen.forward(turtle.window_width())
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

colors = get_color()
height = turtle.window_height()//len(colors)
y = -turtle.window_height()//2

for color in colors:
    draw_color_strip(y, height, color)
    y += height


turtle.done()