import turtle
turtle.bgcolor("black")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
radius = turtle.window_width()//6
x = 0
y = 0

for color in colors:
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(60)
    pen.circle(-radius,120)
    y += 20

turtle.done()