import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

arc_radius = 100

pen.up()
pen.setpos(-arc_radius, 0)
pen.down()

#Happy face
pen.setheading(-60)
pen.circle(arc_radius, 120)

#frown
pen.up()
pen.setpos(0,0)
pen.down()
pen.setheading(60)
pen.circle(-arc_radius, 120)

turtle.done()