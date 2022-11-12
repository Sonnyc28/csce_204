import turtle
turtle.bgcolor("pale goldenrod")

#Sets up pen
pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("royal blue")
pen.hideturtle()    #This hides the cursor

#Let's draw a square
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
pen.setposition(-200,-200)
pen.down()

pen.color("light salmon")
pen.begin_fill()
pen.setheading(0)
pen.forward(100)
pen.right(-120)
pen.forward(100)
pen.right(-120)
pen.forward(100)
pen.end_fill()


turtle.done()       #Must be hte last line of the file