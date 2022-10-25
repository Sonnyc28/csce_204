import turtle
import random
turtle.bgcolor("skyblue")
turtle.setup(1500,750)

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)
turtle.colormode(255)

roadHeight = turtle.window_height()//5
pen.up()
pen.setpos(-turtle.window_width()//2 , turtle.window_height()//2 - roadHeight)
pen.color("burlywood")
pen.down()
pen.begin_fill()
for i in range(2):
    pen.forward(turtle.window_width())
    pen.right(90)
    pen.forward(roadHeight * 3)
    pen.right(90)
pen.end_fill()

def drawBike(x,y):
    boxWidth = turtle.window_width()//3
    bikeLine = boxWidth//6
    smallLine = bikeLine * 5/8
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "green yellow", "gold", "coral", "violet", "silver"]
    thecolor  = random.choice(colors)
    
    pen.up()
    pen.setpos(x,y)
    pen.down()

    #Draw bikes
    pen.setheading(0)
    pen.color("black")
    pen.circle(bikeLine // 3)
    pen.up()
    pen.setpos(x,y+bikeLine // 3)
    pen.color(thecolor)
    pen.down()
    pen.left(60)
    pen.forward(bikeLine)
    pen.right(60)
    pen.forward(bikeLine * 3/8)
    pen.right(180)
    pen.forward(bikeLine * 3/8)
    pen.left(60)
    pen.forward(bikeLine * 3/8)
    pen.left(120)
    for k in range(3):
        pen.forward(smallLine)
        pen.right(120)
    pen.forward(smallLine)
    pen.right(60)
    for k in range(3):
        pen.forward(smallLine)
        pen.right(120)
    pen.setheading(0)
    pen.left(60)
    pen.forward(smallLine * 1/3)
    pen.right(60)
    pen.forward(smallLine * 1/3)
    pen.right(180)
    pen.forward(smallLine * 1/3 * 2)
    pen.up()
    pen.setpos(x + smallLine * 2,y+bikeLine // 3 *2)
    pen.down()
    pen.color("black")
    pen.circle(bikeLine // 3)

turtle.onscreenclick(drawBike)

turtle.done()