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


class SquareRectangle(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


if __name__ == "__main__":
    square_rectangle = SquareRectangle(5)

    print(square_rectangle.width)  # Output: 5
    print(square_rectangle.height)  # Output: 5