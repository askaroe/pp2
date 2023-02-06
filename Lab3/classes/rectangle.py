class Shape():
    def __init__(self):
        pass
    def area(self, length, width):
        return 0

class Rectangle(Shape):
    def __init__(self, length = 0, width = 0):
        Shape.__init__(self)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

l = int(input())
w = int(input())
r = Rectangle(l, w)
print(r.area())

print(Rectangle().area())