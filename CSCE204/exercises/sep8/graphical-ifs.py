import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

shape = turtle.textinput("Shape", "Enter Shape").lower().strip()

shape_size = turtle.window_width()//6

if shape == "circle":
    pen.up()
    pen.setpos(0, -shape_size//2)
    pen.down()
    turtle.circle(shape_size//2)

elif shape == "square":
    pen.up()
    pen.setpos(-shape_size//2, -shape_size//2)
    pen.down()
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)
    pen.left(90)
    pen.forward(shape_size)

elif shape == 'triangle':
    pen.up()
    pen.setpos(-shape_size//2, -shape_size//2)
    pen.down()
    pen.forward(shape_size)
    pen.left(120)
    pen.forward(shape_size)
    pen.left(120)
    pen.forward(shape_size)

turtle.done()