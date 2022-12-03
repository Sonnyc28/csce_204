#Author: Sonny Chen
import turtle
import random
turtle.bgcolor("white")
turtle.setup(750,750)

pen = turtle.Turtle()
pen.pensize(3)      #Changes the width of the pen
pen.color("black")
pen.hideturtle()    #This hides the cursor
pen.speed(0)
boolean = (True, False)
x_playing = random.choice(boolean)
row0 = ["","",""]
row1 = ["","",""]
row2 = ["","",""]
gameover = False
players = ["X", "O"]
playerW = ""

#Making the board
def boardLines(x, y, heading):
    pen.up()
    pen.setpos(x, y)
    pen.down()
    pen.setheading(heading)
    pen.forward(turtle.window_height())

boardLines(-turtle.window_width()//6, turtle.window_height()//2, -90)
boardLines(turtle.window_width()//6, turtle.window_height()//2, -90)
boardLines(turtle.window_width()//2, -turtle.window_height()//6, 180)
boardLines(turtle.window_width()//2, turtle.window_height()//6, 180)

def draw_player(x,y):
    global gameover
    global x_playing
    if gameover == True:
        winner()
        return
    if x_playing == True:
        drawX(x,y)
        x_playing = False

    elif x_playing == False:
        drawO(x,y)
        x_playing = True

    list_thing(x,y)

#Draws X   
def drawX(x,y):
    if x > turtle.window_width()//6:
        newx = turtle.window_width()//4.2
    if y > turtle.window_height()//6:
        newy = turtle.window_height()//4.2
    if x < -turtle.window_width()//6:
        newx = -turtle.window_width()//2.35
    if y < -turtle.window_height()//6:
        newy = -turtle.window_height()//2.35
    if x > -turtle.window_width()//6 and x < turtle.window_width()//6:
        newx = -turtle.window_width()//11
    if y > -turtle.window_height()//6 and y < turtle.window_height()//6:
        newy = -turtle.window_height()//11

    pen.up()
    pen.setpos(newx,newy)
    pen.down()
    pen.setheading(45)
    pen.forward(200)
    pen.left(180)
    pen.forward(100)
    pen.left(90)
    pen.forward(100)
    pen.left(180)
    pen.forward(200)

#Draws 
def drawO(x,y):
    if x > turtle.window_width()//6:
        newx = turtle.window_width()//4.2
    if y > turtle.window_height()//6:
        newy = turtle.window_height()//4.2
    if x < -turtle.window_width()//6:
        newx = -turtle.window_width()//2.35
    if y < -turtle.window_height()//6:
        newy = -turtle.window_height()//2.35
    if x > -turtle.window_width()//6 and x < turtle.window_width()//6:
        newx = -turtle.window_width()//11
    if y > -turtle.window_height()//6 and y < turtle.window_height()//6:
        newy = -turtle.window_height()//11
    pen.up()
    pen.setpos(newx,newy)
    pen.down()
    pen.setheading(-45)
    pen.circle(100)

turtle.onscreenclick(draw_player)

def list_thing(x,y):
    global row0, row1, row2
    global gameover
    global players
    global playerW
    col = 0

    if x > turtle.window_width()//6:
        newx = turtle.window_width()//4.2
        col = 2
    if x < -turtle.window_width()//6:
        newx = -turtle.window_width()//2.35
        col = 0
    if x > -turtle.window_width()//6 and x < turtle.window_width()//6:
        newx = -turtle.window_width()//11
        col = 1

    if y > turtle.window_height()//6:
        newy = turtle.window_height()//4.2
        row0[col]=x_playing
    if y < -turtle.window_height()//6:
        newy = -turtle.window_height()//2.35
        row2[col]=x_playing
    if y > -turtle.window_height()//6 and y < turtle.window_height()//6:
        newy = -turtle.window_height()//11
        row1[col]=x_playing

    # X = False
    # O = True

    if row0[0] == row1[0] == row2[0] == True:
        playerW = players[1]
        print("Winner")
        gameover = True
    elif row0[1] == row1[1] == row2[1] == True:
        playerW = players[1]
        print("Winner")
        gameover = True
    elif row0[2] == row1[2] == row2[2] == True:
        playerW = players[1]
        print("Winner")
        gameover = True

    elif row0[0] == row1[0] == row2[0] == False:
        playerW = players[0]
        print("Winner")
        gameover = True
    elif row0[1] == row1[1] == row2[1] == False:
        playerW = players[0]
        print("Winner")
        gameover = True
    elif row0[2] == row1[2] == row2[2] == False:
        playerW = players[0]
        print("Winner")
        gameover = True

    elif row0[0] == row1[1] == row2[2] == True:
        playerW = players[1]
        print("Winner")
        gameover = True
    elif row0[0] == row1[1] == row2[2] == False:
        playerW = players[0]
        print("Winner")
        gameover = True

    elif row0[0] == row0[1] == row0[2] == True:
        playerW = players[1]
        print("Winner")
        gameover = True
    elif row1[0] == row1[1] == row1[2] == True:
        playerW = players[1]
        print("Winner")
        gameover = True
    elif row2[0] == row2[1] == row2[2] == True:
        playerW = players[1]
        print("Winner")
        gameover = True

    elif row0[0] == row0[1] == row0[2] == False:
        playerW = players[0]
        print("Winner")
        gameover = True
    elif row1[0] == row1[1] == row1[2] == False:
        playerW = players[0]
        print("Winner")
        gameover = True
    elif row2[0] == row2[1] == row2[2] == False:
        playerW = players[0]
        print("Winner")
        gameover = True

    print(row0)
    print(row1)
    print(row2)

def winner():
    style = ("Ariel", 100, "normal")
    global playerW
    pen.setheading(0)
    pen.up()
    pen.setpos(-turtle.window_width()//2, -turtle.window_height()//6)
    pen.down()
    pen.begin_fill()
    pen.forward(turtle.window_width())
    pen.left(90)
    pen.forward(turtle.window_height()//3)
    pen.left(90)
    pen.forward(turtle.window_width())
    pen.end_fill()

    if playerW == "X":
        pen.color = "sky blue"
        pen.up()
        pen.setpos(0,0)
        pen.down()
        pen.write("X is the WINNER", font = style)

turtle.done()