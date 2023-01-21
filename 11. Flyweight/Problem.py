import time
from unittest.mock import Mock
import random


Image = Mock()
Image.open = lambda image: time.sleep(0.00001)


class Tree:
    def __init__(self, x, y, size, type, texture):
        self.x = x
        self.y = y
        self.size = size
        self.type = type
        self.texture = texture


if __name__ == "__main__":
    time_start = time.time()

    trees = []
    for i in range(100):
        x = random.randint(0, 1000)
        y = random.randint(0, 1000)
        size = random.randint(1, 10)
        type = random.choice(['Oak', 'Maple', 'Pine'])
        texture = Image.open('tree_texture.png')
        trees.append(Tree(x, y, size, type, texture))

    time_end = time.time()
    print(f"Time taken: {time_end - time_start}")
