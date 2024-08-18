import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        distance = math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        return distance <= self.radius

    def __contains__(self, point):
        return self.contains(point)

    def __str__(self):
        return f'Circle(center=({self.x}, {self.y}), radius={self.radius})'

# Testing
p1 = Point(1, 2)
p2 = Point(12, 5)

c1 = Circle(1, 2, 10)

print(p1 in c1)  # True
print(p2 in c1)  # False
