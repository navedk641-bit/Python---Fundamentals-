class Shape:
    def display(self):
        print("This is a Shape")

class Circle(Shape):
    def area(self, radius):
        print("Circle Area:", 3.14 * radius * radius)

class Rectangle(Shape):
    def area(self, length, breadth):
        print("Rectangle Area:", length * breadth)

class Triangle(Shape):
    def area(self, base, height):
        print("Triangle Area:", 0.5 * base * height)


c = Circle()
c.display()
c.area(5)

r = Rectangle()
r.display()
r.area(10, 5)

t = Triangle()
t.display()
t.area(6, 4)
