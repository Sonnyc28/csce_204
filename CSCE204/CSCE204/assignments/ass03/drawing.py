#Author:    Sonny Chen
import turtle
import math
turtle.bgcolor("pale green")

#Sets up pen
pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("black","white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

#Making body
pen.up()
pen.setposition(0,-105)
pen.down()

pen.begin_fill()
pen.setheading(0)
pen.circle(70)
pen.end_fill()

#Making the legs
pen.color("black","azure")
pen.up()
pen.setposition(-35,-120)
pen.setheading(0)
pen.down()

pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.up()
pen.setposition(35,-120)
pen.setheading(0)
pen.down()

pen.begin_fill()
pen.circle(20)
pen.end_fill()

#Makes the head of the cat
pen.color("black","white")
pen.up()
pen.setposition(-(200 * math.sqrt(2))/2,0)
pen.down()

pen.begin_fill()
pen.forward(200 * math.sqrt(2))
pen.left(135)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.end_fill()

#Makes facial features

#Makes eyes
pen.up()
pen.setposition(-(200 * math.sqrt(2))/2/4,70)
pen.down()
pen.color("black")

pen.begin_fill()
pen.setheading(270)
pen.circle(8)
pen.end_fill()

pen.up()
pen.setposition((200 * math.sqrt(2))/3/4,70)
pen.down()

pen.begin_fill()
pen.setheading(270)
pen.circle(8)
pen.end_fill()

#Makes nose and line/"mouth"
pen.up()
pen.setposition(-(20 * math.sqrt(2))/2,40)
pen.down()
pen.color("black","light salmon")

pen.setheading(0)
pen.begin_fill()
pen.forward(20 * math.sqrt(2))
pen.right(135)
pen.forward(20)
pen.right(90)
pen.forward(20)
pen.end_fill()

pen.up()
pen.setposition((-(20 * math.sqrt(2))/2)-5,40 - (20/math.sqrt(2)))
pen.down()
pen.color("black")

pen.setheading(0)
pen.forward((((20 * math.sqrt(2))/2)+5)*2)

#Making the ears
pen.up()
pen.setposition((-(200 * math.sqrt(2))/1/5)+12,45)
pen.color("black","pink")

pen.begin_fill()
pen.setheading(90)
pen.forward(50)
pen.down()

pen.forward(25 * math.sqrt(2))
pen.setheading(0)
pen.left(315)
pen.forward(25)
pen.right(90)
pen.forward(25)
pen.end_fill()

pen.up()
pen.setposition(((200 * math.sqrt(2))/5)-12,45)

pen.begin_fill()
pen.setheading(90)
pen.forward(50)
pen.down()

pen.forward(25 * math.sqrt(2))
pen.setheading(0)
pen.right(135)
pen.forward(25)
pen.left(90)
pen.forward(25)
pen.end_fill()

turtle.done()