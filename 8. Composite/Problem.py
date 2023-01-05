class Shape:
    def move(self, x, y):
        pass


def move_shapes(shapes, x, y):
    for shape in shapes:
        shape.move(x, y)


if __name__ == "__main__":
    shape1 = Shape()
    shape2 = Shape()
    group = [shape1, shape2]

    move_shapes(group, 2, 3)
