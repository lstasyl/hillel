import math

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return 0

class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height

class Parallelogram(Rectangle):
    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def square(self):
        return self.width * self.height * math.sin(math.radians(self.angle))

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Triangle(Shape):
    def __init__(self, x, y, base, height):
        super().__init__(x, y)
        self.base = base
        self.height = height

    def square(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f'Triangle: {self.base}, {self.height}'

class Scene:
    def __init__(self):
        self._figures = []

    def add_figure(self, figure):
        self._figures.append(figure)

    def total_square(self):
        return sum(f.square() for f in self._figures)

    def __str__(self):
        return '\n'.join(str(f) for f in self._figures)

r = Rectangle(0, 0, 10, 20)
r1 = Rectangle(10, 0, -10, 20)
r2 = Rectangle(0, 20, 100, 20)

c = Circle(10, 0, 10)
c1 = Circle(100, 100, 5)

p = Parallelogram(1, 2, 20, 30, 45)
p1 = Parallelogram(1, 2, 20, 30, 45)

t = Triangle(0, 0, 10, 20)

scene = Scene()
scene.add_figure(r)
scene.add_figure(r1)
scene.add_figure(r2)
scene.add_figure(c)
scene.add_figure(c1)
scene.add_figure(p)
scene.add_figure(t)

print("Total square:", scene.total_square())
