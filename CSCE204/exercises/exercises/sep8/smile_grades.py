import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("gold")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

grade = turtle.numinput("Grades", "Enter Grade", 80,0,100)

radius = turtle.window_width()//6
eye = radius//4
mouth = radius//2

pen.up()
pen.setpos(0, -radius)
pen.down()
pen.begin_fill()
pen.circle(radius)
pen.end_fill()

pen.color("Black")
pen.up()
pen.setpos(eye,eye)
pen.down()
pen.begin_fill()
pen.circle(eye//2)
pen.end_fill()

pen.up()
pen.setpos(-eye,eye)
pen.down()
pen.begin_fill()
pen.circle(eye//2)
pen.end_fill()

if grade >= 89.5:
    pen.up()
    pen.setpos(-mouth,-mouth//2)
    pen.down()
    pen.setheading(-60)
    pen.circle(mouth, 120)

elif grade >= 79.5:
    pen.up()
    pen.setpos(-mouth,-mouth//2)
    pen.down()
    pen.forward(mouth * 2)

else:
    pen.up()
    pen.setpos(-mouth,-mouth//2)
    pen.down()
    pen.setheading(60)
    pen.circle(-mouth, 120)


turtle.done()