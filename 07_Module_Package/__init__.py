import math

def area(radius):
    return math.pi * radius * radius

def circumference(radius):
    return 2 * math.pi * radius
def area(length, breadth):
    return length * breadth

def perimeter(length, breadth):
    return 2 * (length + breadth)
from geometry import circle, rectangle

r = 5
print("Circle Area:", circle.area(r))
print("Circle Circumference:", circle.circumference(r))

l = 10
b = 5

print("Rectangle Area:", rectangle.area(l, b))
print("Rectangle Perimeter:", rectangle.perimeter(l, b))
