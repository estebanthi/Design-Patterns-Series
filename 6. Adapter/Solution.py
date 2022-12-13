class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square = square

    @property
    def width(self):
        return self.square.side_length

    @property
    def height(self):
        return self.square.side_length

    def get_area(self):
        return self.square.get_area()


if __name__ == "__main__":
    # Now we can use the SquareToRectangleAdapter class to use the Square class
    # as if it were a Rectangle

    square = Square(4)
    adapter = SquareToRectangleAdapter(square)

    print(adapter.width)  # 4
    print(adapter.height)  # 4
    print(adapter.get_area())  # 16