class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        pass


class RectangleDrawMixin:
    def draw_rectangle(self):
        pass


class Rectangle(Shape, RectangleDrawMixin):
    def draw(self):
        pass


class TriangleDrawMixin:
    def draw_triangle(self):
        pass


class Triangle(Shape, TriangleDrawMixin):
    pass
