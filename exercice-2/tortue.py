class Tortue:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.direction="right"
    def look_right(self):
        self.direction="right"
    def look_left(self):
        self.direction="left"
    def look_up(self):
        self.direction="up"
    def look_down(self):
        self.direction="down"
    def walk(self, distance):
        if self.direction=="right":
            self.x+=distance
        elif self.direction=="left":
            self.x-=distance
        elif self.direction =="up":
            self.y-=distance
        elif self.direction=="down":
            self.y+=distance
    def teleport(self,x,y):
        self.x=x
        self.y=y

