import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        return self.x, self.y

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def dist(self, p2):
        newx = math.sqrt((p2.x - self.x) * (p2.x - self.x))
        newy = math.sqrt((p2.y - self.y) * (p2.y - self.y))
        return newx, newy
    
p1 = Point(5, 4)
p2 = Point(3, 4)

print(p1.show())
p1.move(1, 1)
print(p1.show())
print(p1.dist(p2))