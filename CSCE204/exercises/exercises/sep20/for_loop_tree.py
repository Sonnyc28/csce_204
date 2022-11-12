import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

trunk_width = turtle.window_width()//12
bottom_width = trunk_width * 3
middle_width = bottom_width * 2/3
top_width = middle_width * 2/3

#draw a brown trunk
pen.color("brown")
pen.up()
pen.setpos(-trunk_width//2,-trunk_width)
pen.down()
pen.begin_fill()
for i in range(4):
    pen.forward(trunk_width)
    pen.left(90)
pen.end_fill()

#draw the bottom layer
pen.color("forest green")
pen.up()
pen.setpos(-bottom_width//2, 0)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(bottom_width)
    pen.left(120)
pen.end_fill()

#draw middle layer
pen.color("forest green")
pen.up()
pen.setpos(-middle_width//2, bottom_width * 1/2)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(middle_width)
    pen.left(120)
pen.end_fill()

#draw top layer
pen.color("forest green")
pen.up()
pen.setpos(-top_width//2, (bottom_width + middle_width) * 1/2)
pen.down()
pen.begin_fill()
for i in range(3):
    pen.forward(top_width)
    pen.left(120)
pen.end_fill()

turtle.done()