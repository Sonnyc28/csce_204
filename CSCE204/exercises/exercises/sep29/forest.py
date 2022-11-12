import turtle
import random
turtle.bgcolor("skyblue")
turtle.setup(500,500)

pen = turtle.Turtle()
pen.pensize(2)      #Changes the width of the pen
pen.color("red")
pen.hideturtle()    #This hides the cursor
pen.speed(0)

grid_size = int(turtle.numinput("Size","Enter size", 5, 1, 10))
box_width = turtle.window_width()//grid_size
tree_size = box_width // 3
padding = tree_size
tree_trunk_height = tree_size * 2/3
tree_trunk_width = tree_trunk_height // 3
tree_leaves_radius = tree_size // 3
y = -turtle.window_height()//2 + padding

for row in range(grid_size):
    x = -turtle.window_width()//2 + padding
    for col in range(grid_size):
        pen.up()
        pen.setpos(x,y)
        pen.down()

        #Draw tree
        pen.color("brown")
        pen.begin_fill()
        for i in range(4):
            if i %2 == 0:
                pen.forward(tree_trunk_width)
            else:
                pen.forward(tree_trunk_height)
            pen.left(90)
        pen.end_fill()
        pen.up()
        pen.setpos(x + tree_trunk_width//2, y + tree_trunk_height*2/3)
        pen.down()
        pen.color("forest green")
        pen.begin_fill()
        pen.circle(tree_leaves_radius)
        pen.end_fill()

        x += box_width
    y += box_width

turtle.done()