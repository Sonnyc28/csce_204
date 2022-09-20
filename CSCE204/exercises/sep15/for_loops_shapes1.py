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

pen.up()
pen.setpos(-10,100)
pen.down()

for i in range(3):
    pen.forward(120)
    pen.left(120)

turtle.done()