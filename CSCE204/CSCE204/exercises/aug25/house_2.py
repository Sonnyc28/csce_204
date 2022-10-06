import turtle
turtle.bgcolor("pale goldenrod")

#Sets up pen
pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("royal blue")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

house_size = 100

pen.up()
pen.setposition(-house_size//2,-house_size//2)
pen.down()
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)
pen.left(90)
pen.forward(house_size)

pen.up()
pen.setposition(-house_size*0.6,house_size//2)
pen.down()
pen.setheading(0)
pen.forward(house_size*1.2)
pen.left(120)
pen.forward(house_size*1.2)
pen.left(120)
pen.forward(house_size*1.2)
pen.left(120)
pen.forward(house_size*1.2)

turtle.done()