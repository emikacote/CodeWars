from math import pi

class Shape:
    def __init__(self, area): self.area = area
    def __lt__(self, other): return self.area < other.area

class Square(Shape):
    def __init__(self, side): self.area = side**2

class Rectangle(Shape):
    def __init__(self, width, height): self.area = width*height

class Triangle(Shape):
    def __init__(self, base, height): self.area = 0.5*base*height

class Circle(Shape):
    def __init__(self, radius): super().__init__(pi*radius**2)

class CustomShape(Shape):
    pass
