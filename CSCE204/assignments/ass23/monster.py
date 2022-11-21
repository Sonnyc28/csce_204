import shapes as sh

class Monster:
    def __init__(self, x, y, width, color):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
    
    def draw(self, pen):
        self.body(pen, self.x, self.y, self.width)
        self.eyes(pen, self.x, self.y, self.width)

    def body(self, pen, x, y, width):
        pen.setheading(10)
        sh.draw_rect(pen, x, y, width, width, self.color)
        pen.up()
        pen.setpos(x-width*3/4, y+width*0.5)
        pen.down()
        pen.forward(width*2.3)
        pen.left(180)
        pen.forward(width*0.8)
        pen.left(80)
        pen.forward(width*1.2)
        pen.left(180)
        pen.forward(width*1.2)
        pen.left(90)
        pen.forward(width*0.5)
        pen.left(90)
        pen.forward(width*1.2)
        pen.left(180)
        pen.forward(width*1.2)
        pen.right(90)
        pen.forward(width*0.25)
        pen.setheading(0)
        pen.right(90)
        pen.forward(width*0.36)
        pen.right(90)
        pen.forward(width*0.25)
        pen.setheading(300)
        pen.color("black")
        pen.circle(width*1/4,120)
        pen.setheading(-18)
        sh.draw_triangle(pen, x+width*1/3, y+width*1.56/5, width*1/12, "white")
        pen.setheading(35)
        sh.draw_triangle(pen, x+width*1.6/3, y+width*1.5/5, width*1/12, "white")
        pen.setheading(0)

    def eyes(self, pen, x, y, width):
        pen.setheading(10)
        sh.draw_circle(pen, x+width*0.8/4, y+width*0.5, width*1/6, "white")
        sh.draw_circle(pen, x+width*2.8/4, y+width*0.5, width*1/6, "white")

        sh.draw_circle(pen, x+width*0.8/4, y+width*0.55, width*1/8, "black")
        sh.draw_circle(pen, x+width*2.8/4, y+width*0.55, width*1/8, "black")

        sh.draw_circle(pen, x+width*0.8/4, y+width*0.7, width*1/30, "white")
        sh.draw_circle(pen, x+width*2.8/4, y+width*0.7, width*1/30, "white")
        pen.setheading(0)