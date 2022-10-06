import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

scale = turtle.numinput("U-haul", "Size (1-10)", 5, 1, 10)

width = turtle.window_width()/12 * scale
height = width // 3
cab_width = width // 6
cab_height = height // 2
dwheel = width // 6

#draw the frame
pen.up()
pen.setpos(-width // 2, 0)
pen.down()
pen.begin_fill()
pen.forward(width)
pen.left(90)
pen.forward(cab_height)
pen.left(90)
pen.forward(cab_width)
pen.right(90)
pen.forward(height - cab_height)
pen.left(90)
pen.forward(width - cab_width)
pen.left(90)
pen.forward(height)
pen.end_fill()

pen.color("black")
pen.up()
pen.setpos(-width // 3, -dwheel// 3)
pen.down()

pen.begin_fill()
pen.circle(dwheel//2)
pen.end_fill()

pen.color("black")
pen.up()
pen.setpos(width // 4, -dwheel// 3)
pen.down()

pen.begin_fill()
pen.circle(dwheel//2)
pen.end_fill()

turtle.done()