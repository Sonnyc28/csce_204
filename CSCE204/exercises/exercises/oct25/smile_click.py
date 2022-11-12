import turtle
import random
turtle.bgcolor("white")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

def draw_smiley_face(x,y):
    width = 50
    draw_circle(x,y,width, "yellow")
    draw_circle(x-width/5, y + width * 0.05, width/6, "black")
    draw_circle(x+width/5, y + width * 0.05, width/6, "black")
    draw_smile(x, y-width*0.3, width*0.5, "black")

def draw_circle(x, y, width, color):
    pen.up()
    pen.setpos(x,y-width//2)
    pen.down()
    pen.color(color)
    pen.begin_fill()
    pen.circle(width//2)
    pen.end_fill()

def draw_smile(x, y, width, color):
    num = random.randint(0,1)
    if num == 0:
        pen.up()
        pen.setpos(x - width*0.8, y + width*0.3)
        pen.down()
        pen.setheading(-60)
        pen.color(color)
        pen.circle(width*0.8, 120)
        pen.setheading(0)
    else:
        pen.up()
        pen.setpos(x + width * 0.7, y + width * - 0.1)
        pen.down()
        pen.color(color)
        pen.setheading(120)
        pen.circle(width*0.8, 120)
        pen.setheading(0)

turtle.onscreenclick(draw_smiley_face)

turtle.done()