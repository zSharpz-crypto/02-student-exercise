"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0,):
        self.x = x
        self.y = y
        self.sides = sides
        if sides < 3:
            raise ValueError("More than 3")
        self.length = side_length
        if side_length <= 0:
            raise ValueError("must be positive")
        self.color = color
        self.size = pen_size
        if pen_size <= 0:
            raise ValueError("must be positive")
        self.angle = angle
        self._pen = turtle.Turtle()
        self._pen.hideturtle()

    def draw(self):
        self._pen.penup()
        self._pen.goto(self.x, self.y)
        self._pen.setheading(0)
        self._pen.pencolor(self.color)
        self._pen.pendown()
        self._pen.pensize(self.size)
        for _ in range(self.sides):
            self._pen.forward(self.length)
            self._pen.left(360//self.sides)
        self._pen.penup()

    def move_to(self, x, y):
        self.x = x
        self.y = y
        self._pen.clear()
        self.draw()
