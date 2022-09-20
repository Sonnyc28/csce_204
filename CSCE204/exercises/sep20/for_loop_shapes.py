import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

shape = turtle.textinput("Shape", "Enter Shape").lower().strip()
shape_width = turtle.window_width()//5

pen.up()
pen.setpos(-shape_width//2, -shape_width//2)
pen.down()

if shape == "circle":
    pen.color("red")
    pen.begin_fill()
    pen.up()
    pen.setx(0)
    pen.down()
    pen.circle(shape_width//2)
    pen.end_fill()
    print("Circle")
elif shape == "square":
    pen.color("green")
    pen.begin_fill()
    for i in range(4):
        pen.forward(shape_width)
        pen.left(90)
    print("square")
    pen.end_fill()
elif shape == "triangle":
    pen.color("orange")
    pen.begin_fill()
    for i in range(3):
        pen.forward(shape_width)
        pen.left(120)
    print("Triangle")
    pen.end_fill()
else:
    print("Sorry, invalid shape")


turtle.done()