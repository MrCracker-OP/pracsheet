import math

# Base class: Shape
class Shape:
    def area(self):
        pass  # To be overridden by derived classes

# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Function to print the area
def print_area(shape):
    print(f"The area is: {shape.area()}")

# Demonstrating polymorphism
circle = Circle(7)
rectangle = Rectangle(4, 8)

print_area(circle)   # Prints the area of the circle
print_area(rectangle) # Prints the area of the rectangle
