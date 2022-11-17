import shapes as sh

class House:
    def __init__(self, address, x, y, width, building_color, roof_color, has_chimney):
        self.address = address
        self.x = x
        self.y = y
        self.width = width
        self.building_color = building_color
        self.roof_color = roof_color
        self.has_chimney = has_chimney

    def draw(self, pen):
        sh.draw_rect(pen, self.x, self.y, self.width, self.width, self.building_color)
        sh.draw_rect(pen, self.x + self.width*0.35, self.y, self.width*0.3, self.width*0.6, self.roof_color)
        if self.has_chimney:
            sh.draw_rect(pen, self.x +self.width*0.65, self.y + self.width*1.4, self.width *0.2, self.width*0.4, self.building_color)
        sh.draw_triangle(pen, self.x - self.width *0.1, self.y + self.width, self.width *1.2, self.roof_color)
        sh.draw_circle(pen, self.x + self.width*0.55, self.y + self.width*0.4, self.width * 0.05, self.building_color)