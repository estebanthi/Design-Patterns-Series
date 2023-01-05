class Shape:
    def move(self, x, y):
        pass

class Group:
    def __init__(self):
        self._shapes = []

    def move(self, x, y):
        for shape in self._shapes:
            shape.move(x, y)

    def add(self, shape):
        self._shapes.append(shape)

    def remove(self, shape):
        self._shapes.remove(shape)


if __name__ == "__main__":
    shape1 = Shape()
    shape2 = Shape()
    group = Group()
    group.add(shape1)
    group.add(shape2)

    group.move(2, 3)
