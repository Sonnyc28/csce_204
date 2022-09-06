#Author: Sonny Chen
import turtle
turtle.bgcolor("sky blue")

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("white")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

scale = turtle.numinput("Train", "Size (1-10)", 5, 1, 10)
