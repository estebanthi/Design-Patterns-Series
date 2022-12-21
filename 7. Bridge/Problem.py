class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self, canvas):
        canvas.draw_line(1, 1, 2, 2, self.color)

class Canvas:
    def draw_line(self, x1, y1, x2, y2, color):
        print(f"Drawing line from ({x1}, {y1}) to ({x2}, {y2}) with color {color}")


if __name__ == "__main__":
    canvas = Canvas()
    shape = Shape("red")
    shape.draw(canvas)
