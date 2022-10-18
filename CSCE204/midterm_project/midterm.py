import turtle
import random
turtle.bgcolor("skyblue")
turtle.setup(1500,750)

pen = turtle.Turtle()
pen.pensize(5)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

roadHeight = turtle.window_height()//5

bikeList = []
bikeColor = []

bikeNum = int(turtle.numinput("Bikes","Enter Number of Bikes: ", 5, 1, 10))

#Writing title
style = ('Times New Roman', 50, 'bold')
pen.color("black")
pen.up()
pen.setpos(-turtle.window_width()//2 + roadHeight//2, turtle.window_height()//2 - roadHeight//3*2)
pen.down()
pen.write("Biking Party", font= style)

#box for each bike
boxWidth = turtle.window_width()//bikeNum
bikeLine = boxWidth//6
smallLine = bikeLine * 5/8
padding = bikeLine

fontSize = int(smallLine/3)

#Make the background
pen.up()
pen.setpos(-turtle.window_width()//2 , turtle.window_height()//2 - roadHeight)
pen.color("burlywood")
pen.down()
pen.begin_fill()
for i in range(2):
    pen.forward(turtle.window_width())
    pen.right(90)
    pen.forward(roadHeight * 3)
    pen.right(90)
pen.end_fill()

#Asks user for bike names and colors
for bike in range(bikeNum):
    names = turtle.textinput("Bike Name", "Enter Name of Bike: ").strip()
    colors = turtle.textinput("Bike Color", "Enter Color of Bike: ").strip().lower()
    bikeList.append(names)
    bikeColor.append(colors)

x = -turtle.window_width()//2 + padding
y = random.randint(-turtle.window_height()//2 + roadHeight, turtle.window_height()//2 - roadHeight - (bikeLine // 3))

for j in range(bikeNum):
    pen.up()
    pen.setpos(x,y)
    pen.down()

    #Draw bikes
    pen.setheading(0)
    pen.color("black")
    pen.circle(bikeLine // 3)
    pen.up()
    pen.setpos(x,y+bikeLine // 3)
    pen.color(bikeColor[j])
    pen.down()
    pen.left(60)
    pen.forward(bikeLine)
    pen.right(60)
    pen.forward(bikeLine * 3/8)
    pen.right(180)
    pen.forward(bikeLine * 3/8)
    pen.left(60)
    pen.forward(bikeLine * 3/8)
    pen.left(120)
    for k in range(3):
        pen.forward(smallLine)
        pen.right(120)
    pen.forward(smallLine)
    pen.right(60)
    for k in range(3):
        pen.forward(smallLine)
        pen.right(120)
    pen.setheading(0)
    pen.left(60)
    pen.forward(smallLine * 1/3)
    pen.right(60)
    pen.forward(smallLine * 1/3)
    pen.right(180)
    pen.forward(smallLine * 1/3 * 2)
    pen.up()
    pen.setpos(x + smallLine * 2,y+bikeLine // 3 *2)
    pen.down()
    pen.color("black")
    pen.circle(bikeLine // 3)

    #Writing the names
    style2 = ('Ariel', fontSize, 'bold')
    pen.color("black")
    pen.up()
    pen.setpos(x + smallLine //3 *2 ,y - smallLine // 2)
    pen.down()
    pen.write(bikeList[j], font=style2)

    x+=boxWidth
    y = random.randint(-turtle.window_height()//2 + roadHeight, turtle.window_height()//2 - roadHeight)

turtle.done()