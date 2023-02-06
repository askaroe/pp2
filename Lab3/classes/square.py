class Shape():
    def __init__(self) -> None:
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length = 0):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length * self.length


x = int(input())
s = Square(x)
print(s.area())

print(Square().area())

