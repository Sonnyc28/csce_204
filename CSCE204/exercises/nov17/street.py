from house import House
import turtle
turtle.bgcolor("skyblue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("black")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

houses = []
houses.append(House("1 A Street", -200, 0, 50, "medium aquamarine", "hot pink", True))
houses.append(House("2 A Street", -100, 100, 50, "medium turquoise", "violet", False))
houses.append(House("3 A Street", 0, 0, 50, "green", "red", True))
houses.append(House("4 A Street", 100, -100, 50, "gold", "blue", True))
houses.append(House("5 A Street", 200, 0, 50, "purple", "sandy brown", False))

for house in houses:
    house.draw(pen)
turtle.done()