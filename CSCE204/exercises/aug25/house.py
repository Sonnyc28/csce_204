import turtle
turtle.bgcolor("pale goldenrod")

#Sets up pen
pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("royal blue")
pen.hideturtle()    #This hides the cursor


pen.up()
pen.setposition(-50,-50)
pen.down()

pen.begin_fill()
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.end_fill()

pen.up()
pen.setposition(50,50)
pen.down()

pen.color("red")
pen.begin_fill()
pen.setheading(0)
pen.forward(5)
pen.left(120)
pen.forward(110)
pen.left(120)
pen.forward(110)
pen.left(120)
pen.forward(5)
pen.end_fill()

pen.up()
pen.setposition(-10,-50)
pen.down()

pen.color("brown")
pen.begin_fill()
pen.setheading(0)
pen.forward(20)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(20)
pen.left(90)
pen.forward(40)
pen.end_fill()


turtle.done()