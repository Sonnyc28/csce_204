import turtle
import random
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)
turtle.colormode(255)
style = ("Ariel", 12, "normal")

#Ask the user for their name
name = turtle.textinput("Name", "What is your name: ").strip()
#Ask the user how man times they want to see their name
num = int(turtle.numinput("Name", "How many times do you want to see their name: ", 10, 1, 100))

#Loop through and display their name the given number of times
for i in range(num):
    x = random.randint(-turtle.window_width()//2, turtle.window_width()//2)
    y = random.randint(-turtle.window_height()//2, turtle.window_height()//2)
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    pen.color(r,g,b)
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.write(name, font = style)

turtle.done()