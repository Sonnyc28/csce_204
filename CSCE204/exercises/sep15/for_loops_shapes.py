import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

#using a for loop draw a square
for i in range (4):
    pen.forward(100)
    pen.left(90)

turtle.done()