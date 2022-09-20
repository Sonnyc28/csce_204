#Author: Sonny Chen
import turtle
turtle.bgcolor("black")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

width = turtle.window_width()//20

spacing = turtle.window_width()//10
x = -turtle.window_width()//2 + spacing//2

num = int(turtle.numinput("Stars", "How Many Stars"))
for i in range(num):
    pen.up()
    pen.setpos(-width//2 + x, -width//2)
    pen.down()
    pen.pencolor('deep pink')
    pen.fillcolor("hot pink")
    pen.begin_fill()
    for j in range(8):
        pen.forward(width)
        pen.left(135)
    pen.end_fill()

    x += spacing

turtle.done()